import numpy as np
import Ngl
import Nio

def draw_sea_polyline(endLon, plot, wks):
    # 海岸线- 图1 绘制(海岸线和等高线有区别吗)
    shpf3 = Nio.open_file("/home/xulh/mnt/python/python_script/orl/quanqiu/HAX.shp", "r")
    # 4海岸线
    lon3 = np.ravel(shpf3.variables["x"][:])
    lat3 = np.ravel(shpf3.variables["y"][:])
    segments3 = shpf3.variables["segments"][:, 0]
    dqres = Ngl.Resources()  # -- resources for polylines
    dqres.gsLineColor = "black"
    dqres.gsLineThicknessF = 1.0
    dqres.gsSegments = segments3
    Ngl.add_polyline(wks, plot, lon3, lat3, dqres)
    # 5.海岸线-图2 绘制
    shpf4 = Nio.open_file("/home/xulh/mnt/python/python_script/orl/quanqiu/DYAX.shp", "r")
    lon4 = np.ravel(shpf4.variables["x"][:])
    lat4 = np.ravel(shpf4.variables["y"][:])
    segments4 = shpf4.variables["segments"][:, 0]
    dqres = Ngl.Resources()
    dqres.gsLineColor = "black"
    dqres.gsLineThicknessF = 1.0
    dqres.gsSegments = segments4
    Ngl.add_polyline(wks, plot, lon4, lat4, dqres)
    if endLon == 360:
        resp = Ngl.Resources()
        resp.gsLineColor = "black"
        resp.gsLineThicknessF = 1
        resp.gsLineDashPattern = 2
        Ngl.add_polyline(wks, plot, [0, 180], [0, 0], resp)
        Ngl.add_polyline(wks, plot, [180, 360], [0, 0], resp)
        Ngl.add_polyline(wks, plot, [180, 180], [-90, 90], resp)


