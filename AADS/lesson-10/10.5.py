# Alice and Bob are playing a game: n cards are laid out in a row, the number ai is written on the i-th
# card. In one move, you can take one, two or three cards from the right end of the row. The game
# ends when there are no more cards. The winner is the one with the maximum sum of numbers on
# the cards at the end of the game. Who will win if played optimally?

# Let dp[i] be the max sum player can achieve if he takes the card i while playing on deck with cards 1..i.
# It's obvious that other player will get the sum(a[1..i]) - dp[i].
# So, dp[i] = max(
#    We took card a[i], the opponent took card a[i-1],
#       sum(a[1..i-1])-dp[i-1]+a[i] => sum(a[1..i]) - dp[i-1]  My score at i - 1 plus a[i]
#    We took cards a[i-1..i], the opponent took card a[i-2]
#       sum(a[1..i-2])-dp[i-2]+a[i]+a[i-1] => sum(a[1..i]) - dp[i-2] My score at i - 2 plus a[i]+a[i-1]
#   We took cards a[i-2..i], the opponent took card a[i-3]    
#       sum(a[1..i-3])-dp[i-3]+a[i]+a[i-1]+a[i-2] => sum(a[1..i]) - dp[i-3] My score at i - 3 plus a[i]+a[i-1]+a[i-3]
# )
# My implementation is O(n2). Can be easily improved to O(n) by using prefix sums of a[] or something like that.

*a, = map(int, input().split())
n = len(a)
dp = [0] * n
dp[0], dp[1], dp[2] = a[0], a[0] + a[1], a[0] + a[1] + a[2]
for i in range(3, n):
    dp[i] = max(sum(a[:i+1]) - dp[i-j] for j in range(1, 4) if i - j >= 0)

print(dp)
print(f'Alice - {dp[-1]} points.\nBob - {sum(a) - dp[-1]} points.')
