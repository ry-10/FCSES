import json
import pdal

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
input_las_path = r"C:\Users\Administrator\Desktop\py-gra\graduation-py\pycrown\example\data\UAV.las"  # 替换为您的LAS文件路径
tem_pcd = r"C:\Users\Administrator\Desktop\py-gra\graduation-py\pycrown\example\data\UAV.pcd"  # 替换为您希望创建的PCD文件路径

las_to_pcd(input_las_path, tem_pcd)
