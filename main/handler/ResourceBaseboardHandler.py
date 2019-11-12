from handler import ResourceCommonHandler
from resourceConfig import BaseboardConfig as bbc
from util.ResourcesUtils import create_or_update_resource
from util import colorTool
import Ngl


class ResourceBaseboardHandler(ResourceCommonHandler):

    def __init__(self, workstation,input_data,use_default_setting,color_cfg_file):
        ResourceCommonHandler.__init__(self,workstation,input_data,use_default_setting)
        self.color_cfg_file = color_cfg_file

    def contour_map(self):
        resource_config = {}
        # 是否使用默认配置
        if self.use_dafault_setting:
            resource_config = bbc.get_whole_china_common_config()

        # 是否有色板配置文件
        if self.color_cfg_file:
            cnLevels = colorTool.getColorValueDef(self.color_cfg_file)
            cn_params_dict = {
                "cnLevels": cnLevels
                , "cnFillColors": colorTool.getColorOrder(self.color_cfg_file)
            }
            resource_config.update(cn_params_dict)

        # 是否有用户自定义配置
        if self.params_dict:
            resource_config.update(self.params_dict)

        # 构造resource对象
        self.resource = create_or_update_resource(params_dict=resource_config)

        # 绘图
        map_plot = Ngl.contour_map(self.workstation, self.input_data, self.resource)

        return map_plot
