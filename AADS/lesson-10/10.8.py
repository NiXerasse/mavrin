# There are n people in the line for tickets to the concert. Two people standing next in line can
# cooperate, and the one that goes earlier in line will buy two tickets: for oneself and for the next one.
# Person i spends ai seconds to buy one ticket and bi seconds to buy two tickets. How long does it
# take for everyone to buy tickets?

# Let dp[i] be the minimum time needed to buy tickets for people 1..i.
# Then dp[i] = min(
#   We can buy our ticket yourself
#       dp[i - 1] + a[i]
#   We can cooperate with previous person
#       dp[i - 2] + b[i - 1]
# )

*a, = map(int, input().split())
*b, = map(int, input().split())
n = len(a)
dp = [0] * n
dp[0], dp[1] = a[0], min(a[0] + a[1], b[0])
for i in range(2, n):
    dp[i] = min(dp[i - 1] + a[i], dp[i - 2] + b[i - 1])
print(dp[-1])
