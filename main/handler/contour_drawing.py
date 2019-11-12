import Ngl
from thirdTime.util import colorTool


def draw_contour(colorBarName, data, endLat, endLon, imgOutputPaths, lat, lon, startLat, startLon, wks):
    res = Ngl.Resources()
    res.nglFrame = False
    res.nglDraw = False

    resource_map_setting(endLat, endLon, lon, res, startLat, startLon)

    resource_Axises_setting(imgOutputPaths, res)

    resource_cn_setting(colorBarName, res)
    # 其他相关配置
    resource_other_setting(lat, lon, res)
    # 绘等高线图
    plot = Ngl.contour_map(wks, data, res)

    return plot


def resource_other_setting(lat, lon, res):
    res.lbOrientation = "horizontal"
    res.lbLabelPosition = "Bottom"
    res.lbLabelFontHeightF = 0.012097
    res.lbLabelBarOn = True  # 显示色标
    res.pmLabelBarWidthF = 0.7  # 色标变窄
    res.pmLabelBarHeightF = 0.08  # 色标变细
    res.pmLabelBarOrthogonalPosF = 0.06
    res.vpXF = 0.085021
    res.vpYF = 0.892473
    res.vpWidthF = 0.866043  # Change the aspect ratio, but
    res.vpHeightF = 0.406451  # make plot as large as possible.
    res.tiMainOn = False  # 不显示主标题
    res.sfXArray = lon
    res.sfYArray = lat


def resource_cn_setting(colorBarName, res):
    # cn系列配置
    res.cnFillOn = True
    res.cnLinesOn = False  # 去除等值线
    res.cnLineLabelsOn = False  # 不显示数值
    res.cnLevels = colorTool.getColorValueDef(colorBarName)
    res.cnFillColors = colorTool.getColorOrder(colorBarName)
    res.cnLevelSelectionMode = "ExplicitLevels"
    res.cnSmoothingOn = False  # 是否平滑
    res.cnSmoothingDistanceF = 0.1
    res.cnNoDataLabelOn = False
    res.cnConstFLabelOn = False
    res.cnInfoLabelOn = False  # 不画等值线信息标签


def resource_Axises_setting(imgOutputPaths, res):
    ## if有组合条件是，建议采用如下方式，同时python3建议用括号包括整个条件
    if (imgOutputPaths.find("/TC_ACE/") != -1
            or imgOutputPaths.find("/TC_NUM/") != -1):
        res.tmXBTickSpacingF = 20  # 主刻度间隔
        res.tmYLTickSpacingF = 10  # 主刻度间隔
    res.tmYLLabelFontHeightF = 0.012097  # Y轴左坐标轴刻度字体大小
    res.tmYLMinorOn = True  # 打开副刻度
    res.tmYLMajorLengthF = 0.009  # Y轴主刻度线长度
    res.tmYLMajorThicknessF = 3
    res.tmXBLabelDeltaF = -0.7
    res.tmYLLabelDeltaF = -0.7


def resource_map_setting(endLat, endLon, lon, res, startLat, startLon):
    # map系列配置
    res.mpOutlineOn = True
    res.mpLimitMode = "LatLon"
    res.mpMinLonF = startLon  ## 为什么这里不是min(lon)
    res.mpMaxLonF = max(lon)
    res.mpMinLatF = startLat  ## 为什么这里不是min(lat)
    res.mpMaxLatF = endLat  ## 为什么这里不是max(lat)
    res.mpCenterLonF = (startLon + endLon) / 2.
    res.mpShapeMode = "FreeAspect"
    res.mpGridAndLimbOn = False
    res.mpLandFillColor = [255.0 / 255, 255.0 / 255, 254.0 / 255]
    res.mpFillOn = True
    res.mpGeophysicalLineColor = "transparent"
    # tm系列配置
    res.tmXBOn = True  # 显示横/下坐标刻度
    res.tmYLOn = True  # 显示纵/左坐标刻度
    res.tmXTOn = False  # 显示横/上坐标刻度
    res.tmYROn = False  # 显示纵/右坐标刻度
    res.tmBorderThicknessF = 2.0  # 坐标轴线宽度
    res.tmXBLabelFontHeightF = 0.012097  # X轴标签字体大小
    res.tmXMajorGridLineDashPattern = 2
    res.tmXMajorGridThicknessF = .8  # X轴主刻度网线粗细
    res.tmXBMinorOn = True  # 打开副刻度
    res.tmXBMajorLengthF = 0.009  # 设置X轴底部主要刻度长度
    res.tmXBMajorThicknessF = 3  # 设置X轴底部主要刻度kuan度
    res.tmXBTickSpacingF = 60  # 主刻度间隔
    res.tmYLTickSpacingF = 30  # 主刻度间隔