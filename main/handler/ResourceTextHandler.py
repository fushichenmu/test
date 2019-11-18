from handler import ResourceCommonHandler
from resourceConfig import ScaleConfig as sc
from util.ResourcesUtils import create_or_update_resource
import Ngl


class ResourceTextHandler(ResourceCommonHandler):
    def __init__(self,workstation,plot,use_default_setting=True,scala_figure="Scale 1:20 000 000",location="95x17"):
        ResourceCommonHandler.__init__(workstation=workstation,plot=plot,use_default_setting=use_default_setting)
        self.scala_figure = scala_figure
        self.location = location

    def contour_map(self):
        params_dict = {}
        scala_figure =self.scala_figure
        lon_axis_value,lat_axis_value  = self.location.split("x")
        if self.use_default_setting:
            params_dict = sc.get_whole_china_common_config()
        resource = create_or_update_resource(params_dict)
        Ngl.add_text(self.workstation, self.plot, scala_figure, lon_axis_value, lat_axis_value, resource)