#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2019/10/21
# @Author : xulh
# @File : olr_main.py

import sys
from thirdTime.calculate import drawImage, olr_data, olr_calculate_data

#数据路径
dataInputPaths = "/home/xulh/nfsshare/cdbdata/data/NOAA/noaa_olr/"
#时间范围
timeRanges = sys.argv[1].split(",")
#季：season 月：mon 中国候：five 日：day
timeTypes = sys.argv[2]
#要素
elements = "olr"
#文件名
fileName = "2019_10.nc"
#输出路径
dataOutputPaths = ""
#输出名
dataOutputNames = ""
#纬度范围
latRanges = [-60,60]
#精度范围
lonRanges = [0,360]
imgOutputPaths="/home/xulh/mnt/python/python_script/orl/"
colorBarName = "/home/xulh/mnt/python/python_script/orl/color_fy3b_olr1.ini"
imgOutputNames = "test1"
mainTitle="对流活动平均场"
subTitles = "2019年10月22日"
unit = "单位：W/㎡"
outputData = {}
dataSources="数据：NOAA_OLR"

data = olr_data.getOlrData(dataInputPaths + fileName, timeRanges, timeTypes, elements, dataOutputPaths, dataOutputNames, latRanges, lonRanges, outputData)
olrData = olr_calculate_data.caluOlrData(data[elements], "avg", "time")
print(olrData.shape)
#tool.getColorMap("/home/xulh/mnt/python/python_script/orl/color_fy3b_olr1.ini")
lon = data["lon"]
lat = data["lat"]
drawImage.draw(olrData, lon, lat, "olrData", latRanges, lonRanges, "png", colorBarName, imgOutputPaths, imgOutputNames, mainTitle, subTitles, unit, dataSources)


