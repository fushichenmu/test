from PIL import Image, ImageFont, ImageDraw
def setting_bgImage(im):
    ncc_img = Image.open("/home/xulh/mnt/python/python_script/NCC.png")  # 这个和下面的区别是什么？
    x1, y1 = ncc_img.size
    p1 = Image.new('RGBA', ncc_img.size, (255, 255, 255))
    p1.paste(ncc_img, (0, 0, x1, y1), ncc_img)
    im.paste(p1, (10, 150, 80, 190))
    # 加载bcc.png
    bcc_img = Image.open("/home/xulh/mnt/python/python_script/BCC.png")
    # 设置背景色为白色
    x, y = bcc_img.size
    p = Image.new('RGBA', bcc_img.size, (255, 255, 255))
    p.paste(bcc_img, (0, 0, x, y), bcc_img)
    im.paste(p, (82, 150, 122, 190))
