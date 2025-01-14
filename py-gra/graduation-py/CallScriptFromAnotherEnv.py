import subprocess
import os
# 调用单木分割模块的脚本，输入CHM\DTM\DSM\LAS数据，输出树高（csv）文件。
# 本模块结果数据只保存当前处理一次的，历史数据会删除，具有及时性。
# 指定工作目录
working_directory = r"C:\Users\Administrator\Desktop\py-gra\graduation-py\pycrown\example"

# 激活环境的命令
activate_command = r'"C:\Program Files\ArcGIS\Pro\bin\Python\Scripts\activate.bat" myenv'

# 要运行的Python脚本
script_command = "python example.py"

# 指定输入数据的路径（相对路径）
CHMPath = 'data/CHM.tif'
DTMPath = 'data/DEM.tif'
DSMPath = 'data/DSM.tif'
LASPath = 'data/las.las'

# 组合命令
command = f'{activate_command} && {script_command} {CHMPath} {DTMPath} {DSMPath} {LASPath}'
print(command)

# command = script_command

# 使用 subprocess.Popen 来执行命令，并设置工作目录
with subprocess.Popen(command, cwd=working_directory, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) as process:
    # 等待进程结束
    stdout, stderr = process.communicate()

    # 输出标准输出和标准错误
    # print(stdout.decode())
    # print(stderr.decode())
    try:
        print(stdout.decode('utf-8'))
    except UnicodeDecodeError:
        print(stdout.decode('cp936'))  # Windows 中常用的编码
    # 尝试不同的编码方式
    try:
        print(stderr.decode('utf-8'))
    except UnicodeDecodeError:
        print(stderr.decode('cp936'))  # Windows 中常用的编码
    # 输出退出码
    print("Exit Code:", process.returncode)



