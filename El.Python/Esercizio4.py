#Dictionary lookup
def add_new_entry(myDict, key, value):
    # Add the new key-value pair to the dictionary
    myDict[key] = value
    
    # Return the updated dictionary
    return myDict

# my usage
my_dict = {'Norway': 1, 'Sweden': 2, 'Finland': 3}
key = 'Russia'
value = 4
updated_dict = add_new_entry(my_dict, key, value)
print(updated_dict)  # Output: {'Norway':1,'Sweden':2,'Finland':3,'Russia':4}
