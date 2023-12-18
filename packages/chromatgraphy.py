from packages.image import concatenate_draw,get_image
import glob

texts = {"day2": ["ニンヒドリン","ヨード"],
         "day3": ["ヨード",],
         "day4": ["ニンヒドリン"],
         }


def get_concat_pictures(outputpath):
    for key in texts:
        lst_path = glob.glob("/Users/kotaro/Desktop/自学/Pycharm/衛生/Pictures/" + key + "/*.JPG")
        lst = []
        for i in range(len(lst_path)):
            lst.append(get_image(lst_path[i]))
        concatenate_draw(lst, texts[key], outputpath, key)
