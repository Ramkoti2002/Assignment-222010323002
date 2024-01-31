def repeatedNumber(A):
    n = len(A)
    S = sum(A)  # Sum of all elements in the array
    S_n = n * (n + 1) // 2  # Sum of first n natural numbers
    S_sq = sum(x*x for x in A)  # Sum of squares of all elements in the array
    S_sq_n = (n * (n + 1) * (2 * n + 1)) // 6  # Sum of squares of first n natural numbers
    
    A_minus_B = S - S_n
    A_plus_B = (S_sq - S_sq_n - (S - S_n)**2) // A_minus_B
    
    A = (A_plus_B + A_minus_B) // 2
    B = A - A_minus_B
    
    return [A, B]

input_array = [3, 1, 2, 5, 3]
print(repeatedNumber(input_array))  # Output: [3, 4]
