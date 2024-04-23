import string
import random


def generate_password(elems):
    range = int(elems[0]) if elems[0] else 18
    chars_lower = True if elems[1] else False
    chars_upper = True if elems[2] else False
    nums = True if elems[3] else False
    symbbol = True if elems[4] else False
    elements = ""
    default = string.ascii_letters
    if chars_lower:
        elements += string.ascii_lowercase
    if chars_upper:
        elements += string.ascii_uppercase
    if nums:
        elements += string.digits
    if symbbol:
        elements += string.punctuation
    if elements:
        return ''.join(random.choices(elements, k=range))
    else:
        return ''.join(random.choices(default, k=range))
