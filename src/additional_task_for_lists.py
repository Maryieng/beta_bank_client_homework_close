from operator import mul


def first_and_last_letter(list_strings: list[str]) -> list[str]:
    new_list = []
    for word in list_strings:
        if word == '':
            new_list.append(word)
        elif word[0] == word[-1]:
            new_list.append(word)
    return new_list


def maximum_product(list_numbers: list[int]) -> int:
    sort_list_numbers = sorted(list_numbers)
    return max(mul(*sort_list_numbers[:2]), mul(*sort_list_numbers[-2:]))
