# replace_value = '2019年11月11日#20191106|20191205'
# raw_value ='起报时间:$|预报时间:$-$'

# for value in replace_value:
#     raw_value = raw_value.replace('$',value)
# print(raw_value)
from util import xmlUtils
def parse_and_integrate_params(input_data, params_xml_file):
    # 获取input_data
    # input_data = parse_input_data(input_data)
    # 获取xml分装的参数列表
    params_dict = xmlUtils.xml2dict(params_xml_file)
    second_params_dict = xmlUtils.xml2dict(params_dict['second_params_file_id'])  # 此处暂且以绝对路径的形式，
    # 入参重新拼接
    sub_title_list = []
    for key in params_dict.keys():
        if key in second_params_dict.keys():

            raw_value = second_params_dict[key] #预报时间:$-$
            for value in params_dict[key].split("|"):  # 20191106|20191205
                raw_value = raw_value.replace("$", value)

            if key.startswith('sub_title'):#副标题组装
                sub_title_list.append(raw_value)
                second_params_dict['sub_titles'] = sub_title_list
                # del second_params_dict[key],params_dict[key]
            else:
                second_params_dict[key] =raw_value#非副标题组装
    #更新到params_dict中去
    params_dict.update(second_params_dict)
    return input_data, params_dict

# input ='aaa'
# params_xml_file=r'E:\PythonWorkSpace\test\main\util\input_params.xml'
#
# input_data, params_dict = parse_and_integrate_params(input,params_xml_file)
# print(input_data)
# print(params_dict)

color_values = '255,255,255|0,0,0|255,0,0|0,0,255|0,69,107'
color_list = []
for color_str in color_values.split("|"):
    color_list.append([float(x)/255.0 for x in color_str.split(",")])
