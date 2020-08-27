from PIL import Image, ImageDraw, ImageFont, ImageGrab

# 指定要使用的字体和大小；/Library/Fonts/是macOS字体目录；Linux的字体目录是/usr/share/fonts/
# font = ImageFont.truetype('C:\Windows\Fonts\ARIALUNI.TTF', 16)
# font = ImageFont.truetype('C:\Windows\Fonts\ARIALUNI.TTF', 16)
# font = ImageFont.truetype('C:\Windows\Fonts\ARIALUNI.TTF', 16)
# font = ImageFont.truetype('C:\Windows\Fonts\\arialbd.ttf', 24)



# image: 图片  text：要添加的文本 font：字体
def add_text_to_image(image, text):
    rgba_image = image.convert('RGBA')
    text_overlay = Image.new('RGBA', rgba_image.size, (255, 255, 255, 0))
    image_draw = ImageDraw.Draw(text_overlay)
    # 设置字体大小和图片成比例
    y = rgba_image.size[1]
    print(y)
    if y > 860:
        font_size = 24
    elif 480 < y:
        font_size = 18
    else:
        font_size = 12
    print(font_size)
    font = ImageFont.truetype('C:\Windows\Fonts\\arialbd.ttf', font_size)
    text_size_x, text_size_y = image_draw.textsize(text, font=font)
    # 设置文本文字位置
    print(rgba_image)
    text_xy = (rgba_image.size[0] - text_size_x - 10, rgba_image.size[1] - text_size_y - 10)
    # 设置文本颜色和透明度
    image_draw.text(text_xy, text, font=font, fill=(240, 240, 240, 180))
    # image_draw.text(text_xy, text, font=font, fill=(227, 62, 51, 180))

    image_with_text = Image.alpha_composite(rgba_image, text_overlay)

    return image_with_text


# im_before = Image.open("sorce.jpg")
# im_before.show()
im_before = ImageGrab.grabclipboard()  # 获取剪贴板文件
im_after = add_text_to_image(im_before, '1024shen.com')
im_after.show()
# input("11111")
