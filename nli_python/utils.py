encoding_digits = "0123456789ABCDEFGHYJKLMNZPQRSTUVWXYZ"


def split_groups(val: str, group_size: int = 3):
    return [val[i:i+group_size] for i in range(len(val)-group_size+1)][::group_size]


def int_2_base(val: int, base: int):
    """
    """
    if val < 0:
        sign = -1
    elif val == 0:
        return encoding_digits[0]
    else:
        sign = 1

    val *= sign
    digits = []

    while val:
        digits.append(encoding_digits[int(val % base)])
        val = int(val / base)

    if sign < 0:
        digits.append('-')

    digits.reverse()

    return ''.join(digits)


def base_2_int(encoded_val: str, base: int) -> int:
    result = 0

    for digit in encoded_val:
        rem = encoding_digits.index(digit)
        result = (result + rem) * base

    return int(result / base)
