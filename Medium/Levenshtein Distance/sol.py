# Great Explanation: https://www.youtube.com/watch?v=MiqoA-yF-0M

# T.C: O(n*m)
# S.C: O(n*m)
def levenshteinDistance(str1, str2):
    len1, len2 = len(str1), len(str2)
    dp = [ [0 for _ in range(len1 + 1)] for _ in range(len2 + 1)]
    for i in range(len2 + 1):
        dp[i][0] = i
    for j in range(len1 + 1):
        dp[0][j] = j
    for i in range(1, len2 + 1):
        for j in range(1, len1 + 1):
            if str1[j-1] != str2[i-1]:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
            else:
                dp[i][j] = dp[i-1][j-1]
    return dp[len2][len1]


# Space Complexity can be reduced to 2 rows of length min(m,n)
# As, always we are looking value at [i-1, j], [i, j-1], and [i-1, j-1] index

