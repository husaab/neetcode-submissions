class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        possibilities = [[0 for _ in range(n)] for _ in range(m)]

        def dfs(row, col):
            if row >= m or row < 0 or col >= n or col < 0:
                return 0
            
            if row == m-1 and col == n-1:
                return 1
            
            if possibilities[row][col] > 0:
                return possibilities[row][col]

            paths_going_right = dfs(row, col+1)
            paths_going_down = dfs(row+1, col)

            possibilities[row][col] = (
                paths_going_right + paths_going_down
            )

            return possibilities[row][col]
            
        return dfs(0, 0)

        