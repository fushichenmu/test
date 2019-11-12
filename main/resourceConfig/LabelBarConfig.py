label_bar_params_dict = {
    "whole_china_lb":{
        "lbAutoManage":False,
        "lbLabelAlignment":"BoxCenters",
        "lbTitleString":"fads",
        "lbTitleFontHeightF":0.035,
        "lbTitleFontColor":"white",
        "lbPerimOn":True,
        "lbPerimColor":"black",
        "lbPerimThicknessF":2,
        "lbJustification" :"CenterLeft",

        "lbBoxMajorExtentF":0.8,
        "lbMonoFillPattern":True,
        "lbLabelJust":"CenterLeft",
    },

    "whole_china_vp" :{
        "vpWidthF":0.11

    }

}


def get_whole_china_common_config():
    whole_china_common_config = {}
    for var_name in label_bar_params_dict.keys():
        if var_name.startswith('whole_china_'):
            whole_china_common_config.update(label_bar_params_dict[var_name])
    return whole_china_common_config