from util import xmlUtils
import Nio

import numpy as np


def execute(input_data, params_xml_file):
    # 参数校验
    valid_message = validation_params(input_data, params_xml_file)
    if valid_message['isSuccess']:
        #解析并整合参数
        input_data, params_dict = parse_and_integrate_params(input_data, params_xml_file)

        if params_dict["region_type"] == "wholeChina":
            from drawService.chinaService.wholeChinaService import WholeChinaService
            common_business_service = WholeChinaService(input_data, params_dict)
        nboxes = common_business_service.draw()
        return nboxes
    else:
        return valid_message




def validation_params(input_data, params_xml_file):
    valid_message = {"isSuccess": True}
    if not input_data:
        print("入参错误，缺少input_data!")  # 此处以后引入日志
        valid_message["isSuccess"] = False
        valid_message["error_message"] = "入参错误，缺少input_data!"
        return valid_message
    if not params_xml_file:
        print("入参错误，缺少params_xml_file!")
        valid_message["isSuccess"] = False
        valid_message["error_message"] = "入参错误，缺少params_xml_file!"
        return valid_message
    return valid_message


# 解析input_data参数
def parse_input_data(input_data):
    switchDict = {
        "str": input_data_str,
        "ndarray": input_data_object
    }
    return switchDict.get(type(input_data))(input_data)


def input_data_str(input_data):
    parsed_data = Nio.open_file(input_data, "r")
    return parsed_data


def input_data_object(input_data):
    return input_data


def parse_and_integrate_params(input_data, params_xml_file):
    # 获取input_data
    # input_data = parse_input_data(input_data)
    # 获取xml分装的参数列表
    first_params_dict = xmlUtils.xml2dict(params_xml_file)
    second_params_dict = xmlUtils.xml2dict(first_params_dict['business_id'])  # 此处暂且以绝对路径的形式，
    # 入参重新拼接
    sub_title_list = []
    for key in first_params_dict.keys():
        if key in second_params_dict.keys():

            raw_value = second_params_dict[key] #预报时间:$-$
            for value in first_params_dict[key].split("|"):  # 20191106|20191205
                raw_value = raw_value.replace("$", value)

            if key.startswith('sub_title'):#副标题组装
                sub_title_list.append(raw_value)
                second_params_dict['sub_titles'] = sub_title_list
                # del second_params_dict[key],first_params_dict[key]
            else:
                second_params_dict[key] =raw_value#非副标题组装

    #更新到params_dict中去
    first_params_dict.update(second_params_dict)

    for key in first_params_dict:
        if not key.startswith('color'):
            continue
        else:
            color_values = first_params_dict[key].split('|')
            if key =='color_lables':
                first_params_dict[key]=color_values
            else:
                color_list = []
                for color_str in color_values.split("|"):
                    color_list.append([float(x) / 255.0 for x in color_str.split(",")])
                first_params_dict[key] = color_list
    return input_data, first_params_dict
