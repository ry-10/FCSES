import streamlit as st
import geemap.foliumap as geemap
import ee

# 初始化 Google Earth Engine
ee.Authenticate()
ee.Initialize(project='ee-haoz13503')

# 创建一个 Streamlit 页面
st.title("Google Earth Engine Tiles in Streamlit")

# 创建一个 GEE 图层
image = ee.Image('USGS/SRTMGL1_003')

# 设置可视化参数
visualization = {
    'min': 0,
    'max': 3000,
    'palette': ['blue', 'green', 'red']
}

# 创建一个地图对象
map = geemap.Map()
map.addLayer(image, visualization, "SRTM DEM")

# 将地图转换为 HTML，并在 Streamlit 中展示
map.to_streamlit(height=700)
