def is_odd(number):
    return number % 2 != 0


def remove_empty_elements(lst):
    while None in lst:
        lst.remove(None)
