# https://www.algoexpert.io/questions/Number%20Of%20Ways%20To%20Traverse%20Graph
# T.C: O(2^(n+m)), watch algo expert video @13:10
# S.C: O(n+m); max recusrion stack height if n+m
def numberOfWaysToTraverseGraph1(width, height):
    if width == 1 or height == 1:
        return 1
    return numberOfWaysToTraverseGraph1(width, height-1) + numberOfWaysToTraverseGraph1(width-1, height)

# T.C: O(n*m)
# S.C: O(n*m)
def numberOfWaysToTraverseGraph2(width, height):
    ways = [[0 for _ in range(width)] for _ in range(height)]
    # Only 1 way to reach
    for i in range(height):
        ways[i][0] = 1
    for j in range(width):
        ways[0][j] = 1
    for i in range(1, height):
        for j in range(1, width):
            ways[i][j] = ways[i-1][j] + ways[i][j-1]
    return ways[height-1][width-1]
