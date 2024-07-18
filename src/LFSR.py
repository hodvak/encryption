from typing import List


def test_formula(formula: List[bool], data: List[bool]) -> bool:
    if len(formula) != len(data):
        print("WTF")
        return

    return (sum(f and d for f, d in zip(formula, data)) % 2 == 1)


def get_series(start_values: List[int | bool] | str, recursive: List[int | bool] | str) -> str:
    start_values = [str(int(a)) != '0' for a in start_values]
    recursive = [str(int(a)) != '0' for a in recursive]
    my_length = len(start_values)
    if my_length != len(recursive):
        print("TF you want?!")
    res = start_values[::]
    res.append(test_formula(recursive, res[-my_length:]))
    while any(a != b for a, b in zip(start_values, res[-my_length:])):
        res.append(test_formula(recursive, res[-my_length:]))

    res = res[:-my_length]
    res = "".join(str(int(r)) for r in res)
    print(res + "|" + ''.join(str(int(a)) for a in start_values))
    return res



if __name__ == '__main__':
    # for 10110 with x_{n+5} = x_{n+0} xor x_{n+1} xor x_{n+4}
    # ser = get_series("10110", "11001")
    ser = get_series("111000", "111111")
    print(ser, len(ser))
