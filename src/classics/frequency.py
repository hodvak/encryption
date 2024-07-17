from typing import List, Dict


def get_frequency(text: str) -> Dict[chr, int]:
    text = text.lower().replace(' ', '')
    res = {chr(c): 0 for c in range(ord('a'), ord('z') + 1)}
    for char in text:
        res[char] += 100/len(text)
    return res
