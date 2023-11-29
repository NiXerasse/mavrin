# The turtle moves from (0, 0) to (n-1, m-1). On each cell there are some number of flowers. The turtle
# will collect all the flowers that she meets on the way. Find the maximum odd number of flowers
# that she can collect (you cannot skip flowers on the way). Time O(nm).

# Let dp[i][j] be the pair (x, y), where
# x - the maximum odd number of flowers,
# y - the maximum even number of flowers the turtle can collect travelling to cell (i, j).
# Then dp[i][j].x = max(
#                       (dp[i - 1][j].x if f[i][j] % 2 == 0 else dp[i - 1][j].y) + f[i][j],
#                       (dp[i][j - 1].x if f[i][j] % 2 == 0 else dp[i][j - 1].y) + f[i][j]
#                   ),
# Then dp[i][j].y = max(
#                       (dp[i - 1][j].y if f[i][j] % 2 == 0 else dp[i - 1][j].x) + f[i][j],
#                       (dp[i][j - 1].y if f[i][j] % 2 == 0 else dp[i][j - 1].x) + f[i][j]
#                   )

n, m = map(int, input().split())
f = [[0] * (n + 1), *[[0, *map(int, input().split())] for _ in range(m)]]
dp = [[(None, None)] * (n + 1) for _ in range(m + 1)]
dp[1][1] = (f[1][1], None) if f[1][1] % 2 else (None, f[1][1])
for i in range(1, m + 1):
    for j in range(1, n + 1):
        if (i, j) != (1, 1):
            variants = [x + f[i][j] for x in (*dp[i - 1][j], *dp[i][j - 1]) if x is not None]
            max_even = max([x for x in variants if x % 2 == 0], default=None)
            max_odd = max([x for x in variants if x % 2 == 1], default=None)
            dp[i][j] = (max_odd, max_even)
for r in dp:
    print(''.join(str(x).rjust(13) for x in r))
print(dp[m][n][0])
