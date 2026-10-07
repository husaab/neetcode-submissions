class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        MAX_ROWS = len(board)
        MAX_COLS = len(board[0])

        visited = set()

        def dfs(row, col, i, visited):
            if i > len(word):
                return False

            if i == len(word):
                return True

            if (row, col) in visited:
                return False

            if row >= MAX_ROWS or row < 0 or col >= MAX_COLS or col < 0:
                return False
            
            if board[row][col] != word[i]:
                return False

            visited.add((row, col))

            found = (
                dfs(row+1, col, i+1, visited) or
                dfs(row-1, col, i+1, visited) or
                dfs(row, col+1, i+1, visited) or
                dfs(row, col-1, i+1, visited)
            )

            visited.remove((row, col))

            return found
            

        for row in range(MAX_ROWS):
            for col in range(MAX_COLS):
                if board[row][col] == word[0]:
                    if dfs(row, col, 0, visited):
                        return True
        
        return False

        
        
