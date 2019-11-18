from handler import ResourceCommonHandler
from resourceConfig import LebelBarConfig as lbc
from resourceConfig import LegendLocationConfig as lblc
from util.ResourcesUtils import create_or_update_resource
from util import colorTool
import numpy as np
import Ngl

class ResourceLabelBarHandler(ResourceCommonHandler):
    def __init__(self,workstation,plot,color_cfg_file,use_default_setting = True,output_img_name=''):
        ResourceCommonHandler.__init__(self,workstation=workstation,use_default_setting=use_default_setting)
        self.plot =plot
        self.color_cfg_file=color_cfg_file
        self.output_img_name = output_img_name


    def contour_map(self):
        params_dict = {}
        #1.读取wholechina常用配置
        if self.use_default_setting:
            params_dict = lbc.get_whole_china_common_config()

        #2.读取色标取值数据
        cn_fill_colors = colorTool.getColorOrder(self.color_cfg_file)

        cn_levels = colorTool.getColorValueDef(self.color_cfg_file)
        nboxes = np.shape(cn_fill_colors)[0]
        labels = [""] * nboxes

        #3.图例解释数据
        if (self.output_img_name.contains("RH") or self.output_img_name.contains("TK")):
            labels[0] = "NoData"
            labels[1] = "<" + str(cn_levels[1])
            labels[nboxes - 1] = ">" + str(cn_levels[nboxes - 2])
            for i in range(2, nboxes - 1):
                labels[i] = str(cn_levels[i - 1]) + "~" + str(cn_levels[i])
        else:
            labels[0] = "<" + str(cn_levels[0])
            labels[nboxes - 1] = ">" + str(cn_levels[nboxes - 2])
            for i in range(1, nboxes - 1):
                labels[i] = str(cn_levels[i - 1]) + "~" + str(cn_levels[i])

        #4.其他配置
        params_dict['vpHeightF'] = 0.022 * 0.868 * (nboxes + 3 - (nboxes - 5) / 2.8)
        params_dict['lbFillColors'] = cn_fill_colors
        if (self.output_img_name.contains("TK")):
            params_dict["lbLabelFontHeightF"] = 0.009
        else:
            params_dict["lbLabelFontHeightF"] = 0.009677
        lbres = create_or_update_resource(params_dict=params_dict)
        lbid = Ngl.labelbar_ndc(self.workstation, nboxes, labels, 0, 0, lbres)

        #5.色标位置配置
        if self.use_default_setting:
            params_dict = lblc.get_whole_china_common_config()
        lblres = create_or_update_resource(params_dict=params_dict)

        Ngl.add_annotation(self.plot, lbid, lblres)