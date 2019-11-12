scale_params_dict = {
    "whole_china_tx" :{
        "txFontHeightF" :0.012097,
        "txFontColor" : "black"
    }


}


def get_whole_china_common_config():
    whole_china_common_config = {}
    for var_name in scale_params_dict.keys():
        if var_name.startswith('whole_china_'):
            whole_china_common_config.update(scale_params_dict[var_name])
    return whole_china_common_config
