ployline_params_dict = {


    #["nh/BOUL_G.shp","BOUL_S.shp","nh/BOUL_S2.shp","nh/HAX.shp","nh/HFCP.shp"]

    # 国界
    "BOUL_G": {
        "gsLineThicknessF": 1.0,
        "gsLineColor": "black",
        "gs_line_dash_pattern": 0
    },

    # 省界
    "BOUL_S": {
        "gsLineThicknessF": 1.0,
        "gsLineColor": "black",
        "gs_line_dash_pattern": 0
    },

    # 香港特别行政区边界
    "BOUL_S2": {
        'source':'xxx',
        'type':'point/polyline/polygon',
        "gsLineThicknessF": 1.0,
        "gsLineColor": "black",
        "gs_line_dash_pattern": 2
    },

    # 海岸线
    "HAX": {
        "gsLineThicknessF": 1.0,
        "gsLineColor": "blue",
        "gs_line_dash_pattern": 0
    },

    # 南海诸岛
    "HFCP": {
        "gsLineThicknessF": 1.0,
        "gsLineColor": (0.0/255,0.0/255,153.0/255),
        "gs_line_dash_pattern": 0
    },
    #南海九段线
    "JDX": {
        "gsLineThicknessF": 2.0,
        "gsLineColor": 'black',
        "gs_line_dash_pattern": 0
    }

    #省会点位（非必须）

}

def get_china_shape_common_config(prefix="china_shape_",file_name=''):
    china_shape_common_config = {}
    for var_name in ployline_params_dict.keys():
        if var_name.startswith(prefix+file_name):
            china_shape_common_config.update(ployline_params_dict[var_name])
    return china_shape_common_config

