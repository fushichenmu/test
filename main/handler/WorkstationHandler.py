# import Ngl
from util.ResourcesUtils import create_or_update_resource
from util import colorTool
import os
class WorkstationHandler:
    def __init__(self
                 , output_img_type=''  #最终输出图片格式 例:png
                 , output_img_path=''  #最终输出图片位置，例:/usr/local/example
                 , color_levels=''   #色板配置文件
                 , wK_res_params={}  #workstation的Resource相关配置参数
                 , plot=None):

        self.__wk_res = create_or_update_resource(None, wK_res_params)
        # 判断文件路径是否存在，如果不存在，则创建，此处是创建多级目录
        if not os.path.isdir(output_img_path):
            os.makedirs(output_img_path)
        self.__wk = Ngl.open_wks(output_img_type, output_img_path, self.__wk_res)
        # workstation配置颜色
        # cmap = colorTool.getColorMap(color_cfg_file)
        Ngl.define_colormap(self.__wk, color_levels)
        self.plot = plot

    def _get_wk_res(self):
        return self.__wk_res

    def _set_wk_res(self, res):
        self.__wk_res = res

    def _get_wk(self):
        return self.__wk

    def _set_wk(self,wk):
        self.__wk = wk

    def _set_wk_color(self,color_cfg_file):
        '''
        用于修改workstation配置颜色！！！
        @param color_cfg_file:
        @return:
        '''
        cmap = colorTool.getColorMap(color_cfg_file)
        Ngl.define_colormap(self.__wk_res, cmap)

    def close_workstation(self):
        # 9.Ngl绘图结束
        Ngl.draw(self.plot)
        Ngl.frame(self.workstation)
        Ngl.end()

# wk_res_params = {
#     "name": "18D_Block",
#     "xcc": {
#         "component": {
#             "core": [],
#             "platform": []
#         },
#     },
#     "uefi": {
#         "component": {
#             "core": [],
#             "platform": []
#         },
#     }
# }
# wk = WorkstationHandler(wK_res_params=wk_res_params)
