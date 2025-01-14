import open3d as o3d
import pdal
import json
import laspy
import numpy as np

def pcd_to_las(input_pcd, output_las):
    # 读取PCD文件
    cloud = o3d.io.read_point_cloud(input_pcd)
    points = np.asarray(cloud.points)

    # 创建一个新的LAS文件
    header = laspy.LasHeader(version="1.4", point_format=2)
    header.x_scale = 0.01
    header.y_scale = 0.01
    header.z_scale = 0.01

    las = laspy.LasData(header)

    # 将点云数据填入LAS文件
    las.x = points[:, 0]
    las.y = points[:, 1]
    las.z = points[:, 2]

    # 保存LAS文件
    las.write(output_las)
output_pcd_path = r"C:\Users\Administrator\Desktop\py-gra\graduation-py\pycrown\example\data\UAV.pcd"  # 替换为您希望创建的PCD文件路径
output_las_path = r"C:\Users\Administrator\Desktop\py-gra\graduation-py\pycrown\example\data\UAV_filtered.las"

pcd_to_las(output_pcd_path, output_las_path)