from PIL import Image, ImageDraw, ImageFont

def concatenate(lst,outputpath,title):
    num = len(lst)
    width = 0
    for i in range(num):
        width += lst[i].width
    height = lst[0].height
    dst = Image.new("RGB", (width, height))
    temp_width = 0
    for i in range(num):
        dst.paste(lst[i], (temp_width, 0))
        temp_width += lst[i].width
    dst.save(outputpath + title + "_concatenated.jpg")
    return dst

def concatenate_h(lst,outputpath,title):
    num = len(lst)
    height = 0
    for i in range(num):
        height += lst[i].height
    width = lst[0].width
    dst = Image.new("RGB", (width, height))
    temp_height = 0
    for i in range(num):
        dst.paste(lst[i], (0, temp_height))
        temp_height += lst[i].height
    dst.save(outputpath + title + "_concatenated_h.jpg")
    return dst

def get_image(input_path):
    return Image.open(input_path)


def concatenate_draw(lst, texts, outputpath, title, font_path="/Users/kotaro/Desktop/自学/Pycharm/衛生/inputs/NotoSansJP-Medium.ttf"):
    font = ImageFont.truetype(font_path, 60)
    num = len(lst)
    width = 0
    for i in range(num):
        width += lst[i].width
    height = lst[0].height
    dst = Image.new("RGB", (width, height))
    temp_width = 0
    for i in range(num):
        dst.paste(lst[i], (temp_width, 0))
        temp_width += lst[i].width

    draw = ImageDraw.Draw(dst)
    temp_width = 0
    for i in range(num):
        draw.text((temp_width+lst[i].width*0.05, lst[i].height * 0.05), texts[i], "red", font=font)
        temp_width += lst[i].width
    dst.save(outputpath + title + "_concatenated_draw.jpg")
    return dst

if __name__=="__main__":
    pass