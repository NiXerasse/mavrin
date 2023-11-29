# The grasshopper jumps from cell 1 to cell n, jumping 1 or 2 cells forward each time. Each cell has
# a cost. Find the number of different paths of minimum cost. Time O(n).

# Let dp[i] be the number of different paths with minimum cost from cell 1 to cell i.
# Let m[i] be the minimum cost of path from cell 1 to cell i.
# We can get to cell i either from cell i - 1 or from cell i - 2, so the minimum cost at cell i will be
# m[i] = min(m[i - 1], m[i - 2]) + cost[i]
# Now, for dp[i].
# dp[i] = dp[i - 1], if m[i - 1] < m[i - 2]
#         dp[i - 2], if m[i - 2] < m[i - 1],
#         dp[i - 1] + dp[i - 2], if m[i - 1] == m[i - 2]

*cost, = map(int, input().split())
n = len(cost)
dp, m = [1] * n, [0] * n
m[0], m[1] = cost[0], cost[0] + cost[1]
for i in range(2, n):
    m[i] = min(m[i - 1], m[i - 2]) + cost[i]
    dp[i] = dp[i - 1] if m[i - 1] < m[i - 2] \
        else dp[i - 2] if m[i - 2] < m[i - 1] \
        else dp[i - 1] + dp[i - 2]

print(f'Minimum cost: {m[n - 1]}')
print(f'Number of paths with minimum cost: {dp[n - 1]}')
