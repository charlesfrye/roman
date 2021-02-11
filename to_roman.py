# flake8: noqa
import sys

roman = [
    "I", "V", "X", "L", "C", "D", "M"]

arabic = [
    1, 5, 10, 50, 100, 500, 1000, 5000]

additive_forms = [
    "IIII", "XXXX", "CCCC"]

semiadditive_forms = [
    "VIV", "LXL", "DCD"]

subtractive_forms = [
    "IX", "XC", "CM"]

roman_numerals = {
    numeral: value for numeral, value in zip(roman, arabic)}


def to_roman(k):
    additive_roman = to_additive(k)
    subtractive_roman = to_subtractive(additive_roman)

    return subtractive_roman


def to_additive(k):
    if k < 5:
        return "I" * k

    for letter, last, next in zip(roman[1:], arabic[1:], arabic[2:]):
        if k < next:
            return letter * (k // last) + to_additive(k % last)


def to_subtractive(additive_str):
    semiadditive_str = additive_str
    for semiadditive, additive in zip(semiadditive_forms, additive_forms):
        semiadditive_str = semiadditive_str.replace(additive, semiadditive[1:])

    subtractive_str = semiadditive_str
    for subtractive, semiadditive in zip(subtractive_forms, semiadditive_forms):
        subtractive_str = subtractive_str.replace(semiadditive, subtractive)

    return subtractive_str


if __name__ == "__main__":
    sys.exit(print(to_roman(int(sys.argv[1]))))
