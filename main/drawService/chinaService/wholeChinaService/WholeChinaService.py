# import Ngl
from handler.ResourceLabelBarHandler import ResourceLabelBarHandler
from handler.ResourceTextHandler import ResourceTextHandler
from handler.WorkstationHandler import WorkstationHandler
from handler.ResourceBaseboardHandler import ResourceBaseboardHandler
from handler.ResourcePolylineHandler import ResourcePolylineHandler
from handler.ResourceSouthseaHandler import ResourceSouthSeaHandler
from resourceConfig import BaseboardConfig as crc
from util import ResourcesUtils, colorTool


class WholeChinaService:
    def __init__(self, businessDto):
        self.businessDto = businessDto

    def draw(self):
        input_data = self.businessDto.input_data
        output_img_type = self.businessDto.output_img_type
        output_img_path = self.businessDto.output_img_path
        output_img_name = self.businessDto.output_img_name
        color_cfg_file = self.businessDto.color_cfg_file


        # 1.创建workstation并且配置workstation的底板夜色  (必选)
        wk_params_dict = self.build_workstationHandler_params()
        workstationHandler = WorkstationHandler(output_img_type, output_img_path, color_cfg_file, wk_params_dict)
        workstation = workstationHandler._get_wk()

        # 2.中国底图 （必选）
        baseboardHandler =  ResourceBaseboardHandler(
            workstation=workstation,input_data=input_data,use_default_setting=True,color_cfg_file=color_cfg_file)
        mapPlot = baseboardHandler.contour_map()
        workstationHandler.plot=mapPlot

        # 3.边界线绘制（可选）
        shape_files =self.businessDto.shape_files
        if True:
            ploylineHandler = ResourcePolylineHandler(workstation=workstation,plot=mapPlot,shapeDtos=shape_files)
            ploylineHandler.contour_map()

        # 4.添加中国图例
        if True:
            labelBarHandler = ResourceLabelBarHandler(workstation=workstation,plot=mapPlot,color_cfg_file = color_cfg_file
                                                      ,output_img_name=output_img_name)
            labelBarHandler.contour_map()

        #5。添加中国比例尺
        if True:
            textHandler = ResourceTextHandler(workstation=workstation,plot=mapPlot)
            textHandler.contour_map()

        #6.南海相关
        shape_files =self.businessDto.shape_files
        if True:
            # def __init__(self, workstation, plot, color_cfg_file='', use_default_setting=True):
            southseaHandler = ResourceSouthSeaHandler(workstation=workstation, plot=mapPlot, color_cfg_file=color_cfg_file, use_default_setting=True)
            southseaHandler.contour_map()


        #7.结束
        workstationHandler.close_workstation()

    def build_workstationHandler_params(self):
        imgWidth, imgHeight = float(self.businessDto.output_img_size.split("x"))  # 输出图片的长宽像素
        wk_params_dict = {
            "wkWidth": imgWidth
            , "wkHeight": imgHeight
        }
        return wk_params_dict

