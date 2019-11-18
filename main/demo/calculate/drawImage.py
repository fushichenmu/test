#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2019/10/21
# @Author : xulh
# @File : drawImage.py

import Ngl

from handler.contour_drawing import draw_contour
from handler.seaPolyline_drawing import draw_sea_polyline
from handler.workstation_setting import create_workstation
from handler.background_setting import setting_bgImage
from handler.font_setting import setting_font

output_directory_absolute_path = "/home/xulh/nfsshare/cdbdata/data/NOAA/noaa_olr/"


def draw(data, lon, lat, dataSources, latRanges, lonRanges, imgTypes, colorBarName, imgOutputPaths, img_output_names,
         mainTitle, subTitles, unit, dataSources1):
    '''
       方法定义： 用于绘图。（画的什么图不清楚，建议名字优化一下）
       @param data: 数据（是否是2D呢？？）
       @param lon: 精度
       @param lat: 纬度 （建议常用的查询要素封装成到一个类中去）
       @param dataSources: 数据源
       @param latRanges:   纬度范围
       @param lonRanges: 经度
       @param imgTypes:  图片格式
       @param colorBarName:  颜色名称（到底是啥玩意）
       @param imgOutputPaths: （图片输出路径）
       @param img_output_names: （图片名称）
       @param mainTitle: 主标题
       @param subTitles: 副标题
       @param unit: 单元（什么的单元？？？）
       @param dataSources1:  数据源1（这个数据源1是干嘛用的，为啥叫1）
       @return: 无返回值，只是用于画图，然后保存而已。
    '''

    #1.数据信息提取Begin
    startLon = lonRanges[0];endLon = lonRanges[1]
    startLat = latRanges[0];endLat = latRanges[1]

    print(" Longitude starts with %f ,ends with %f " % (startLon, endLon))#获取经纬度起止值(此处建议引入日志配置，而不是简单的print函数)
    print(" Latitude starts with %f ,ends with %f " % (startLon, endLon))
    image_path = output_directory_absolute_path + img_output_names #指定输出文件 (常量不应该写死在方法内部，应该定义全局变量，或者由配置文件引入。)

    #2.绘图环境配置Begin
    wks = create_workstation(colorBarName, image_path)



    # 3.绘制等值线图
    plot = draw_contour(colorBarName, data, endLat, endLon, imgOutputPaths, lat, lon, startLat, startLon, wks)
    #4.绘制海岸线图
    draw_sea_polyline(endLon, plot, wks)
    Ngl.draw(plot)
    Ngl.frame(wks)
    Ngl.end()

    #5.字体绘制
    im = setting_font(dataSources1, image_path, mainTitle, subTitles, unit)

    #6.加载ncc.png(不清楚这个作用是什么？ 背景色吗)
    setting_bgImage(im)
    print(image_path + ".png"); im.save(image_path + ".png")

