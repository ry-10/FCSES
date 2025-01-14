import open3d as o3d
import pdal
import json
import laspy
import numpy as np
# 抽稀las数据
def las_to_pcd(input_las, output_pcd):
    # 构建PDAL管线
    pipeline_json = json.dumps({
        "pipeline": [
            input_las,  # 输入的LAS文件
            {
                "type": "writers.pcd",  # 指定writer类型为PCD
                "filename": output_pcd  # 输出的PCD文件
            }
        ]
    })

    # 创建并执行管线
    pipeline = pdal.Pipeline(pipeline_json)
    pipeline.execute()
def pcd_to_las(input_pcd, output_las):
    # # 创建一个新的LAS文件
    # header = laspy.LasHeader(version="1.4", point_format=2)
    # header.x_scale = 0.01
    # header.y_scale = 0.01
    # header.z_scale = 0.01
    #
    # las = laspy.LasData(header)
    #
    # # 将点云数据填入LAS文件
    # las.x = points[:, 0]
    # las.y = points[:, 1]
    # las.z = points[:, 2]
    #
    # # 保存LAS文件
    # las.write(output_las)
    # 读取PCD文件
    cloud = o3d.io.read_point_cloud(input_pcd)
    points = np.asarray(cloud.points)
    las = laspy.file.File(input_las_path)
    header = las.header

    print(header+header.version)

    # 创建一个新的LasFile对象
    outfile = laspy.file.File(output_las, mode="w", header=header)

    # 将点云数据填入LAS文件
    outfile.x = points[:, 0]
    outfile.y = points[:, 1]
    outfile.z = points[:, 2]

    # 关闭文件以完成写入
    outfile.close()
# 使用示例
input_las_path = r"C:\Users\Administrator\Desktop\py-gra\graduation-py\pycrown\example\data\UAV.las"  # 替换为您的LAS文件路径
tem_pcd = r"C:\Users\Administrator\Desktop\py-gra\graduation-py\pycrown\example\data\UAV.pcd"  # 替换为您希望创建的PCD文件路径
output_las_path = r"C:\Users\Administrator\Desktop\py-gra\graduation-py\pycrown\example\data\UAV_filtered.las"

las_to_pcd(input_las_path, tem_pcd)
# 加载LAS文件（需要转换为PCD或其他兼容格式）,open3d不支持读取las数据
cloud = o3d.io.read_point_cloud(tem_pcd)
print(f"PointCloud before filtering: {len(cloud.points)} data points.")

# 应用体素下采样过滤器
# 单位为米，数值越大抽稀的程度越大
voxel_size = 0.2
cloud_filtered = cloud.voxel_down_sample(voxel_size)
print(f"PointCloud after filtering: {len(cloud_filtered.points)} data points.")

# 可视化原始和过滤后的点云
# o3d.visualization.draw_geometries([cloud], window_name="Original Cloud")
# o3d.visualization.draw_geometries([cloud_filtered], window_name="Filtered Cloud")
# 保存抽稀后的点云为PCD文件
o3d.io.write_point_cloud(tem_pcd, cloud_filtered)
# PCD转为las数据
pcd_to_las(tem_pcd,output_las_path)
ratio = len(cloud_filtered.points)/len(cloud.points)
print(f"las数据抽稀完成,比例为:{ratio}")

