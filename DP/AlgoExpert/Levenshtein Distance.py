# 2-D DP using Tabulation | O(M * N) and O(M * N)
def levenshteinDistance(str1, str2):
    # Write your code here.
    dp = [[i for i in range(len(str1) + 1)] for j in range(len(str2) + 1)]
    for i in range(1, len(str2) + 1):
        dp[i][0] = dp[i - 1][0] + 1

    for i in range(1, len(str2) + 1):
        for j in range(1, len(str1) + 1):
            if str2[i - 1] == str1[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1])
    return dp[-1][-1]