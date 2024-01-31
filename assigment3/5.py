def reverse_integer(x):
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31
    
    # Handle the sign of the integer
    sign = 1 if x >= 0 else -1
    x = abs(x)
    
    reversed_x = 0
    
    while x != 0:
        pop = x % 10
        x //= 10
        
        # Check for overflow before updating reversed_x
        if reversed_x > (INT_MAX - pop) // 10:
            return 0
        
        reversed_x = reversed_x * 10 + pop
    
    return sign * reversed_x

# Example usage:
input_1 = 123
output_1 = reverse_integer(input_1)
print(output_1)  # Output: 321

input_2 = -123
output_2 = reverse_integer(input_2)
print(output_2)  # Output: -321

