baseboard_params_dict = {
    'china_baseboard': {
        'cnLevelSelectionMode': 'ExplicitLevels'
        , 'cnInfoLabelOn': False
        , 'cnFillOn': True
        , 'cnFillDrawOrder': 'PreDraw'
        , 'cnLinesOn': False
        , 'cnLevelSpacingF': 20.0
        , 'cnLineLabelsOn': False

        , 'gsnMaximize': False
        , 'gsnDraw': False  # 关掉gsn绘图
        , 'gsnFrame': False  # 关掉gsn绘图框架
        , 'gsnAddCyclic': False  # 不是全球地图，
        , 'gsnRightString': ' '  # 绘图的上边界上方添加给定的字符串，并对其右对齐
        , 'gsnLeftString': ' '  # 绘图的上边界上方添加给定的字符串，并对其左对齐

        ,'lbLabelBarOn': False

        , 'mpProjection': 'LambertConformal'
        , 'mpGridAndLimbOn': False
        , 'mpLambertMeridianF': 105.0
        , 'mpLimitMode': 'Corners '
        , 'mpLambertParallel1F': 25
        , 'mpLambertParallel2F': 48
        , 'mpPerimOn': True
        , 'mpPerimLineThicknessF': 1
        , 'mpGridLineDashPattern': 5
        , 'mpGridLineThicknessF': 0.5
        , 'mpLeftCornerLatF': 13.2578
        , 'mpRightCornerLatF': 50.6752
        , 'mpLeftCornerLonF': 78.9951
        , 'mpRightCornerLonF': 148.8066
        , 'mpFillOn': True
        , 'mpDataSetName': '/nfsshare/cdbdata/algorithm/conductor/WMFS/EXTPRE/ysq/basedata/Earth..4'
        , 'mpDataBaseVersion': 'MediumRes'
        , 'mpAreaMaskingOn': True
        , 'mpMaskAreaSpecifiers': ['China']
        , 'mpMaskOutlineSpecifiers': ['China']
        , 'mpLandFillColor': 'white'
        , 'mpInlandWaterFillColor': 'white'
        , 'mpOceanFillColor': 'white'
        , 'mpOutlineBoundarySets': 'NoBoundaries'
        , 'mpNationalLineColor': 'white'
        , 'mpGeophysicalLineColor': 'white'
        , 'mpNationalLineThicknessF': 0.0

        , 'pmTickMarkDisplayMode': 'Always'

        , 'tmXBOn': False
        , 'tmXTOn': False
        , 'tmYLOn': False
        , 'tmYROn': False

        ,'vpXF': 0.
        , 'vpYF': 1.
        , 'vpWidthF': 1.
        , 'vpHeightF': 1.
    },


}



def get_china_common_config():
    china_common_config = {}
    for var_name in baseboard_params_dict.keys():
        if var_name.startswith('china_'):
            china_common_config.update(baseboard_params_dict[var_name])
    return china_common_config

# ddd = get_china_common_config()
# print(ddd)