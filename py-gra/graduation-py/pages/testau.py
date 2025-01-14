import ee
import streamlit as st
try:
    ee.Authenticate()
    # 初始化 Earth Engine
    ee.Initialize(project='ee-haoz13503')

    # 获取并打印一个数据集的信息作为测试
    dataset = ee.Image('USGS/SRTMGL1_003')
    info = dataset.getInfo()
    print("成功获取数据集信息：", info['id'])
    st.write("成功获取数据集信息：", info['id'])
except ee.EEException as e:
    print("Google Earth Engine 认证失败：", e)
except Exception as e:
    print("其他错误：", e)
