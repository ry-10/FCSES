import ee

# 初始化GEE
ee.Initialize()

# 导入Landsat 8数据
landsat8 = ee.ImageCollection('LANDSAT/LC08/C02/T1_L2') \
    .filterDate('2022-05-01', '2022-12-01') \
    .filter(ee.Filter.lt('CLOUD_COVER', 20)) \
    .filterBounds(yanjiuqu)  # 需要定义yanjiuqu的范围

# 定义派生变量的计算方法
def addIndices(image):
    ndvi = image.normalizedDifference(['SR_B5', 'SR_B4']).rename('NDVI')
    evi = image.expression(
        '2.5 * ((NIR - RED) / (NIR + 6 * RED - 7.5 * BLUE + 1))', {
          'NIR': image.select('SR_B5'),
          'RED': image.select('SR_B4'),
          'BLUE': image.select('SR_B2')
        }).rename('EVI')
    return image.addBands([ndvi, evi])

# 应用指数函数到Landsat 8数据
landsatIndices = landsat8.map(addIndices)

# 合成波段
bands = ['SR_B2', 'SR_B3', 'SR_B4', 'SR_B5', 'SR_B6', 'SR_B7', 'NDVI', 'EVI']
imgcol_median = landsatIndices.select(bands).median()
construct_img = imgcol_median.clip(yanjiuqu)  # 需要定义yanjiuqu的范围

# 导入训练数据
# 需要定义featureCollection
train_data = construct_img.sampleRegions(
    collection=featureCollection,
    properties=['AGB'],
    scale=30
)

# 精度评价
withRandom = train_data.randomColumn('random')
split = 0.7
trainingData = withRandom.filter(ee.Filter.lt('random', split))
testingPartition = withRandom.filter(ee.Filter.gte('random', split))

# 分类方法选择随机森林
classifier = ee.Classifier.smileRandomForest(100).setOutputMode('REGRESSION') \
    .train(
        features=trainingData,
        classProperty='AGB',
        inputProperties=bands
    )

# 对影像进行分类
regression = construct_img.classify(classifier, 'predicted')
