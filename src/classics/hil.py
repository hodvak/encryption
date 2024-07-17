import math
from typing import List

import numpy as np
import numpy
from numpy import matrix
from numpy import linalg


def modMatInv(A, p):  # Finds the inverse of matrix A mod p
    n = len(A)
    A = matrix(A)
    adj = numpy.zeros(shape=(n, n))
    for i in range(0, n):
        for j in range(0, n):
            adj[i][j] = ((-1) ** (i + j) * int(round(linalg.det(minor(A, j, i))))) % p
    return (pow(int(round(linalg.det(A))), -1, p) * adj) % p


def minor(A, i, j):  # Return matrix A with the ith row and jth column deleted
    A = numpy.array(A)
    minor = numpy.zeros(shape=(len(A) - 1, len(A) - 1))
    p = 0
    for s in range(0, len(minor)):
        if p == i:
            p = p + 1
        q = 0
        for t in range(0, len(minor)):
            if q == j:
                q = q + 1
            minor[s][t] = A[p][q]
            q = q + 1
        p = p + 1
    return minor


def text_to_matrix(text: str) -> np.ndarray:
    text = text.lower()
    n = round(len(text) ** 0.5)
    if n ** 2 != len(text):
        raise ValueError("Text must be square")
    arr = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            arr[i, j] = ord(text[i + j * n]) - ord('a')
    return arr


def encrypt(text: List[int] | str,
            matrix: str | np.ndarray,
            mod: int = ord('z') - ord('a') + 1) -> str | List[int]:
    is_text = isinstance(text, str)

    if isinstance(matrix, str):
        matrix = text_to_matrix(matrix)

    if is_text:
        text = text.lower().replace(' ', '')
        text = [ord(c) - ord('a') for c in text]

    n = len(matrix)
    res = []
    for lst in zip(*([iter(text)] * n)):
        lst = np.array(lst)
        # print(matrix)
        # print(lst)
        curr_res = matrix @ lst
        # print(curr_res)
        curr_res = [int(a) % mod for a in curr_res]
        res = res + curr_res

    if is_text:
        res = ''.join([chr(ord('a') + c) for c in res])
    return res


def decrypt(text: List[int] | str,
            matrix: str | np.ndarray,
            mod: int = ord('z') - ord('a') + 1) -> str | List[int]:
    if isinstance(matrix, str):
        matrix = text_to_matrix(matrix)
    matrix = modMatInv(matrix, mod)
    return encrypt(text, matrix, mod)


def find_key(text: str, enc_text: str) -> np.ndarray:
    n = 2
    while n < len(text):
        mat = None
        for i in range(0, len(text) - n, n):
            mat = text_to_matrix(text[i: i + n * n])
            det = int(round(linalg.det(mat)))
            print(f"for text: '{text[i: i + n * n]}'")
            print(f"matrix is:")
            print(mat)
            print(f"det is: {det}")
            if math.gcd(det, 26) != 1:
                print(f"not a good det")
                continue
            inv = modMatInv(mat, 26)
            print("P^(-1) =")
            print(inv)
            print("C =")
            C = text_to_matrix(enc_text[i: i + n * n])
            print(C)
            print("C * P^(-1) =")
            key = (C @ inv) % 26
            print(key)
            print("try this key")
            enc2 = encrypt(text, key)
            print(enc2)
            if enc2 != enc_text:
                print("move to next n")
                break
            else:
                print("done")
                return key
        n += 1


if __name__ == '__main__':
    print(encrypt("whendidalicewritetooscar", np.array([[23, 8],
                                                        [10, 7]])))

    print(decrypt("qjobdirefkawsbyfkrseomgp", np.array([[23, 8],
                                                        [10, 7]])))

    find_key("victorhasreadthistextfromtrent", "lzlgxujprkuqqxtvnsneuffhjuztol")
    print(modMatInv(np.array([[23, 8],
                              [10, 7]]), 26))
    #
    # print(decrypt("aanmwdruaeowqxzmsdmosscjmk", np.array([[3, 7],
    #                                                     [14, 19]])))

    # m = find_key("whendidalicewritetooscar", "ilulvgpsjcagwjmnspwyuoqh")
    # print(m)
    # print(modMatInv(m, 26))
