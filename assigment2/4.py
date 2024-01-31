def majority_element(nums):
    # Initialize variables to keep track of the majority element and its count
    majority_element = nums[0]
    count = 1

    # Traverse the array starting from the second element
    for num in nums[1:]:
        if count == 0:
            # Reset majority element and count if count becomes zero
            majority_element = num
            count = 1
        elif majority_element == num:
            # Increment count if the current element is the majority element
            count += 1
        else:
            # Decrement count if the current element is not the majority element
            count -= 1

    return majority_element

# Example usage:
input_array = [2, 1, 2]
result = majority_element(input_array)
print(result)  # Output: 2

