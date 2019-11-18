label_bar_params_dict = {
    "china_label_bar_lb":{
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

        "vpWidthF":0.11
    },

    "china_label_bar_vp" :{


    }

}


def get_china_label_bar_common_config():
    china_label_bar_common_config = {}
    for var_name in label_bar_params_dict.keys():
        if var_name.startswith('china_label_bar_'):
            china_label_bar_common_config.update(label_bar_params_dict[var_name])
    return china_label_bar_common_config