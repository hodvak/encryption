import math
from typing import Tuple, Optional


def fermat(n: int) -> Tuple[int, int]:
    x = math.ceil(n ** 0.5)
    print(f"x = ceil(sqrt(n)) = {x}")
    y = math.sqrt(x ** 2 - n)
    print(f"y = sqrt(x^2 - n) = {y}")
    while y != round(y):
        x += 1
        print(f"x = x+1 = {x}")
        y = math.sqrt(x ** 2 - n)
        print(f"y = sqrt(x^2 - n) = {y}")
    res = (x - round(y), x + round(y))
    print(f"res = (x-y,x+y) = {res}")
    return res


def pollard(n: int, B: int = 100) -> Optional[Tuple[int, int]]:
    a = 2
    for k in range(2, B + 1):
        a = pow(a, k, n)
        print(f"2^({k}!) % {n} = {a}")
        my_gcd = math.gcd(a - 1, n)
        print(f"gcd(a - 1,n) = {my_gcd}")
        if my_gcd > 1:
            if my_gcd < n:
                res = (my_gcd, n // my_gcd)
                print(f"res =  {res}")
                return res
            print("we cannot find a prime factors ...")
            return None


def with_roots(a, b, n) -> Optional[Tuple[int, int]]:
    if pow(a, 2, n) != pow(b, 2, n):
        print("your so stupid! a^2 need to be equal to b^2 (mod n)")
        return None

    p = math.gcd(a + b, n)
    q = n // p
    res = (p, q)
    print(f"res = {res}")
    return res


if __name__ == "__main__":
    print("fermat")
    print(fermat(26069))

    print("pollard")
    print(pollard(2183))

    print("with_roots")
    print(with_roots(115, 8, 4387))
