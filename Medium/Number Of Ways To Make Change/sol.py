# T.C: O(n*d)
# S.C: O(n)
def numberOfWaysToMakeChange(n, denoms):
    ways = [0] * (n+1)
    # There is only 1 way to make $0 i.e use nothing!
    ways[0] = 1
    for coin in denoms:
        for amount in range(1, n+1):
            if coin <= amount:
                ways[amount] += ways[amount - coin]
    return ways[n]

