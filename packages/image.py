from PIL import Image, ImageDraw, ImageFont

def concatenate(lst,outputpath):
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
    dst.save(outputpath + "_concatenated.jpg")
    return dst

def get_image(input_path):
    return Image.open(input_path)

if __name__=="__main__":
    pass
