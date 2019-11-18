label_bar_location_params_dict = {
    "whole_china_am" :{
        "amJust" :"BottomLeft",
        "amParallelPosF" :-0.489247,
        "amOrthogonalPosF" : 0.4856322
    }
}

def get_whole_china_common_config():
    whole_china_common_config = {}
    for var_name in label_bar_location_params_dict.keys():
        if var_name.startswith('whole_china_'):
            whole_china_common_config.update(label_bar_location_params_dict[var_name])
    return whole_china_common_config