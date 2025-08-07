def second_largest(numbers):
    # Remove duplicates by converting to a set
    unique_numbers = list(set(numbers))
    
    # Ensure there are at least two unique numbers
    if len(unique_numbers) < 2:
        return None  # Not enough elements to find second largest
    
    # Sort in descending order
    unique_numbers.sort(reverse=True)
    
    # Return second element
    return unique_numbers[1]

# Example list
num_list = [10, 20, 4, 45, 99, 99]

# Find and display second-largest number
second_largest_num = second_largest(num_list)
if second_largest_num is not None:
    print("Second largest number is:", second_largest_num)
else:
    print("List doesn't have enough unique elements.")

# Dictionaries to merge
dict1 = {'a': 100, 'b': 200}
dict2 = {'b': 300, 'c': 400}

# Merge using union operator (Python 3.9+)
merged_dict = dict1 | dict2
print("Merged dictionary:", merged_dict)
