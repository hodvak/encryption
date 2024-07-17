import numpy as np
import pandas as pd


def encrypt(n, e, M) -> int:
    return pow(M, e, n)


def decrypt(n, d, M) -> int:
    return pow(M, d, n)


sign = decrypt


def fast_decrypt(p, q, d, x) -> int:
    n = p * q
    print(f"n = {n}")

    Mp = q * pow(q, -1, p)
    print(f"Mp = q * (q^-1 mod p) = {Mp}")
    xp = x % p
    print(f"xp = x % p = {xp}")
    dp = d % (p - 1)
    print(f"dp = d % p - 1 = {dp}")
    ap = pow(xp, dp, p)
    print(f"ap = xp^dp % p = {ap}")

    Mq = p * pow(p, -1, q)
    print(f"Mq = p * (p^-1 mod q) = {Mq}")
    xq = x % q
    print(f"xq = x % q = {xq}")
    dq = d % (q - 1)
    print(f"dq = d % q - 1 = {dq}")
    aq = pow(xq, dq, q)
    print(f"aq = xq^dq % q = {aq}")

    a = (Mp * ap + Mq * aq) % n
    print(f"a = (Mp * ap + Mq * aq) % n = {a}")
    print(a)
    return a


fast_sign = fast_decrypt


def square_and_multiply(n: int, e: int, M: int) -> int:
    z2 = []
    zm = []
    z = []

    bin_e = f"{e:b}"
    print(f"e = {bin_e}")
    # res = M
    # print(f"{M}^1 = {res} (mod {n})")
    res = 1
    for index, value in enumerate(bin_e, start=0):
        z.append(res)
        res = res * res % n
        z2.append(res)
        if value == '1':
            res = res * M % n
            zm.append(res)
        if value == '0':
            zm.append(None)
    mat = np.array([z, z2, zm]).T
    data = pd.DataFrame(mat, columns=["z", "z^2 % n", "z * m % n"])
    print(data)
    return res


if __name__ == '__main__':
    # fast_decrypt(131, 199, 12113, 2117)
    print(square_and_multiply(26069, 17, 2117))
    # print(encrypt(101 * 599, 19, 33))
