# Merging and Sorting Two Tuples

def merge_and_sort_tuples(t1, t2):
    merged_tuple = t1 + t2
    sorted_tuple = tuple(sorted(merged_tuple))
    return sorted_tuple

tuple1 = (5, 2, 8)
tuple2 = (3, 7, 1)
result = merge_and_sort_tuples(tuple1, tuple2)
print("Merged and Sorted Tuple:", result)
