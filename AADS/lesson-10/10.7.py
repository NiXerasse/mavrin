# Vasya has a calculator that can perform three operations: add 1, multiply by 2 and multiply by 3.
# What is the smallest number of operations needed to get the number n from the number 1?

# Let dp[i] be the minimum number of operations to get i from 1
# Then dp[i] = min(
#       dp[i - 1] + 1                   Add 1 to i - 1
#       dp[i // 2] + 1 if i % 2 == 0    Multiply i // 2 by 2 if i is even
#       dp[i // 3] + 1 if i % 3 == 0    Multiply i // 3 by 3 if 3 is divider of i
# )

n = int(input())
dp = [0] * (n + 1)
for i in range(2, n + 1):
    dp[i] = min(
        dp[i - 1],
        dp[i // 2] if i % 2 == 0 else dp[i - 1],
        dp[i // 3] if i % 3 == 0 else dp[i - 1]
    ) + 1
print(dp[n])
