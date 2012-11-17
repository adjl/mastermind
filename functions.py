def is_odd(number):
    return number % 2 != 0


def remove_empty_elements(lst):
    while None in lst:
        lst.remove(None)


def remove_duplicates(lst):
    lst.sort()
    for i, element in enumerate(lst):
        if element in lst[:i]:
            lst[i] = None
    remove_empty_elements(lst)
