from handler import ResourceCommonHandler
from resourceConfig import ScaleConfig as sc
from util.ResourcesUtils import create_or_update_resource
import Ngl


class ResourceTextHandler(ResourceCommonHandler):
    def __init__(self,workstation,plot,params_dict={}):
        ResourceCommonHandler.__init__(workstation=workstation,plot=plot)
        self.params_dict = params_dict


    def contour_map(self):
        params_dict = self.params_dict

        scala_figure =params_dict.pop('scala_figure')
        lon_axis_value,lat_axis_value= params_dict.pop('location',default='93x17').split("x")

        resource = create_or_update_resource(params_dict)
        Ngl.add_text(self.workstation, self.plot, scala_figure, lon_axis_value, lat_axis_value, resource)