from PIL import Image, ImageFont, ImageDraw

def setting_bgImage(im):
    ncc_img = Image.open("/home/nriet/PycharmProjects/test-master/main/logoFiles/NCC.png")  # 这个和下面的区别是什么？
    x1, y1 = ncc_img.size
    p1 = Image.new('RGBA', ncc_img.size, (255, 255, 255))
    p1.paste(ncc_img, (0, 0, x1, y1), ncc_img)
    im.paste(p1, (40,40))
    # 加载bcc.png
    bcc_img = Image.open("/home/nriet/PycharmProjects/test-master/main/logoFiles/BCC.png")
    # 设置背景色为白色
    x, y = bcc_img.size
    p = Image.new('RGBA', bcc_img.size, (255, 255, 255))
    p.paste(bcc_img, (0, 0, x, y), bcc_img)
    im.paste(p, (40+x1+10,40))



def add_title(output_img_file, main_title, sub_titles, standard='cn'):
    if standard=='cn':
        font_file = "/home/nriet/PycharmProjects/test-master/main/fontFiles/MSYH.TTC" #微软雅黑
        font_main = ImageFont.truetype(font=font_file, size=20) #主标题20px
        font_sub = ImageFont.truetype(font=font_file, size=15)  #副标题15px
        top_padding = 40  #上边距40px
        title_padding = 5 #标题间隔5px
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
        im.save(output_img_file)
        # im.show()

add_title("download.png","我爱我家",['副标题1','副标题2'],'cn')




