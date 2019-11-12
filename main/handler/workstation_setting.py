import Ngl
from thirdTime.util import colorTool


def create_workstation(colorBarName, image_path):
    # 3.1打开工作台
    wkres = Ngl.Resources()
    wkres.wkWidth = 930
    wkres.wkHeight = 930
    workstation = Ngl.open_wks("png", image_path, wkres)
    # 3.2获取底板颜色
    cmap = colorTool.getColorMap(colorBarName)
    Ngl.define_colormap(workstation, cmap)
    return workstation