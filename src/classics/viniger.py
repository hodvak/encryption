from typing import List


def encrypt(text: List[int] | str,
            word: List[int] | str,
            mod: int = ord('z') - ord('a') + 1) -> str | List[int]:
    is_text = isinstance(text, str)

    if isinstance(word, str):
        word = [ord(c) - ord('a') for c in word]

    if is_text:
        text = text.lower().replace(' ', '')
        text = [ord(c) - ord('a') for c in text]

    res = [(a + word[i % len(word)]) % mod for i, a in enumerate(text)]

    if is_text:
        res = ''.join([chr(ord('a') + a) for a in res])

    return res


def decrypt(text: List[int] | str,
            word: List[int] | str,
            mod: int = ord('z') - ord('a') + 1) -> str | List[int]:
    if isinstance(word, str):
        word = [ord(c) - ord('a') for c in word]

    word = [(- a) % mod for a in word]
    return encrypt(text, word, mod)


def list_minus_list(l1: List[int] | str, l2: List[int] | str, mod: int = ord('z') - ord('a') + 1) -> List[int]:
    """
    good for finding the key length and value if given text and its encrypted version
    :param l1: usually the encrypted version
    :param l2: usually the original text
    :param mod: the mod we use (defaults to number of english letters)
    :return: l1 - l2 % mod
    """
    if isinstance(l1, str):
        l1 = l1.lower().replace(' ', '')
        l1 = [ord(c) - ord('a') for c in l1]

    if isinstance(l2, str):
        l2 = l2.lower().replace(' ', '')
        l2 = [ord(c) - ord('a') for c in l2]

    return [(a - b) % mod for a, b in zip(l1, l2)]


def list_to_word(l: List[int]):
    return ''.join([chr(ord('a') + a) for a in l])


if __name__ == '__main__':
    print(encrypt('my name is hod and this is a long sentence', 'hello'))
    print(decrypt('tcylalmdsckeyohomdtghpzyuziyesugp', 'hello'))

    print(list_to_word(list_minus_list('tcylalmdsckeyohomdtghpzyuziyesugp', 'mynameishodandthisisalongsentence')))
