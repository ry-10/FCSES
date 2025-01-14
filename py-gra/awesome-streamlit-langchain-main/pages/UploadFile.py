import streamlit as st
import os

# 设置保存文件的路径
save_path = 'files/shp'

# 确保路径存在
if not os.path.exists(save_path):
    os.makedirs(save_path)

# Streamlit 文件上传组件
uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    # 获取文件名
    file_name = uploaded_file.name

    # 创建完整的文件路径
    file_path = os.path.join(save_path, file_name)

    # 以二进制写模式打开文件
    with open(file_path, "wb") as f:
        # 将上传的文件写入到文件系统
        f.write(uploaded_file.getbuffer())

    st.success(f"File '{file_name}' saved at '{file_path}'!")
