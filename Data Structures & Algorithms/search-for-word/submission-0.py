class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        visited = set()
        

        def dfs(r, c, i):
            if i == len(word):
                return True

            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[i] or (r, c) in visited:
                return False

            # Choose
            visited.add((r, c))

            # Explore
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if dfs(nr, nc, i + 1):
                    return True

            # Backtrack
            visited.remove((r, c))

            return False

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True

        return False

                    

