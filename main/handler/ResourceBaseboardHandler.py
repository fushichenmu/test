from handler import ResourceCommonHandler
from resourceConfig import BaseboardConfig as bbc
from util.ResourcesUtils import create_or_update_resource
from util import colorTool
import Ngl
import numpy as np

class ResourceBaseboardHandler(ResourceCommonHandler):

    def __init__(self, workstation,input_data,param_dict,color_levels):
        ResourceCommonHandler.__init__(self,workstation,input_data)
        self.param_dict =param_dict
        self.color_levels =color_levels

    def contour_map(self):
        resource_config = {}

        # 是否有色板配置文件
        if self.color_levels:
            cn_params_dict = {
                "cnLevels": self.color_levels
                , "cnFillColors":np.arange(0,len(self.color_levels),1).tolist()
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
