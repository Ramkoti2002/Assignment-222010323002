def plus_one(digits):
    n = len(digits)

    for i in range(n - 1, -1, -1):
        digits[i] += 1

        if digits[i] < 10:
            return digits
        else:
            digits[i] = 0

    digits.insert(0, 1)

    return digits

input1 = [1, 2, 3]
output1 = plus_one(input1)
print(output1)  # Output: [1, 2, 4]

