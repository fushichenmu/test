from handler import ResourceCommonHandler
from resourceConfig import GISLayersConfig as plc
from resourceConfig import SouthSeaConfig as ssc
from util.ResourcesUtils import create_or_update_resource
import numpy as np
from util import colorTool,ResourcesUtils
import Ngl,Nio,os
shape_file_path = "/nfsshare/cdbdata/algorithm/conductor/WMFS/EXTPRE/ysq/map/"


class ResourceSouthSeaHandler(ResourceCommonHandler):
    def __init__(self,workstation,plot,color_cfg_file='',use_default_setting=True):
        ResourceCommonHandler.__init__(self,workstation=workstation,use_default_setting =use_default_setting,color_cfg_file=color_cfg_file)
        self.plot = plot


    def contour_map(self):
        # 1.绘制南海底板
        if self.use_dafault_setting:
            resource_config = ssc.get_south_sea_common_config()
        if self.color_cfg_file:
            cnLevels = colorTool.getColorValueDef(self.color_cfg_file)
            cn_params_dict = {
                "cnLevels": cnLevels
                , "cnFillColors": colorTool.getColorOrder(self.color_cfg_file)
            }
            resource_config.update(cn_params_dict)
        # 是否有用户自定义配置
        if self.params_dict:
            resource_config.update(self.params_dict)
        self.resource = create_or_update_resource(params_dict=resource_config)
        south_sea_plot = Ngl.contour_map(self.workstation, self.input_data, self.resource)

        # 2.绘制南海地理线
        file_names = ["nh/BOUL_G.shp","BOUL_S.shp","nh/BOUL_S2.shp","nh/HAX.shp","nh/HFCP.shp"]  #nh/BOUL_JDX.shp 九段线已经在已定国界中包含
        for file_name in file_names:#对于每一个线条绘制需求
            params_dict = plc.get_whole_china_common_config(prefix= "south_sea_"
                                                            ,file_name=os.path.basename(file_name).split('.')[0])
            shape = Nio.open_file(shape_file_path+file_name, "r")
            lon = np.ravel(shape.variables["x"][:])
            lat = np.ravel(shape.variables["y"][:])
            params_dict['gsSegments'] = shape.variables["segments"][:, 0]
            resource = create_or_update_resource(params_dict=params_dict)
            Ngl.add_polyline(self.workstation, south_sea_plot, lon, lat, resource)

        # 3. 南海加比例尺
        txres = Ngl.Resources()
        txres.txFontHeightF = 0.008
        txres.txFontColor = "black"
        Ngl.add_text(self.workstation, south_sea_plot, "1:40 000 000", 118, 3, txres)

        # 4.南海放在中国的位置
        adres = Ngl.Resources()
        adres.amParallelPosF = 0.489247
        adres.amOrthogonalPosF = 0.4856322
        adres.amJust = "BottomRight"
        Ngl.add_annotation(self.plot, south_sea_plot, adres)




