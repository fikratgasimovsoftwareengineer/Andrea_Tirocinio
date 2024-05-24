
#List manipulation
def merge_and_sort_lists(list1, list2):
    # Merge the two lists
    merged_list = list1 + list2
    
    # Sort the merged list
    sorted_list = sorted(merged_list)
    
    # Return the sorted list
    return sorted_list

list1 = [3, 1, 4, 7]
list2 = [6, 5, 2, 8]
result = merge_and_sort_lists(list1, list2)
print(result)  # Output: [1, 2, 3, 4, 5, 6, 7, 8]
# Sort ordina una medesima lista mentre sorted ordina creando una nuova lista.
