"""
PyCrown - Fast raster-based individual tree segmentation for LiDAR data
-----------------------------------------------------------------------
Copyright: 2018, Jan Zörner
Licence: GNU GPLv3
"""

from datetime import datetime
# 忽略报错即可，在其他环境运行
from pycrown import PyCrown
import sys

if __name__ == '__main__':

    TSTART = datetime.now()

    F_CHM = sys.argv[1]
    F_DTM = sys.argv[2]
    F_DSM = sys.argv[3]
    F_LAS = sys.argv[4]

    PC = PyCrown(F_CHM, F_DTM, F_DSM, F_LAS, outpath='result')

    # Cut off edges
    # PC.clip_data_to_bbox((1802200, 1802400, 5467250, 5467450))

    # Smooth CHM with 5m median filter
    PC.filter_chm(5, ws_in_pixels=True)

    # Tree Detection with local maximum filter
    PC.tree_detection(PC.chm, ws=5, ws_in_pixels=True, hmin=10.)

    # Clip trees to bounding box (no trees on image edge)
    # original extent: 1802140, 1802418, 5467295, 5467490
    # PC.clip_trees_to_bbox(bbox=(1802150, 1802408, 5467305, 5467480))
    # PC.clip_trees_to_bbox(bbox=(1802160, 1802400, 5467315, 5467470))
    PC.clip_trees_to_bbox(inbuf=11)  # inward buffer of 11 metre

    # Crown Delineation
    PC.crown_delineation(algorithm='dalponteCIRC_numba', th_tree=10.,
                         th_seed=0.7, th_crown=0.55, max_crown=10.)

    # Correct tree tops on steep terrain
    PC.correct_tree_tops()

    # Calculate tree height and elevation
    PC.get_tree_height_elevation(loc='top')
    PC.get_tree_height_elevation(loc='top_cor')

    # Screen small trees
    PC.screen_small_trees(hmin=10., loc='top')

    # Convert raster crowns to polygons
    PC.crowns_to_polys_raster()
    PC.crowns_to_polys_smooth(store_las=True)

    # Check that all geometries are valid
    PC.quality_control()

    # Export results
    PC.export_raster(PC.chm, PC.outpath / 'chm.tif', 'CHM')
    PC.export_tree_locations(loc='top')
    PC.export_tree_locations(loc='top_cor')
    # PC.export_tree_crowns(crowntype='crown_poly_raster')
    # PC.export_tree_crowns(crowntype='crown_poly_smooth')

    TEND = datetime.now()

    print(f"Number of trees detected: {len(PC.trees)}")
    print(f'Processing time: {TEND-TSTART} [HH:MM:SS]')
