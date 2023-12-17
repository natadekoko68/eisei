import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib
import scipy.optimize as op

samples = ["PE","PS"]

kenryosen_concs = {"PE":[0, 0.025, 0.05, 0.1],
                   "PS":[0, 0.0125, 0.025, 0.05, 0.1],
                   } #mM
kenryosen_abs = {"PE" : [0.000, 0.073, 0.161, 0.356],
                 "PS" : [0.000, 0.007, 0.064, 0.093, 0.211],
                 } #a.u.

mokuteki_abs = {"PE" : 0.095,
                "PS" : 0.007,
                } #a.u.

mokuteki_quantity = {"PE" : 4.7,
                     "PS" : 3.9,
                     } #ml

def f(x,a,b):
    return a * x + b

def make_linspace(key,num=100):
    max_temp = max(kenryosen_concs[key])
    min_temp = min(kenryosen_concs[key])
    return np.linspace(min_temp,max_temp,num)


from sklearn.metrics import r2_score


def graph(key):
    popt, _ = op.curve_fit(f, kenryosen_concs[key], kenryosen_abs[key])
    x = make_linspace(key)
    y_pred = popt[0] * x + popt[1]
    r2 = r2_score(kenryosen_abs[key], np.array(kenryosen_concs[key])*popt[0] + popt[1])
    plt.scatter(kenryosen_concs[key], kenryosen_abs[key], marker=".", label=key)
    plt.plot(x, y_pred, label=f'Fit: R2={r2:.4f}', color='black')
    plt.title(f"検量線({key})")
    plt.legend()
    plt.xlabel("濃度 (mM)")
    plt.ylabel("吸光度 (a.u.)")
    plt.tight_layout()
    plt.show()

def main():
    for key in samples:
        graph(key)

if __name__=="__main__":
    main()



