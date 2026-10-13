class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[-1 for _ in range(len(text2))] for _ in range(len(text1))]

        def dfs(index1, index2):
            if index1 >= len(text1) or index2 >= len(text2):
                return 0

            if dp[index1][index2] != -1:
                return dp[index1][index2]

            if text1[index1] == text2[index2]:
                dp[index1][index2] = 1 + dfs(index1+1, index2+1)
                return dp[index1][index2]

            skip_from_text1 = dfs(index1 + 1, index2)
            skip_from_text2 = dfs(index1, index2 + 1)

            dp[index1][index2] = max(skip_from_text1, skip_from_text2)
            
            return dp[index1][index2]
        
        dfs(0, 0)

        return max(dp[0])