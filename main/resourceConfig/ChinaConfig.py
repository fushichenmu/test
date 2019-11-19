china_params_dict = {

    # 底板
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

        , 'lbLabelBarOn': False

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

        , 'vpXF': 0.
        , 'vpYF': 1.
        , 'vpWidthF': 1.
        , 'vpHeightF': 1.
    },
    # 主体地理线
    'china_geoline': {
        # file_names = ["HYDL.shp", "BOUL_S.shp", "HAX.shp", "nh/HFCP.shp",
        #               "BOUL_S2.shp", "BOUL_GY.shp", "BOUL_GW.shp"]

        # river
        "river": {
            "file_name": "HYDL.shp",
            "type": "polyline",
            "gsLineThicknessF": 1.0,
            "gsLineColor": "blue",
            "gs_line_dash_pattern": 0
        },
        # province
        "province": {
            "file_name": "BOUL_S.shp",
            "type": "polyline",
            "gsLineThicknessF": 1.0,
            "gsLineColor": "black",
            "gs_line_dash_pattern": 0
        },
        # coastline
        "coastline": {
            "file_name": "HAX.shp",
            "type": "polyline",
            "gsLineThicknessF": 1.0,
            "gsLineColor": (0.0, 0.0, 153.0 / 255),
            "gs_line_dash_pattern": 0
        },
        # south_sea
        "south_sea": {
            "file_name": "nh/HFCP.shp",
            "type": "polyline",
            "gsLineThicknessF": 1.0,
            "gsLineColor": (0.0, 0.0, 153.0 / 255),
            "gs_line_dash_pattern": 0
        },
        # HongKong
        "HongKong": {
            "file_name": "BOUL_S2.shp",
            "type": "polyline",
            "gsLineThicknessF": 2.0,
            "gsLineColor": "black",
            "gs_line_dash_pattern": 2
        },
        # Established_boundaries
        "established_boundaries": {
            "file_name": "BOUL_GY.shp",
            "type": "polyline",
            "gsLineThicknessF": 2.0,
            "gsLineColor": "black",
            "gs_line_dash_pattern": 0
        },
        # Unestablished boundaries
        "unestablished_boundaries": {
            "file_name": "BOUL_GW.shp",
            "type": "polyline",
            "gsLineThicknessF": 2.0,
            "gsLineColor": "black",
            "gs_line_dash_pattern": 1
        },
    },
    # 图例
    "china_labelbar": {
        "lbAutoManage": False,
        "lbLabelAlignment": "BoxCenters",
        "lbTitleString": "fads",
        "lbTitleFontHeightF": 0.035,
        "lbTitleFontColor": "white",
        "lbPerimOn": True,
        "lbPerimColor": "black",
        "lbPerimThicknessF": 2,
        "lbJustification": "CenterLeft",

        "lbBoxMajorExtentF": 0.8,
        "lbMonoFillPattern": True,
        "lbLabelJust": "CenterLeft",

        "vpWidthF": 0.11
    },

    # 图例位置
    "china_labelbar_location": {
        "amJust": "BottomLeft",
        "amParallelPosF": -0.489247,
        "amOrthogonalPosF": 0.4856322
    },

    # 比例尺
    "china_scale": {
        "scala_figure": "Scale 1:20 000 000",
        "location": "95x17",
        "txFontHeightF": 0.012097,
        "txFontColor": "black"
    },
    # 南海相关
    "china_south_sea": {
        # 底板
        'south_sea_baseboard': {
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
            , 'gsnRightString': ""  # 绘图的上边界上方添加给定的字符串，并对其右对齐
            , 'gsnLeftString': ""  # 绘图的上边界上方添加给定的字符串，并对其左对齐
            , "gsnCenterString": ""

            , 'lbLabelBarOn': False

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

            , 'pmTickMarkDisplayMode': 'Always'

            , 'tmXBOn': False
            , 'tmXTOn': False
            , 'tmYLOn': False
            , 'tmYROn': False

            , 'vpXF': 0.
            , 'vpYF': 1.
            , "vpWidthF": 0.18
            , "vpHeightF": 0.18
        },
        # 地理线
        'south_sea_geoline': {

            # file_names = ["nh/BOUL_G.shp", "BOUL_S.shp", "nh/BOUL_S2.shp", "nh/HAX.shp",
            #               "nh/HFCP.shp"]  # nh/BOUL_JDX.shp 九段线已经在已定国界中包含

            # 国界
            "BOUL_G": {
                "file_name": "nh/BOUL_G.shp",
                "type": "polyline",
                "gsLineThicknessF": 1.0,
                "gsLineColor": "black",
                "gs_line_dash_pattern": 0
            },

            # 省界
            "BOUL_S": {
                "file_name": "BOUL_S.shp",
                "type": "polyline",
                "gsLineThicknessF": 1.0,
                "gsLineColor": "black",
                "gs_line_dash_pattern": 0
            },

            # 香港特别行政区边界
            "BOUL_S2": {
                "file_name": "nh/BOUL_S2.shp",
                "type": "polyline",
                "gsLineThicknessF": 1.0,
                "gsLineColor": "black",
                "gs_line_dash_pattern": 2
            },

            # 海岸线
            "HAX": {
                "file_name": "nh/HAX.shp",
                "type": "polyline",
                "gsLineThicknessF": 1.0,
                "gsLineColor": "blue",
                "gs_line_dash_pattern": 0
            },

            # 南海诸岛
            "HFCP": {
                "file_name": "nh/HFCP.shp",
                "type": "polyline",
                "gsLineThicknessF": 1.0,
                "gsLineColor": (0.0 / 255, 0.0 / 255, 153.0 / 255),
                "gs_line_dash_pattern": 0
            },
            # 南海九段线
            # "JDX": {
            #     "file_name": "",
            #     "type": "polyline",
            #     "gsLineThicknessF": 2.0,
            #     "gsLineColor": 'black',
            #     "gs_line_dash_pattern": 0
            # }

            # 省会点位（非必须）
        },
        # 比例尺
        'south_sea_scale': {
            "scala_figure": "1:40 000 000"
            , "location": "118x3"
            , "txFontHeightF": 0.008
            , "txFontColor": "black"
        },
        # 小地图位置
        'south_sea_location': {
            "amParallelPosF": 0.489247
            , "amOrthogonalPosF": 0.4856322
            , "amJust": "BottomRight"
        }
    },

    # logo 和 标题
    "logo_and_titles": {
        "font_file_path": "/home/nriet/PycharmProjects/test-master/main/fontFiles/MSYH.TTC"  # 微软雅黑
        , "font_main_size": 20  # 主标题20px
        , "font_sub_size": 15  # 副标题15px
        , "top_padding": 40  # 上边距40px
        , "title_padding": 5  # 标题间隔5px
    }

}
