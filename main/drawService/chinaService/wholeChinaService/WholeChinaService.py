# import Ngl
from handler.ResourceLabelBarHandler import ResourceLabelBarHandler
from handler.ResourceTextHandler import ResourceTextHandler
from handler.WorkstationHandler import WorkstationHandler
from handler.ResourceBaseboardHandler import ResourceBaseboardHandler
from handler.ResourcePolylineHandler import ResourcePolylineHandler
from handler.ResourceSouthseaHandler import ResourceSouthSeaHandler
from handler import ResourceTitleAndLogoHandler
from resourceConfig.ChinaConfig import china_params_dict
import xml


class WholeChinaService:
    def __init__(self, input_data,business_params_dict):
        self.business_params_dict = business_params_dict
        self.input_data=input_data

    def draw(self):
        input_data = self.input_data
        output_img_type = self.business_params_dict["output_img_type"]
        output_img_path = self.business_params_dict["output_img_path"]
        output_img_name = self.business_params_dict["output_img_name"]
        # output_img_size = self.business_params_dict['output_img_size']
        color_lables = self.business_params_dict["color_lables"]
        color_levels = self.business_params_dict["color_levels"]
        color_levels_default = self.business_params_dict["color_levels_default"]
        main_title = self.business_params_dict["main_title"]
        sub_titles = self.business_params_dict["sub_titles"]






        # 1.创建workstation并且配置workstation的底板夜色  (必选)
        wk_params_dict = self.build_workstationHandler_params()
        workstationHandler = WorkstationHandler(output_img_type, output_img_path, color_levels, wk_params_dict)
        workstation = workstationHandler._get_wk()

        # 2.中国底图 （必选）
        baseboardHandler =  ResourceBaseboardHandler(
            workstation=workstation,input_data=input_data,use_default_setting=True,color_levels=color_levels,param_dict=china_params_dict.get('china_baseboard'))
        mapPlot = baseboardHandler.contour_map()
        workstationHandler.plot=mapPlot

        # 3.边界线绘制（可选）
        if True:
            ploylineHandler = ResourcePolylineHandler(workstation=workstation,plot=mapPlot,param_dict=china_params_dict.get('china_geoline'))
            ploylineHandler.contour_map()

        # 4.添加中国图例
        if True:
            labelBarHandler = ResourceLabelBarHandler(workstation=workstation,plot=mapPlot,color_cfg_file = color_cfg_file
                                                      ,output_img_name=output_img_name)
            labelBarHandler.contour_map()

        #5.添加中国比例尺
        if True:
            textHandler = ResourceTextHandler(workstation=workstation,plot=mapPlot)
            textHandler.contour_map()

        #6.南海相关
        if True:
            southseaHandler = ResourceSouthSeaHandler(workstation=workstation, plot=mapPlot, color_cfg_file=color_cfg_file, use_default_setting=True)
            southseaHandler.contour_map()

        #7.关闭workstation
        workstationHandler.close_workstation()

        #8.绘制多级标题及logo
        ResourceTitleAndLogoHandler.add_title(output_img_file=output_img_path + output_img_name + output_img_type
                                              , main_title=main_title, sub_titles=sub_titles, standard='cn')

    def build_workstationHandler_params(self):
        imgWidth, imgHeight = float(self.business_params_dict["output_img_size"].split("x"))  # 输出图片的长宽像素
        wk_params_dict = {
            "wkWidth": imgWidth
            , "wkHeight": imgHeight
        }
        return wk_params_dict

