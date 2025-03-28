# Finding Common Elements in Multiple Lists

def common_elements(*lists):
    sets = [set(lst) for lst in lists]
    return set.intersection(*sets)

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
list3 = [5, 6, 7, 8, 9]

print("Common Elements:", common_elements(list1, list2, list3))