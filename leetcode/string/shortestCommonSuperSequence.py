class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n = len(str1)
        m = len(str2)
        ## Find the longest common subsequence
        dp = [[0 for i in range(m+1)] for j in range(n+1)]
        for i in range(n+1):
            for j in range(m+1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                elif str1[i-1] == str2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        i = n
        j = m
        res = ""
        while i > 0 and j > 0:
            if str1[i-1] == str2[j-1]:
                res = str1[i-1] + res
                i -= 1
                j -= 1
            else:
                if dp[i-1][j] > dp[i][j-1]:
                    res = str1[i-1] + res
                    i -= 1
                else:
                    res = str2[j-1] + res
                    j -= 1
        while i > 0:
            res = str1[i-1] + res
            i -= 1
        while j > 0:
            res = str2[j-1] + res
            j -= 1
        return res
    
#       0	1(A)    2(E)    3(B)    4(D)
# 0   	0	0	    0	    0	    0
# 1(A)	0	1	    1	    1	    1
# 2(B)	0	1	    1	    2	    2
# 3(C)	0	1	    1	    2	    2
# 4(D)	0	1	    1	    2	    3