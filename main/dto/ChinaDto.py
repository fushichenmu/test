class ChinaDto:
    def __init__(self, input_data, color_cfg_file='', output_img_size='930x930'
                 , output_img_path='', output_img_name='', output_img_type='png'
                 ,draw_south_sea=True,draw_legend=True,draw_region_type="wholeChina"
                 ,busId='',title_figures=[]):
        self.input_data = input_data
        self.color_cfg_file = color_cfg_file
        self.output_img_size = output_img_size
        self.output_img_path = output_img_path
        self.output_img_name = output_img_name
        self.output_img_type = output_img_type
        self.title_figures = title_figures  # 标题列表
        self.draw_south_sea = draw_south_sea
        self.draw_legend = draw_legend
        self.draw_region_type = draw_region_type
        self.busId = busId


