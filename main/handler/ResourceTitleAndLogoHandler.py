from PIL import Image, ImageFont, ImageDraw

def setting_bgImage(im):
    # ncc_img = Image.open("/home/nriet/PycharmProjects/test-master/main/logoFiles/NCC.png")  # 这个和下面的区别是什么？
    ncc_img = Image.open(r"E:\PythonWorkSpace\test\main\NCC.png")  # 这个和下面的区别是什么？
    x1, y1 = ncc_img.size
    p1 = Image.new('RGBA', ncc_img.size, (255, 255, 255))
    p1.paste(ncc_img, (0, 0, x1, y1), ncc_img)
    im.paste(p1, (40,40))
    # 加载bcc.png
    # bcc_img = Image.open("/home/nriet/PycharmProjects/test-master/main/logoFiles/BCC.png")
    bcc_img = Image.open(r"E:\PythonWorkSpace\test\main\BCC.png")
    # 设置背景色为白色
    x, y = bcc_img.size
    p = Image.new('RGBA', bcc_img.size, (255, 255, 255))
    p.paste(bcc_img, (0, 0, x, y), bcc_img)
    im.paste(p, (40+x1+10,40))



def add_title(output_img_file, main_title, sub_titles, params_dict={},standard='cn'):
    if standard=='cn':
        font_file = params_dict.get('font_file_path')
        font_main_size = params_dict.get('font_main_size')
        font_sub_size = params_dict.get('font_sub_size')
        font_main = ImageFont.truetype(font=font_file, size=font_main_size) #主标题20px
        font_sub = ImageFont.truetype(font=font_file, size=font_sub_size)  #副标题15px
        top_padding = params_dict.get('top_padding')  #上边距40px
        title_padding = params_dict.get('title_padding') #标题间隔5px
        im = Image.open(output_img_file, "r")
        draw = ImageDraw.Draw(im)
        img_width,img_height=im.size

        #主标题绘制
        main_width, main_height = draw.textsize(main_title, font_main)
        draw.text(((img_width - main_width) / 2, top_padding), main_title, font=font_main, fill='black')
        #副标题绘制
        for subtitle in sub_titles:
            sub_width, sub_height = draw.textsize(subtitle, font_sub)
            index = sub_titles.index(subtitle)
            draw.text(((img_width - sub_width) / 2, top_padding+main_height+(index+1)*title_padding+index*sub_height), subtitle, font=font_sub, fill='black')
        setting_bgImage(im)
        # im.save(output_img_file)
        im.show()
    else:
        pass #其他的待定

logo_and_titles= {
    "font_file_path": r"C:\Windows\Fonts\MSYH.TTC"  # 微软雅黑
    , "font_main_size": 20  # 主标题20px
    , "font_sub_size": 15  # 副标题15px
    , "top_padding": 40  # 上边距40px
    , "title_padding": 5  # 标题间隔5px
}


add_title(r"E:\PythonWorkSpace\test\main\download.png","我爱我家",['副标题1','副标题2'],logo_and_titles,'cn')




