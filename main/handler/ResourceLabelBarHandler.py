from handler import ResourceCommonHandler
from resourceConfig import LebelBarConfig as lbc
from resourceConfig import LegendLocationConfig as lblc
from util.ResourcesUtils import create_or_update_resource
from util import colorTool
import numpy as np
import Ngl

class ResourceLabelBarHandler(ResourceCommonHandler):
    def __init__(self,workstation,plot,output_img_name='',params_dict={},
                 ,location_params_dict = {},color_levels=[],color_lables=''):
        ResourceCommonHandler.__init__(self,workstation=workstation,plot=plot)
        self.output_img_name = output_img_name
        self.params_dict = params_dict
        self.color_levels=color_levels
        self.color_labels=color_lables


    def contour_map(self):
        params_dict = self.params_dict
        color_labels = self.color_labels
        color_levels = self.color_levels
        cn_fill_colors = np.arange(0,color_levels,1)

        nboxes = np.shape(cn_fill_colors)[0]

        # labels = [""] * nboxes
        #3.图例解释数据
        # if (self.output_img_name.contains("RH") or self.output_img_name.contains("TK")):
        #     labels[0] = "NoData"
        #     labels[1] = "<" + str(cn_levels[1])
        #     labels[nboxes - 1] = ">" + str(cn_levels[nboxes - 2])
        #     for i in range(2, nboxes - 1):
        #         labels[i] = str(cn_levels[i - 1]) + "~" + str(cn_levels[i])
        # else:
        #     labels[0] = "<" + str(cn_levels[0])
        #     labels[nboxes - 1] = ">" + str(cn_levels[nboxes - 2])
        #     for i in range(1, nboxes - 1):
        #         labels[i] = str(cn_levels[i - 1]) + "~" + str(cn_levels[i])

        #4.其他配置
        params_dict['vpHeightF'] = 0.022 * 0.868 * (nboxes + 3 - (nboxes - 5) / 2.8)
        params_dict['lbFillColors'] = cn_fill_colors
        if (self.output_img_name.contains("TK")):
            params_dict["lbLabelFontHeightF"] = 0.009
        else:
            params_dict["lbLabelFontHeightF"] = 0.009677
        lbres = create_or_update_resource(params_dict=params_dict)
        lbid = Ngl.labelbar_ndc(self.workstation, nboxes, color_labels, 0, 0, lbres)

        #5.色标位置配置
        lblres = create_or_update_resource(params_dict=self.location_params_dict)
        Ngl.add_annotation(self.plot, lbid, lblres)