def is_odd(number):
    return number % 2 != 0


def remove_duplicate_elements(lst):
    lst.sort()
    element = lst[-1]

    for i in range(len(lst) - 2, -1, -1):
        if element == lst[i]:
            del lst[i]
        else:
            element = lst[i]


def remove_empty_elements(lst):
    while None in lst:
        lst.remove(None)
