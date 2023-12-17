import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib
import scipy.optimize as op
from sklearn.metrics import r2_score

samples = ["PE", "PS"]

standard_concs = {"PE": [0, 0.025, 0.05, 0.1],
                  "PS": [0, 0.0125, 0.025, 0.05, 0.1],
                  }  # mM
standard_abs = {"PE": [0.000, 0.073, 0.161, 0.356],
                "PS": [0.000, 0.007, 0.064, 0.093, 0.211],
                }  # a.u.

objective_abs = {"PE": 0.095,
                "PS": 0.007,
                }  # a.u.
objective_quantities = {"PE": 4.7,
                     "PS": 3.9,
                     }  # ml

dilution_rate = {"PE": 2,
                 "PS": 1/0.3,
                 }  # 倍


def f(x, a, b):
    return a * x + b


def make_linspace(key, num=100):
    max_temp = max(standard_concs[key])
    min_temp = min(standard_concs[key])
    return np.linspace(min_temp, max_temp, num)


def graph(key,outputpath):
    popt, _ = op.curve_fit(f, standard_concs[key], standard_abs[key])
    x = make_linspace(key)
    y_pred = popt[0] * x + popt[1]
    x_obj = (objective_abs[key] - popt[1])/popt[0]
    r2 = r2_score(standard_abs[key], np.array(standard_concs[key]) * popt[0] + popt[1])
    fig = plt.figure(tight_layout=True, figsize=(8, 6), dpi=300)
    ax = fig.add_subplot(1, 1, 1)
    plt.scatter(standard_concs[key], standard_abs[key], marker=".", label=f"{key}標準液", color='black')
    plt.plot(x, y_pred, label=f'回帰直線: R$^{{{2}}}$={r2:.3f}', color='blue')
    plt.scatter(x_obj, objective_abs[key], color='red', label=f"{key}画分({dilution_rate[key]:.2f}倍希釈)")
    text = f"y = {popt[0]:.4f}x + {popt[1]:.4f}" if popt[1] > 0 else f"y = {popt[0]:.4f}x - {abs(popt[1]):.4f}"
    plt.text(max(standard_concs[key]) / 2, (popt[0] * max(standard_concs[key]) / 2 + popt[1]) * 0.8, text)
    plt.title(f"検量線 ({key})")
    plt.legend()
    plt.xlabel("濃度 (mM)")
    plt.ylabel("吸光度 (a.u.)")
    plt.xlim(ax.get_xlim())
    plt.ylim(ax.get_ylim())
    plt.plot([x_obj, x_obj], [ax.get_ylim()[0], objective_abs[key]], ":")
    plt.plot([ax.get_xlim()[0], x_obj], [objective_abs[key], objective_abs[key]], ":")
    plt.text(x_obj, ax.get_ylim()[0],f"　{x_obj:.3f}", horizontalalignment='left', verticalalignment='bottom')
    plt.text(ax.get_xlim()[0], objective_abs[key], f"　{objective_abs[key]:.3f}", horizontalalignment='left', verticalalignment='bottom')
    plt.savefig(outputpath + f"Day3({key}).jpg", dpi=300)
    # plt.show()
    plt.clf()


def day3(outputpath="/Users/kotaro/Desktop/"):
    for key in samples:
        graph(key,outputpath=outputpath)


if __name__ == "__main__":
    day3()
