#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2019/10/21
# @Author : xulh
# @File : olr_calculate_data.py

import numpy as np


def caluOlrData(plrData,statTypes,statDims):
	if statTypes=="avg":
		outputData = np.average(plrData,0)
		return outputData

