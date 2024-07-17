from typing import List
import consts
from classics import frequency
from numpy import convolve


def encrypt(text: List[int] | str, key: int | str, mod: int = ord('z') - ord('a') + 1) -> str | List[int]:
    is_text = isinstance(text, str)
    if isinstance(key, str):
        key = ord(key) - ord('a')
    key %= mod
    if is_text:
        text = text.lower().replace(' ', '')
        text = [ord(c) - ord('a') for c in text]

    res = [(a + key) % mod for a in text]

    if is_text:
        res = ''.join([chr(ord('a') + key) for key in res])

    return res


def decrypt(text: List[int] | str, key: int | str, mod: int = ord('z') - ord('a') + 1) -> str | List[int]:
    return encrypt(text, -key, mod)


def get_frequency_key_old(encrypted_text: str) -> None:
    text_freq = sorted(frequency.get_frequency(encrypted_text).items(), key=lambda x: -x[1])
    top_my_letter, freq_my_letter = text_freq[0]
    english_freq = sorted(list(consts.english_freq.items()), key=lambda x: -x[1])
    for top_english_letter, freq_english_letter in english_freq:
        print(f"my top letter: '{top_my_letter}' with frequency: {freq_my_letter}%")
        print(f"top english letter: '{top_english_letter}' with frequency: {freq_english_letter}%")
        key = (ord(top_my_letter) - ord(top_english_letter)) % 26
        print(f"key is {key}")
        print(f"sentence = '{decrypt(encrypted_text, key)}'")
        print(f"=" * 30)


def get_frequency_key_new(encrypted_text: str) -> None:
    """
    The naive Nelson
    :param encrypted_text:
    :return:
    """
    text_freq = frequency.get_frequency(encrypted_text)
    english_freq = list(consts.english_freq.values())

    mult_freq = convolve(list(text_freq.values())[::-1], (english_freq * 2)[:-1], mode='valid')

    data = sorted(list(enumerate(mult_freq)), key=lambda x: -x[1])
    for key, number in data:
        print(f"key is {26 - key} with frequency: {number / 100}%")
        print(f"sentence = '{decrypt(encrypted_text, 26 - key)}'")
        print(f"=" * 30)


if __name__ == '__main__':
    # example text
    # dec_sentance = encrypt("hello my friend my name is hod and I love you from all my heart", 12)
    # dec_sentance = "rgii aecp pqvy tkvg vqhg tocv"
    # dec_sentance = "lzlgx ujprk uqqxt vnsne uffhj uztol"

    # dec_sentance = "vielm bdugb oujld iglof ltbmc lbohl" - affine
    #                "victo rhasr eadth istex tfrom trent"
    #
    # f(x) = ax + b mod 26
    # f('a') = a * 'a' + b mod 26
    # 20 = a * 0 + b mod 26
    # b = 20
    # 3 = a * 7 + 20 mod 26
    # 9 = 7a mod 26
    # 5 = a mod 26
    # a = 5
    # f(x) = 5x + 20 mod 26
    #

    dec_sentance = "sfzql oexpo bxaqe fpqbu qcolj qobkq" # M3 - cieser

    # using nelson (my favorite method)
    get_frequency_key_new(dec_sentance)
    # print("===\n" * 5)

    # using the most used letter (please do something with that, it's just compare the most used each time,
    # you can change the method to show all the frequency of all the letter and check for yourself what's the best key)
    # get_frequency_key_old(dec_sentance)
