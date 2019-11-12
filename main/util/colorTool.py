#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2019/10/21
# @Author : xulh
# @File : colorTool.py

import numpy as np
import Ngl

def getColorCfg(colorFi):
	#print("vals:"+colorFi)
	vals = open(colorFi,"r")
	lines = vals.readlines()
	#print(lines)
	return lines

def getColorMap(colorFi):
	vals = getColorCfg(colorFi)
	i_colorNum = len(vals) - 6
	af_colorMap = np.full((i_colorNum, 3), 255.)
	j=0
	while(j<i_colorNum):
		af_colorTmp = vals[j+6].split(",")
		af_colorMap[j,0] = float(af_colorTmp[0])/255.
		af_colorMap[j,1] = float(af_colorTmp[1])/255.
		af_colorMap[j,2] = float(af_colorTmp[2])/255.
		j = j + 1
	#print(af_colorMap)
	return af_colorMap

def getColorValueDef(colorFi):
	vals = getColorCfg(colorFi)
	af_colorValueDef = list(map(lambda x:float(x),vals[4].split(",")))
	print(np.array(af_colorValueDef))
	return np.array(af_colorValueDef)

def getColorOrder(colorFi):
	vals = getColorCfg(colorFi)
	ai_colorOrder = list(map(lambda x:int(x),vals[2].split(",")))
	#print(np.array(ai_colorOrder)+5)
	return np.array(ai_colorOrder)+5
