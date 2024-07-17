import numpy as np
import pandas as pd

np.set_printoptions(suppress=True)


def oclides(a, b):
    if a < b:
        a, b = b, a

    # a > b
    i = [0, 1]
    ri = [a, b]
    qi = [None]

    while ri[-1] != 0:
        div = ri[-2] // ri[-1]
        rem = ri[-2] % ri[-1]

        i.append(i[-1] + 1)
        ri.append(rem)
        qi.append(div)

    qi.append(None)

    si = [0, 1]
    ti = [1, 0]
    for index in i[2:-1]:
        si.append(-qi[index - 1] * si[index - 1] + si[index - 2])
        ti.append(-qi[index - 1] * ti[index - 1] + ti[index - 2])

    si.append(None)
    ti.append(None)

    mat = np.array([i, ri, qi, si, ti]).T
    data = pd.DataFrame(mat, columns=["i", "ri", "qi", "si", "ti"])
    print(data)
    print(si[-2] * b + ti[-2] * a)
    print(f"{si[-2]} * {b} + {ti[-2]} * {a} = {ri[-2]}")


if __name__ == '__main__':
    oclides((131 - 1) * (199-1), 17)

