#Array Indexing
def find_kernel(array, index):
    # Check if the index is within the bounds of the array
    if 0 <= index < len(array):
        return array[index]
    else:
        return None

# My usage
array = ["Maserati","Defender","Ford","GM","Finmeccanica"]
index = 1
result = find_kernel(array, index)
print(result)  # Output:'Defender'

# Example with out of bounds index
index_out_of_bounds = 5
result_out_of_bounds = find_kernel(array, index_out_of_bounds)
print(result_out_of_bounds)  # Output: None
