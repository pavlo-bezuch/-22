def remove_duplicates(lst):
    return list(dict.fromkeys(lst))

def sort_list(lst):
    numbers = [x for x in lst if isinstance(x, (int, float))]
    strings = [x for x in lst if isinstance(x, str)]
    numbers.sort()
    strings.sort()
    return numbers + strings

original_list = [1, 2, 3, 4, 5, 6, 3, 4, 5, 7, 6, 5, 4, 3, 4, 5, 4, 3, 'Привіт', 'анаконда']
unique_list = remove_duplicates(original_list)
sorted_list = sort_list(unique_list)

print(sorted_list)
