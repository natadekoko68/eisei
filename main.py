from packages.day3 import day3
from packages.day5 import day5
from packages.chromatgraphy import get_concat_pictures

if __name__ == "__main__":
    # outputpath = "/Users/kotaro/Desktop/"
    outputpath = "./outputs/"
    day3(outputpath=outputpath)
    day5(outputpath=outputpath)
    get_concat_pictures(outputpath=outputpath)
