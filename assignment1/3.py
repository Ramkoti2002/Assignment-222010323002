def climbStairs(A):
    if A == 1:
        return 1
    if A == 2:
        return 2
    
    dp = [0] * (A + 1)
    dp[1] = 1  # There's 1 way to reach the first step
    dp[2] = 2  # There are 2 ways to reach the second step
    
    for i in range(3, A + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
        
    return dp[A]

print(climbStairs(2))  # Output: 2

print(climbStairs(3))  # Output: 3
