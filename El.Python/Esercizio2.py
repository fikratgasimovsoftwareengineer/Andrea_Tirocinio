#Set Operations
def set_operations(set1, set2):
    # Calculate the union of the two sets
    union_set = set1.union(set2)
    
    # Calculate the intersection of the two sets
    intersection_set = set1.intersection(set2)
    
    # Calculate the difference (set1 - set2)
    difference_set = set1.difference(set2)
    
    # Return the results as a tuple
    return (union_set, intersection_set, difference_set)

# My values
set1 = {"Physics", "Maths", 3}
set2 = {"Maths", 3, "Yoga"}

result = set_operations(set1, set2)
print(result)  # Output: ({Physics, Maths, 3, Yoga}, {Maths, 3}, {Physics})
