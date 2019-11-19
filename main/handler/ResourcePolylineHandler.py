from handler import ResourceCommonHandler
from resourceConfig import GISLayersConfig as plc
from util.ResourcesUtils import create_or_update_resource
import numpy as np
import os
shape_file_path = "/nfsshare/cdbdata/algorithm/conductor/WMFS/EXTPRE/ysq/map/"


class ResourcePolylineHandler(ResourceCommonHandler):
    def __init__(self,workstation,plot,param_dict):
        ResourceCommonHandler.__init__(self,workstation=workstation,plot = plot)
        self.param_dict = param_dict

    def contour_map(self):
        for key, params_dict in self.param_dict.items():
            file_name = params_dict.pop('file_name')
            type = params_dict.pop('type')
            shape = Nio.open_file(shape_file_path+file_name, "r")
            lon = np.ravel(shape.variables["x"][:])
            lat = np.ravel(shape.variables["y"][:])
            params_dict['gsSegments'] = shape.variables["segments"][:, 0]
            resource = create_or_update_resource(params_dict=params_dict)
            # 2.绘制曲线图
            if type =='polyline':
                Ngl.add_polyline(self.workstation, self.plot, lon, lat, resource)
