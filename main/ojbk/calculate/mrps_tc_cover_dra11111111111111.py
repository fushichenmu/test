import Ngl
from thirdTime.util import colorTool, IoUtil
import os
import numpy as np

def setCommonRes(res=None):
    if res == None:
        res = Ngl.Resources()
    res.gsnFrame = False
    res.gsnDraw = False
    res.tiMainOn = False
    res.gsnLeftString = ""
    res.gsnRightString = ""
    res.tmXBMinorOn = False
    res.tmYLMinorOn = False
    res.vpXF = 0
    res.vpYF = 1
    res.vpWidthF = 1.
    res.vpHeightF = 1.
    res.cnConstFEnableFill = False
    res.cnNoDataLabelOn = False
    res.cnConstFLabelOn = False
    res.lbLabelBarOn = False
    res.cnInfoLabelOn = False
    res.tmXBOn = False
    res.tmXTOn = False
    res.tmYLOn = False
    res.tmYROn = False
    res.tmXBMinorOn = False
    res.tmYLMinorOn = False


def drawContour(input_data, lon, lat, area_name, config_path, output_img_name, output_img_path, business_id, element_type, input_tulifile_name, acc, params_path):
    '''
    绘制色斑图
    @param input_data: 绘图输入数据
    @param lon: 绘图经度范围
    @param lat: 绘图纬度范围
    @param area_name:区域名称（CH特殊处理）
    @param config_path:配置文件路径
    @param output_img_name:输出文件名
    @param output_img_path:输出路径
    @param business_id:业务id
    @param element_type:业务id预留字段
    @param input_tulifile_name:图例存放文件名
    @param acc:相关系数检验阈值
    @param params_path:参数文件路径+名称
    @return:无返回值
    '''
    minLon = min(lon)
    maxLon = max(lon)
    minLat = min(lat)
    maxLat = max(lat)
    imgSizes = IoUtil.readConfig_int(config_path, "imgSize_" + business_id).split(",")
    # 创建工作台
    wkres = Ngl.Resources()
    wkres.wkWidth = int(imgSizes[0])
    wkres.wkHeight = int(imgSizes[0])
    workstation = Ngl.open_wks("png", output_img_path+output_img_name, wkres)
    ws_id = Ngl.get_workspace_id()
    rlist = Ngl.Resources()
    rlist.wsMaximumSize = 300000000
    Ngl.set_values(ws_id, rlist)


    # 判断文件路径是否存在，如果不存在，则创建，此处是创建多级目录
    if not os.path.isdir(output_img_path):
        os.makedirs(output_img_path)
    drawData = input_data

    color_cfg_file = IoUtil.readConfig_int(config_path, "COLORCFG_" + business_id + "_" + element_type).split(",")
    color_cfg_file = "$NCLJOB_ROOTS/extComponent/ncl_component/config/" +color_cfg_file
    cmap = colorTool.getColorMap(color_cfg_file)
    Ngl.define_colormap(workstation, cmap)

    # 图例信息落文件（给后台java生成图例，合成图片使用）
    f = Ngl.asciiread(color_cfg_file,-1,"string")
    vs = f[4].split(",")[::-1]
    rgb = f[11:][::-1]
    colorInfo = ("COLORVALUE=" +','.join(vs),"RGB="+','.join(rgb))
    del vs
    del rgb
    if os.path.exists(output_img_path + input_tulifile_name):
        dataInfoArr = Ngl.asciiread(output_img_path + input_tulifile_name,-1,"string")
        index=[dataInfoArr.index(str) for str in dataInfoArr if str.contains("COLORVALUE=") ]
        # if not 这个地方需要讨论怎么实现这个missing value
    else:
        dataInfoArr = colorInfo
    Ngl.asciiwrite(output_img_path + input_tulifile_name,dataInfoArr)

    cnLinesOn = IoUtil.readConfig_int(config_path, "cnLinesOn_" + business_id)
    cnFillOn = IoUtil.readConfig_int(config_path, "cnFillOn_" + business_id)
    XYon = IoUtil.readConfig_int(config_path, "isXYon_" + business_id)
    borderOn = IoUtil.readConfig_int(config_path, "borderOn_" + business_id)
    mpGeoOn = IoUtil.readConfig_int(config_path, "mpGeoOn_" + business_id)
    lambertOn = IoUtil.readConfig_int(config_path, "lambertOn_" + business_id)
    markerOn = IoUtil.readConfig_int(config_path, "cnMarkerOn_" + business_id)

    res = Ngl.Resources()
    setCommonRes(res)
    res.gsnAddCyclic = False
    res.mpMinLonF = minLon
    res.mpMaxLonF = maxLon
    res.mpMinLatF = minLat
    res.mpMaxLatF = maxLat
    res.mpCenterLonF = (minLon + maxLon) * 0.5
    res.mpGridAndLimbOn = False
    res.mpFillOn = False
    res.cnLevels = colorTool.getColorValueDef(color_cfg_file)
    if(readParams(params_path,"cnLevels") != ""):
        res.cnLevels = float(readParams(params_path,"cnLevels"),",")
    res.cnLevelSelectionMode = "ExplicitLevels"
    if(XYon == "True"):
        tmXBLabelFontHeightF = IoUtil.readConfig_int(config_path, "X_LABEL_" + business_id)  # X轴标签字体大小
        tmXBMajorLengthF = IoUtil.readConfig_int(config_path, "X_LENGTH_" + business_id)  # X轴主刻度线长度
        tmXBMajorThicknessF = IoUtil.readConfig_int(config_path, "X_THICK_" + business_id)  # X轴主刻度线宽
        tmXBTickSpacingF = IoUtil.readConfig_int(config_path, "X_SPACE_" + business_id)  # X轴主刻度间隔
        tmYLTickSpacingF = IoUtil.readConfig_int(config_path, "Y_SPACE_" + business_id)
        tmYLLabelFontHeightF = IoUtil.readConfig_int(config_path, "Y_LABEL_" + business_id)
        tmYLMajorLengthF = IoUtil.readConfig_int(config_path, "Y_LENGTH_" + business_id)
        tmYLMajorThicknessF = IoUtil.readConfig_int(config_path, "Y_THICK_" + business_id)
        tmXMajorGrid = IoUtil.readConfig_int(config_path, "tmXMajorGrid_" + business_id)  # 是否绘制X坐标轴主刻度网格线
        tmXMajorGridLineDashPattern = float(IoUtil.readConfig_int(config_path, "tmXMajorGridLineDashPattern_" + business_id))  # X坐标轴主刻度网格线线型
        tmXMajorGridThicknessF = float(IoUtil.readConfig_int(config_path, "tmXMajorGridThicknessF_" + business_id))  # X坐标轴主刻度网格线线宽
        tmYMajorGrid = IoUtil.readConfig_int(config_path, "tmYMajorGrid_" + business_id)
        tmYMajorGridLineDashPattern = float(
            IoUtil.readConfig_int(config_path, "tmYMajorGridLineDashPattern_" + business_id))
        tmYMajorGridThicknessF = float(IoUtil.readConfig_int(config_path, "tmYMajorGridThicknessF_" + business_id))
        # 底图属性	
        res.tmXBMode = "Explicit"  # 按给定的间隔绘制X轴主刻度
        res.tmXBTickSpacingF = float(tmXBTickSpacingF)  # 主刻度间隔
        res.tmYLTickSpacingF = float(tmYLTickSpacingF)
        # 画坐标轴
        res.gsnMaximize = True  # 是否占满整个画布
        res.tmXBOn = True  # x轴的底部刻度线
        res.tmYLOn = True  # y轴的左边刻度线
        res.tmXBLabelFontHeightF = float(tmXBLabelFontHeightF)  # X轴标签字体大小
        res.tmXBMajorLengthF = float(tmXBMajorLengthF)  # 设置X轴刻度长度
        res.tmXBMajorThicknessF = float(tmXBMajorThicknessF)  # x轴刻度厚度
        res.tmYLLabelFontHeightF = float(tmYLLabelFontHeightF)  # Y轴左坐标轴刻度字体大小
        res.tmYLMajorLengthF = float(tmYLMajorLengthF)  # Y轴主刻度线长度
        res.tmYLMajorThicknessF = float(tmYLMajorThicknessF)
        # 坐标轴网格线
        res.tmXMajorGrid = tmXMajorGrid  # X轴显示网格线
        res.tmXMajorGridLineDashPattern = tmXMajorGridLineDashPattern  # 网格线为虚线
        res.tmXMajorGridThicknessF = tmXMajorGridThicknessF  # X轴主刻度网线粗细
        res.tmYMajorGrid = tmYMajorGrid  # Y轴显示网格线
        res.tmYMajorGridLineDashPattern = tmYMajorGridLineDashPattern  # 网格线为虚线
        res.tmYMajorGridThicknessF = tmYMajorGridThicknessF  # Y轴网线粗细
    else:
        res.gsnMaximize = False
        if (borderOn == "False"):
            # 去掉四周边框
            res.tmXBBorderOn = False
            res.tmXTBorderOn = False
            res.tmYLBorderOn = False
            res.tmYRBorderOn = False

    if (lambertOn == "True"):
        del res.mpCenterLonF  # 通过mpLambertMeridianF进行设置
        res.gsnDraw = False  # 关掉gsn绘图
        res.gsnFrame = False  # 关掉gsn绘图框架
        res.gsnAddCyclic = False

        # 底图属性
        res.mpFillOn = False
        res.mpGridAndLimbOn = False
        res.mpPerimOn = False  # 是否绘制地图边线
        res.mpOutlineDrawOrder = "PreDraw"  # 在标准绘制前绘制边线
        res.mpProjection = "LambertConformal"  # "LambertEqualArea" 定义投影
        res.mpLambertMeridianF = 105.0  # 中央子午线，中心经度
        res.mpLimitMode = "LatLon"  # 按给定经纬度范围绘制
        res.mpLambertParallel1F = 25  # Default: .001 第一标准纬度
        res.mpLambertParallel2F = 47  # Default: 89.999 第二标准纬度
        res.mpGridLineDashPattern = 5  # 绘制经纬度网格的虚线线型
        res.mpGridLineThicknessF = 0.5  # 绘制经纬度网格的虚线线宽
        res.mpNationalLineColor = "transparent"  # 国界颜色
        res.mpGeophysicalLineColor = "transparent"  # 其他边线线颜色
        res.mpUSStateLineColor = "transparent"  # 美国州界，中国省界
        res.gsnMaximize = False
        res.tiMainOn = False  # 是否显示主标题
        res.lbLabelBarOn = False  # 是否绘制色例
        if (area_name == "CH"):  # 若是绘制中国区域，则设置为固定经纬度范围
            res.mpMinLonF = 78.0
            res.mpMaxLonF = 130.0
            res.mpMinLatF = 15.0
            res.mpMaxLatF = 56.0

        if (business_id == "MRPS-MODES-JYGWMS-CH-Q001"
                or business_id == "MRPS-MODES-JYGWMS-CH-Q002"):
            del res.mpMinLonF
            del res.mpMaxLonF
            del res.mpMinLatF
            del res.mpMaxLatF
            
            res.mpLeftCornerLatF = minLat  # 左下角纬度
            res.mpRightCornerLatF = maxLat  # 右上角纬度
            res.mpLeftCornerLonF = minLon  # 左下角经度
            res.mpRightCornerLonF = maxLon  # 左下角经度
            res.mpLimitMode = "Corners"  # 采用Corners方式绘图，其余按照latlon方式绘图

        # 去掉四周边框
        res.tmXBBorderOn = False
        res.tmXTBorderOn = False
        res.tmYLBorderOn = False
        res.tmYRBorderOn = False
        # 去掉刻度
        res.tmXBOn = False
        res.tmXTOn = False
        res.tmYLOn = False
        res.tmYROn = False
        # 左上角坐标
        res.vpXF = 0  # 左上点离左边画布边缘的距离，设置为0时距离为0
        res.vpYF = 1  # 左上点离上边画布边缘的距离，设置为1时距离为0
        # 调节画布的长宽
        res.vpWidthF = 1.
        res.vpHeightF = 1.
        res.cnSmoothingOn = True  # 设置等值线平滑，三次样条平滑
        res.cnSmoothingDistanceF = 0.0001  # 平滑系数，值越接近0越平滑
    res.cnFillOn = cnFillOn
    if (cnFillOn == "True"):
        res.cnFillColors = colorTool.getColorOrder(color_cfg_file)
    res.cnLineLabelsOn = False  # 等值线标签默认关闭
    res.cnLinesOn = cnLinesOn  # 等值线是否显示

    if (cnLinesOn == "True"):  # 是否绘制等值线
        cnLineLabelsOn = IoUtil.readConfig_int(config_path, "cnLineLabelsOn_" + business_id)  # 打开等值线时，是否显示标签
        LineColor = IoUtil.readConfig_int(config_path, "LineColor_" + business_id)  # 等值线颜色
        cnLineThicknessF = float(IoUtil.readConfig_int(config_path, "LineThick_" + business_id))  # 设置等值线线宽
        cnLineLabelDensityF = float(IoUtil.readConfig_int(config_path, "CL_DENSITY_" + business_id))  # 标签间隔
        cnLineLabelFontHeightF = float(IoUtil.readConfig_int(config_path, "CL_LABEL_" + business_id))  # 标签数值字体大小
        cnSmoothingDistanceF = float(IoUtil.readConfig_int(config_path, "CS_DistanceF_" + business_id))  # 等值线平滑系数

        #res.cnLineLabelsOn	:= cnLineLabelsOn  # 等值线上的数字标签是否显示,此处待定！！！！！！！
        res.gsnContourNegLineDashPattern = 5  # 设置小于0的等值线线型，此处是5号虚线
        if (IoUtil.readConfig_int(config_path, "ZEROLINE_" + business_id) != ""):  # 0线特殊处理，此处为加粗
            res.gsnContourZeroLineThicknessF = float(IoUtil.readConfig_int(config_path, "ZEROLINE_" + business_id))

        if(cnLineLabelsOn == "True"):# 是否绘制等值线标签
            res.cnLineLabelBackgroundColor = "#FEFEFE"  # 标签底色为接  #若需要其他颜色或透明（-1）则另行配置
            res.cnLineLabelDensityF       = float( cnLineLabelDensityF)   	  # 标签间隔
            res.cnLineLabelInterval = 1  # 等值线标签间隔，设置1时，则每条线上都进行标签
            res.cnLineLabelFontHeightF = cnLineLabelFontHeightF  # 标签数值字体大小
            res.cnLineLabelFormat = ".1.4f"  # 标签显示为小数点后一位

        # res.cnLineColor = if(LineColor == "", "black", LineColor)  # 等值线颜色，此处待定个！！
        res.cnLabelMasking = True  # 等值线不穿过标签文字
        # res.cnSmoothingTensionF    	= 5			#使平滑的曲线不相交
        res.cnLineThicknessF = cnLineThicknessF  # 等值线线宽
        res.cnSmoothingOn = True  # 是否平滑
        res.cnSmoothingDistanceF = 0.0001
    mpLandFillColor = IoUtil.readConfig_int(config_path, "LandFillColor_" + business_id)  # 陆地颜色
    if (mpLandFillColor != ""):
        res.mpFillOn = True
        res.mpLandFillColor = mpLandFillColor  # 陆地颜色
    mpGeophysicalLineColor = IoUtil.readConfig_int(config_path, "mpGeoLineColor_" + business_id)
    mpOutlineBoundary = IoUtil.readConfig_int(config_path, "mpOutlineBoundary_" + business_id)  # 是否添加地理边界（国界）
    # res.mpGeophysicalLineColor = where(mpGeophysicalLineColor == "", "transparent",
    #                                    mpGeophysicalLineColor)  # 未设置颜色就默认透明
    res.mpUSStateLineColor = "transparent"
    if (res.mpGeophysicalLineColor != "transparent"):
        mpGeophysicalLineThicknessF = float(IoUtil.readConfig_int(config_path, "mpLineThicknessF_" + business_id))
        res.mpNationalLineThicknessF = 2.0
        res.mpGeophysicalLineThicknessF = mpGeophysicalLineThicknessF
        if (mpOutlineBoundary == ""):
            res.mpOutlineBoundarySets = "National"  # 添加国界线
        res.mpNationalLineColor = mpGeophysicalLineColor
    plot = Ngl.contour_map(workstation, drawData, res)
    # 特殊等值线
    specialLine = IoUtil.readConfig_int(config_path, "specialLine_" + business_id)  # 需要特殊处理的等值线值
    if (specialLine != ""):
        htres = Ngl.Resources()
        htres.gsnDraw = False
        htres.gsnFrame = False
        htres.gsnLeftString = ""  # 左上角不显示标签
        htres.gsnCenterString = ""  # 左上角不显示标签
        htres.gsnRightString = ""  # 右上角不显示标签
        htres.cnFillOn = False
        htres.cnLineLabelsOn = True
        htres.cnInfoLabelOn = False
        htres.cnLineColor = IoUtil.readConfig_int(config_path, "specialLineColor_" + business_id)  # 等值线颜色
        htres.cnLabelMasking = True  # 等值线不穿过文字
        htres.cnLinesOn = True  # 等值线数据是否显示
        htres.cnLineLabelBackgroundColor = "white"
        htres.cnLevelSelectionMode = "ExplicitLevels"  # set explicit contour levels
        htres.cnLevels = float(specialLine.split(","))
        htres.cnLineThicknessF = float(
            IoUtil.readConfig_int(config_path, "specialLineThickness_" + business_id))  # 等值线粗细
        htres.cnLineLabelFontHeightF = 0.008
        htres.cnSmoothingOn = True
        htres.cnSmoothingDistanceF = 0.001
        htres.cnLineLabelFormat = ".1.4f"
        line = Ngl.contour_map(workstation, drawData, htres)
        # overlay(plot, line)  todo

    if (markerOn == "True"):  # 打点，相关系数检验
        number = float(acc)
        # 打点
        mksres = True  # marker属性
        mksres.gsMarkerIndex = 16  # 空心圆点4,实心点16
        mksres.gsMarkerColor = "black"
        mksres.gsMarkerSizeF = 2.5
        size = np.shape(drawData)
        zlon = drawData.variable['lon']
        zlat = drawData.variable['lat']
        # 循环筛选出需要打点的经纬度
        for i in range(size[0]):
            for j in range(size[1]):
                if (not np.isnan(drawData[i, j]) and np.abs(drawData[i, j]) >= number):
                    if 'lats' not in locals().keys():
                        lats = zlat[i]
                        lons = zlon[j]
                    else:
                        lats = np.hstack(lats, zlat[i], 0)
                        lons = np.hstack(lons, zlon[j], 0)
        mark = Ngl.add_polymarker(workstation, plot, lons, lats, mksres)  # 点直接打在plot上的
    Ngl.draw(plot)
    Ngl.frame(workstation)
    Ngl.end()
    transparentBkColor("white -crop "+(imgSizes[0]+"x"+imgSizes[1]+"+"+imgSizes[2]+"+"+imgSizes[3]), outputPath + outputName + ".png")
    #调用imageMagic切图
    del drawData,plot,workstation,res,cmap
    return 0







def transparentBkColor(color, filename):
    cmd = "convert -transparent %s  %s  %s" % (color,filename ,filename)
    os.system(cmd)


def readParams(paramPath, paraIDInput):
    argu = Ngl.asciiread(paramPath,-1,"string")
    for i in range(0,len(argu)-1):
        if (0 == len(argu(i))):
            continue
        lineargu = argu(i).split("=")
        paraId = lineargu(0)
        if (paraIDInput == paraId):
            if(len(lineargu)==1):
                return ""
            return lineargu(1)
        del lineargu
    return ""