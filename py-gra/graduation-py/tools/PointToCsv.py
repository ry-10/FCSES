import geopandas as gpd
import pandas as pd
# 将点数据转为csv表格，以便于gee使用
def shp_to_csv(shp_path, csv_path):
    """
    将点类型的Shapefile转换为CSV格式。

    参数:
    shp_path (str): 输入Shapefile的路径。
    csv_path (str): 输出CSV文件的路径。
    """
    # 读取Shapefile
    gdf = gpd.read_file(shp_path)

    # 检查几何类型是否为Point
    if not all(gdf.geom_type == 'Point'):
        raise ValueError("Shapefile不包含全部为点的几何类型")

    # 提取坐标和属性
    df = pd.DataFrame(gdf)
    df['X'] = gdf.geometry.x
    df['Y'] = gdf.geometry.y

    # 将数据保存为CSV
    df.to_csv(csv_path, index=False)

# 示例用法
input_shp = r'C:\Users\Administrator\Desktop\py-gra\graduation-py\pycrown\example\result\tree_location_top_cor.shp'  # 替换为你的Shapefile路径
output_csv = 'path_to_your_output_file.csv'  # 替换为输出文件的路径

shp_to_csv(input_shp, output_csv)
