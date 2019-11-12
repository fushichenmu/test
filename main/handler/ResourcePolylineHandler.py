from handler import ResourceCommonHandler
from resourceConfig import PolylineConfig as plc
from util.ResourcesUtils import create_or_update_resource
import numpy as np

shape_file_path = "/nfsshare/cdbdata/algorithm/conductor/WMFS/EXTPRE/ysq/map/"


class ResourcePolylineHandler(ResourceCommonHandler):
    def __init__(self,workstation,plot,shapeDtos):
        ResourceCommonHandler.__init__(self,workstation=workstation)
        self.plot = plot
        self.shapeDtos = shapeDtos

    def contour_map(self):

        for shapeDto in self.shapeDtos:#对于每一个线条绘制需求
            # 1.参数组装
            file_name = shapeDto.file_name
            params_dict={}
            if shapeDto.use_default_setting: #读取其默认配置
                params_dict = plc.get_whole_china_common_config(file_name=file_name)
            if shapeDto.params_dict: #兼容用户自定义配置
                params_dict.update(shapeDto.params_dict)
            shape = Nio.open_file(shape_file_path+file_name, "r")
            lon = np.ravel(shape.variables["x"][:])
            lat = np.ravel(shape.variables["y"][:])
            params_dict['gsSegments'] = shape.variables["segments"][:, 0]
            resource = create_or_update_resource(params_dict=params_dict)

            # 2.绘制曲线图
            Ngl.add_polyline(self.workstation, self.plot, lon, lat, resource)