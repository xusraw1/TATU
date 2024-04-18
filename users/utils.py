import string
import random


def get_random_symbols():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=10))
