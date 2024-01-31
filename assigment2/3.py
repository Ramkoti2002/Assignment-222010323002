def is_palindrome_integer(x):
    # Negative numbers are not palindromic
    if x < 0:
        return 0

    # Calculate the length of the number
    num_digits = 0
    temp_x = x
    while temp_x > 0:
        num_digits += 1
        temp_x //= 10

    # Reverse the second half of the number
    reversed_second_half = 0
    temp_x = x
    for _ in range(num_digits // 2):
        reversed_second_half = reversed_second_half * 10 + temp_x % 10
        temp_x //= 10

    # If the number of digits is odd, skip the middle digit
    if num_digits % 2 == 1:
        temp_x //= 10

    # Compare the reversed second half with the first half
    return temp_x == reversed_second_half

# Example usage:
print(is_palindrome_integer(12121))  # Output: 1
print(is_palindrome_integer(123))    # Output: 0

