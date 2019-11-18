#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2019/10/21
# @Author : xulh
# @File : olr_data.py

import numpy as np
import Ngl,Nio
import datetime

def getOlrData(dataInputPaths,timeRanges,timeTypes,elements,dataOutputPaths,dataOutputNames,latRanges,lonRanges,outputData):
	
	t1 = datetime.datetime.strptime(timeRanges[0], "%Y%m%d")
	t2 = datetime.datetime.strptime(timeRanges[1], "%Y%m%d")
	t_day = (t2-t1).days
	f = Nio.open_file(dataInputPaths, "r")
	prateOlr = f.variables[elements][t1.day-1:t1.day+t_day]
	lat = f.variables["lat"][:]
	lon = f.variables["lon"][:]
	outputData[elements] = prateOlr
	outputData["lat"] = lat
	outputData["lon"] = lon
	return outputData
