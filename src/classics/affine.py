import math
from typing import List, Tuple
import consts
from classics import frequency
from numpy import convolve


def encrypt(text: List[int] | str,
            key_a: int | str,
            key_b: int | str,
            mod: int = ord('z') - ord('a') + 1) -> str | List[int]:
    is_text = isinstance(text, str)

    if isinstance(key_a, str):
        key_a = ord(key_a) - ord('a')
    key_a %= mod

    if isinstance(key_b, str):
        key_b = ord(key_b) - ord('a')
    key_b %= mod

    if is_text:
        text = text.lower().replace(' ', '')
        text = [ord(c) - ord('a') for c in text]

    res = [(a * key_a + key_b) % mod for a in text]

    if is_text:
        res = ''.join([chr(ord('a') + key) for key in res])

    return res


def reverse_key(key_a: int, key_b: int, mod: int = ord('z') - ord('a') + 1) -> Tuple[int, int]:
    a_minus_1 = pow(key_a, -1, mod)
    return a_minus_1, (- a_minus_1 * key_b) % mod  # (a^-1, (-a^-1 * b) % 26)


def decrypt(text: List[int] | str,
            key_a: int | str,
            key_b: int | str,
            mod: int = ord('z') - ord('a') + 1) -> str | List[int]:
    a_minus_1 = pow(key_a, -1, mod)
    return encrypt(text, a_minus_1, (- a_minus_1 * key_b) % mod, mod)


def get_frequency_key_new(encrypted_text: str) -> None:
    """
    The naive Nelson
    :param encrypted_text:
    :return:
    """
    text_freq = list(frequency.get_frequency(encrypted_text).values())
    english_freq = list(consts.english_freq.values())

    data = []
    num_of_letters = ord('z') - ord('a') + 1
    for key_a in range(num_of_letters):
        if math.gcd(key_a, num_of_letters) != 1:
            continue
        my_freq = [(((key_a * index) % num_of_letters), text_freq[index]) for index in range(num_of_letters)]
        my_freq.sort(key=lambda a: a[0])
        my_freq = [a[1] for a in my_freq]

        mult_freq = convolve(my_freq[::-1], (english_freq * 2)[:-1], mode='valid')
        for key_b, number in enumerate(mult_freq):
            data.append((reverse_key(key_a, key_b), number))

    data.sort(key=lambda a: -a[1])
    for d in data:
        print(f"key = {d[0]} with freq of {d[1] / 100}%")
        print(decrypt(encrypted_text, *d[0]))


if __name__ == '__main__':
    # example text
    dec_sentance = encrypt(
        "english learners spend a lot of time learning complex grammar structures and advanced vocabulary and may end up with language that is too formal for",
        7, 13)
    # dec_sentance = encrypt("hello my friend my name is hod and I love you from all my heart", 3, 4)
    # dec_sentance = "vielm bdugb oujld iglof ltbmc lbohl"
    # using nelson (my favorite method)
    # get_frequency_key_new(dec_sentance)
    print(reverse_key(5, 20))

    # print(encrypt("vielm bdugb oujld iglof ltbmc lbohl", 21, 22))
    # print(reverse_key(5, 20))
