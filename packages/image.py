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

if __name__=="__main__":
    pass
