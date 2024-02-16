
            path.add((r,c))
            res =   (dfs(r + 1, c, i + 1) or
                    )
                    dfs(r - 1, c, i + 1) or
                    dfs(r, c - 1, i + 1) or
                    dfs(r, c + 1, i + 1)   
            
                board[r][c] != word[i]): return False
            if (r < 0 or c < 0 or c >= COLS or r >= ROWS or

                (r, c) in path or
                    #4 calls, to the power of length of the word
            path.remove((r,c))
            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0): return True
        
        return False
        




[
