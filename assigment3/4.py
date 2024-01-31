def convert_to_title(A):
    result = ""
    
    while A > 0:
        result = chr((A - 1) % 26 + ord('A')) + result
        A = (A - 1) // 26
    
    return result

input_1 = 1
output_1 = convert_to_title(input_1)
print(output_1)  # Output: "A"

input_2 = 28
output_2 = convert_to_title(input_2)
print(output_2)  # Output: "AB"

