# Given a sequence of numbers s. Find the minimal number of elements you need to remove so that the
# sequence becomes increasing. Time O(n2).

# Let dp[i] be the minimum number of elements to be removed to get increasing sequence
# with last element of sequence to be at index i
# Then dp[i] = min(dp[j] + i - j - (a[i] > a[j]) for j = 0..i-1)
# We check all previous results assuming that we delete all elements from j to i-1,
# and maybe ith if it's less or equal than a[j]

*a, = map(int, input().split())
n = len(a)
dp = [0] * n
for i in range(1, n):
    dp[i] = min(dp[j] + i - j - (a[i] > a[j]) for j in range(i))
print(dp[-1])
