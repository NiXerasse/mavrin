# The grasshopper jumps from cell 1 to cell n, 1 or 2 cells forward each time. Each cell has a letter
# written on it. Find such a path so that the string read by the grasshopper is lexicographically
# minimal. Time O(n2).

# Let dp[i] be the lexicographically minimum path.
# Then dp[i] = min(dp[i - 1] + c[i], dp[i - 2] + c[i])
# Note that dp[i] = min(dp[i - 1], dp[i - 2])  + c[i] won't work.
# Example: 'act' -> min('a', 'ac') + 't' = 'at', but min('a' + 't', 'ac' + 't') = 'act'

*c, = input()
n = len(c)
dp = [''] * n
dp[0], dp[1] = c[0], c[0] + c[1]
for i in range(2, n):
    dp[i] = min(dp[i - 1] + c[i], dp[i - 2] + c[i])

print(dp[n - 1])
