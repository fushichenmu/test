

def execute(chinaDto):
    '''
    绘图工作的入口，负责处理不同来源的绘图任务
    @param chinaDto:  封装的入参传输对象
    @return: 无返回值
    '''
    region_type = chinaDto.draw_region_type

    common_business_service = ""
    if region_type == "wholeChina":
        from  drawService.chinaService import WholeChinaService
        common_business_service = WholeChinaService(chinaDto)

    nboxes = common_business_service.draw()


    # 11.cmd命令处理其他玩意
    transparentBkColor("white -crop 930x695.912211+0+117.0438945", chinaDto.output_img_path +
                       chinaDto.output_img_name + ".png")
    return nboxes

def add_char(input_img_path, input_img_name, font_file, location, font_size, char):
    '''
    .note 添加图例上的汉字
    .param input_img_path:输入图片路径
    .param input_img_name:输入图片名称
    .param font_file:字体文件
    .param location:添加位置（eg:+1000+800）
    .param font_size:字体大小
    .param char:字符串
    .return: 无返回
    '''
    cmd = ("mogrify -font %s -pointsize %s -annotate %s %s %s%s") % (
        font_file, font_size, location, char, input_img_path, input_img_name)
    os.system(cmd)


def transparentBkColor(color, filename):
    cmd = "convert -transparent %s  %s  %s" % (color, filename, filename)
    os.system(cmd)
