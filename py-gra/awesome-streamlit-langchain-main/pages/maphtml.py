import ee
import streamlit as st
import folium
from streamlit_folium import folium_static

# 初始化 GEE
ee.Initialize()

# 选择一个 GEE 数据集
# image = ee.Image('CGIAR/SRTM90_V4')
featureCollection = ee.FeatureCollection('projects/ee-haoz13503/assets/qilian')


# 获取地图瓦片
# map_id_dict = image.getMapId({'palette': ['blue', 'green', 'red']})
map_id_dict = featureCollection.getMapId({'color': 'green'})

# 创建一个 folium 地图
map = folium.Map(location=[39,100], zoom_start=7)
folium.TileLayer(
    tiles=map_id_dict['tile_fetcher'].url_format,
    attr='Google Earth Engine',
    overlay=True,
    name='SRTM90_V4',
).add_to(map)
folium.Icon().add_to(map)
folium.ClickForLatLng().add_to(map)
folium.LayerControl().add_to(map)

# 在 Streamlit 中显示地图
st.title('Streamlit and GEE')
col1, col2 = st.columns([3, 1])  # 创建比例为 3:1 的两列
with col1:
    folium_static(map,width=800,height=800)  # 地图会显示在较宽的列中
with col2:
    st.write("这里是其他内容")


