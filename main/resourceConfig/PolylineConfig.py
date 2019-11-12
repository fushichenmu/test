ployline_params_dict = {
    # river
    "whole_china_HYDL": {
        "gsLineThicknessF": 1.0,
        "gsLineColor": "blue",
        "gs_line_dash_pattern": 0
    },
    # province
    "whole_china_BOUL_S": {
        "gsLineThicknessF": 1.0,
        "gsLineColor": "black",
        "gs_line_dash_pattern": 0
    },
    # coastline
    "whole_china_HAX": {
        "gsLineThicknessF": 1.0,
        "gsLineColor": (0.0, 0.0, 153.0 / 255),
        "gs_line_dash_pattern": 0
    },
    # south_sea
    "whole_china_HFCP": {
        "gsLineThicknessF": 1.0,
        "gsLineColor": (0.0, 0.0, 153.0 / 255),
        "gs_line_dash_pattern": 0
    },
    # Hong Kong
    "whole_china_BOUL_S2": {
        "gsLineThicknessF": 2.0,
        "gsLineColor": "black",
        "gs_line_dash_pattern": 2
    },
    # Established boundaries
    "whole_china_BOUL_GY": {
        "gsLineThicknessF": 2.0,
        "gsLineColor": "black",
        "gs_line_dash_pattern": 0
    },
    # Unestablished boundaries
    "whole_china_BOUL_GW": {
        "gsLineThicknessF": 2.0,
        "gsLineColor": "black",
        "gs_line_dash_pattern": 1
    },

    #["nh/BOUL_G.shp","BOUL_S.shp","nh/BOUL_S2.shp","nh/HAX.shp","nh/HFCP.shp"]

    # 国界
    "south_sea_BOUL_G": {
        "gsLineThicknessF": 1.0,
        "gsLineColor": "black",
        "gs_line_dash_pattern": 0
    },

    # 省界
    "south_sea_BOUL_S": {
        "gsLineThicknessF": 1.0,
        "gsLineColor": "black",
        "gs_line_dash_pattern": 0
    },

    # 香港特别行政区边界
    "south_sea_BOUL_S2": {
        "gsLineThicknessF": 1.0,
        "gsLineColor": "black",
        "gs_line_dash_pattern": 2
    },

    # 海岸线
    "south_sea_HAX": {
        "gsLineThicknessF": 1.0,
        "gsLineColor": "blue",
        "gs_line_dash_pattern": 0
    },

    # 南海诸岛
    "south_sea_HFCP": {
        "gsLineThicknessF": 1.0,
        "gsLineColor": (0.0/255,0.0/255,153.0/255),
        "gs_line_dash_pattern": 0
    },
    #南海九段线
    "south_sea_JDX": {
        "gsLineThicknessF": 2.0,
        "gsLineColor": 'black',
        "gs_line_dash_pattern": 0
    }

    #省会点位（非必须）

}

def get_whole_china_common_config(prefix="whole_china_",file_name=''):
    whole_china_common_config = {}
    for var_name in ployline_params_dict.keys():
        if var_name.startswith(prefix+file_name):
            whole_china_common_config.update(ployline_params_dict[var_name])
    return whole_china_common_config

