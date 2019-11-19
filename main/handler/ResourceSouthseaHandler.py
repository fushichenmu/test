from handler import ResourceCommonHandler
from resourceConfig import GISLayersConfig as plc
from resourceConfig import SouthSeaConfig as ssc
from util.ResourcesUtils import create_or_update_resource
import numpy as np
from util import colorTool, ResourcesUtils
import Ngl, Nio, os

shape_file_path = "/nfsshare/cdbdata/algorithm/conductor/WMFS/EXTPRE/ysq/map/"


class ResourceSouthSeaHandler(ResourceCommonHandler):
    def __init__(self, workstation, plot,input_data, params_dict={},color_levels=[]):
        ResourceCommonHandler.__init__(self, workstation=workstation,input_data=input_data)
        self.plot = plot
        self.params_dict = params_dict
        self.color_levels = color_levels


    def contour_map(self):
        params_dict = self.params_dict
        color_levels = self.color_levels
        cn_fill_colors = np.arange(0,len(color_levels),1)

        # 1.绘制南海底板
        south_sea_baseboard = params_dict.pop('south_sea_baseboard')
        south_sea_baseboard['cnLevels'] = color_levels
        south_sea_baseboard['cnFillColors'] = cn_fill_colors
        resource = create_or_update_resource(params_dict=south_sea_baseboard)
        south_sea_plot = Ngl.contour_map(self.workstation, self.input_data, resource)


        # 2.绘制南海相关地理线
        south_sea_geoline = params_dict.pop('south_sea_geoline')  # 多级
        for key, params_dict in south_sea_geoline.items():
            file_name = params_dict.pop('file_name')
            type = params_dict.pop('type')
            shape = Nio.open_file(shape_file_path + file_name, "r")
            lon = np.ravel(shape.variables["x"][:])
            lat = np.ravel(shape.variables["y"][:])
            params_dict['gsSegments'] = shape.variables["segments"][:, 0]
            resource = create_or_update_resource(params_dict=params_dict)
            # 2.绘制曲线图
            if type == 'polyline':
                Ngl.add_polyline(self.workstation, south_sea_plot, lon, lat, resource)
            else:
                pass #polygon/point 处理待定

        # 3. 南海加比例尺
        south_sea_scale = params_dict.pop('south_sea_scale')
        scala_figure = south_sea_scale.pop('scala_figure')
        x,y = south_sea_scale.pop('location').split('x')
        resource = create_or_update_resource(params_dict=south_sea_scale)
        Ngl.add_text(self.workstation, south_sea_plot, scala_figure, x, y, resource)

        # 4.南海放在中国的位置
        south_sea_location = params_dict.pop('south_sea_location')
        resource = create_or_update_resource(params_dict=south_sea_location)
        Ngl.add_annotation(self.plot, south_sea_plot, resource)



