import  numpy as np

# 南海相关
dict_aa = {

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
    }
    # # 比例尺
    # 'south_sea_scale': {
    #     "txFontHeightF": 0.008
    #     , "txFontColor": "black"
    # },
    # # 小地图位置
    # 'south_sea_location': {
    #     "amParallelPosF": 0.489247
    #     , "amOrthogonalPosF": 0.4856322
    #     , "amJust": "BottomRight"
    # }

shape_file_path='/usr/local/'
for key, shape_params_dict in dict_aa.items():
    file_name = shape_params_dict.pop('file_name')
    type = shape_params_dict.pop('type')

    # shape = Nio.open_file(shape_file_path + file_name, "r")
    # lon = np.ravel(shape.variables["x"][:])
    # lat = np.ravel(shape.variables["y"][:])
    # params_dict['gsSegments'] = shape.variables["segments"][:, 0]
    # resource = create_or_update_resource(params_dict=params_dict)
    # # 2.绘制曲线图
    # if type == 'polyline':
    #     Ngl.add_polyline(self.workstation, self.plot, lon, lat, resource)