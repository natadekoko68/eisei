import matplotlib.pyplot as plt
import japanize_matplotlib
from PIL import Image
import matplotlib.gridspec as gridspec

fluorescent = {"No.1": 1.801,
               "No.2": 1.817,
               "No.3": 1.729,
               "No.4": 1.926,
               "No.5": 1.840,
               "No.6": 2.107,
               "No.7": 1.390,
               "No.8": 1.561,
               "No.9": 1.375,
               "No.10": 1.880,
               "No.11": 1.449,
               "No.12": 1.230,
               "No.13": 2.013,
               "No.14": 0.814,
               }

def to_percentage(key, background="No.14", maximum="No.13"):
    return 100 * (fluorescent[key] - fluorescent[background]) / (fluorescent[maximum] - fluorescent[background])


def prev_main():
    assert (len(fluorescent) == 14)
    labels = [f"No.{i}" for i in range(1, 15)]
    percentage = list(map(to_percentage, fluorescent))
    fig = plt.figure(tight_layout=True, figsize=(12, 6), dpi=300)
    plt.bar([i for i in range(1, 15)], percentage, tick_label=labels)
    plt.title("各サンプルにおけるヒスタミン放出率", size=15)
    plt.ylabel(r"割合 ($\%$)")
    plt.xlabel("サンプル")
    plt.grid(axis="y", linestyle="dotted", color="gray")
    plt.savefig("/Users/kotaro/Desktop/Day5.jpg", dpi=300)
    plt.show()

def day5(outputpath):
    assert (len(fluorescent) == 14)
    percentage = list(map(to_percentage, fluorescent))
    fig = plt.figure(tight_layout=True, figsize=(10, 10), dpi=300)
    gs = gridspec.GridSpec(2, 1)
    plt.subplot(gs[0, 0])
    plt.bar([i for i in range(1, 15)], percentage, tick_label=[f"No.{i}" for i in range(1, 15)])
    plt.title("各サンプルにおけるヒスタミン放出率", size=15)
    plt.ylabel(r"割合 ($\%$)")
    plt.xlabel("サンプル")
    plt.grid(axis="y", linestyle="dotted", color="gray")
    plt.subplot(gs[1,0])
    plt.axis("off")
    im = Image.open("/Table5.png")
    plt.imshow(im)
    plt.savefig(outputpath+"Day5.jpg", dpi=300)
    # plt.show()
    plt.clf()


if __name__ == "__main__":
    day5()
