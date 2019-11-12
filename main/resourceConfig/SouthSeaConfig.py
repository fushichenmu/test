southsea_params_dict = {
    'southsea_cn': {
        'cnLevelSelectionMode': 'ExplicitLevels'
        , 'cnInfoLabelOn': False
        , 'cnFillOn': True
        , 'cnFillDrawOrder': 'PreDraw'
        , 'cnLinesOn': False
        , 'cnLevelSpacingF': 20.0
        , 'cnLineLabelsOn': False
    },

    'southsea_gsn': {
        'gsnMaximize': False
        , 'gsnDraw': False  # 关掉gsn绘图
        , 'gsnFrame': False  # 关掉gsn绘图框架
        , 'gsnAddCyclic': False  # 不是全球地图，
        , 'gsnRightString': ""  # 绘图的上边界上方添加给定的字符串，并对其右对齐
        , 'gsnLeftString': ""  # 绘图的上边界上方添加给定的字符串，并对其左对齐
        , "gsnCenterString": ""
    },

    'southsea_lb': {
        'lbLabelBarOn': False
    },

    'southsea_mp': {
        'mpProjection': 'LambertConformal'
        , 'mpGridAndLimbOn': False
        , 'mpLambertMeridianF': 105.0
        , 'mpLimitMode': 'Corners '
        , 'mpLambertParallel1F': 25
        , 'mpLambertParallel2F': 48
        , 'mpPerimOn': True
        , 'mpPerimLineThicknessF': 1
        , 'mpGridLineDashPattern': 5
        , 'mpGridLineThicknessF': 0.5
        , "mpLeftCornerLatF": 2.8
        , "mpRightCornerLatF": 23.3
        , "mpLeftCornerLonF": 106.7
        , "mpRightCornerLonF": 126.6
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
    },

    'southsea_pm': {
        'pmTickMarkDisplayMode': 'Always'
    },

    'southsea_tm': {
        'tmXBOn': False
        , 'tmXTOn': False
        , 'tmYLOn': False
        , 'tmYROn': False
    },

    'southsea_vp': {
        'vpXF': 0.
        , 'vpYF': 1.
        , "vpWidthF": 0.18
        , "vpHeightF": 0.18
    }

    # 'special_gg':{
        # "gsnMaximize" : False
        # ,"vpHeightF": 0.18
        # ,"vpWidthF": 0.18
        # ,"mpLeftCornerLatF": 2.8
        # ,"mpRightCornerLatF": 23.3
        # ,"mpLeftCornerLonF": 106.7
        # ,"mpRightCornerLonF": 126.6
        # ,"tmXBOn": False
        # ,"tmXTOn": False
        # ,"tmYLOn": False
        # ,"tmYROn": False
        # ,"lbLabelBarOn": False
        # ,"gsnLeftString": ""
        # ,"gsnRightString": ""
        # ,"gsnCenterString": ""
    # }
}

def get_south_sea_common_config(prefix="south_sea"):
    whole_china_common_config = {}
    for var_name in southsea_params_dict.keys():
        if var_name.startswith(prefix):
            whole_china_common_config.update(southsea_params_dict[var_name])
    return whole_china_common_config