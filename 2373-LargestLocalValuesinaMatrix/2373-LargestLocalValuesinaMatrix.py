        res = [[0]*(n-2) for _ in range(n-2)]
        for i in range(n-2):
            for j in range(n-2):
                res[i][j] = max(grid[ii][jj] for ii in range(i, i + 3) for jj 
in range(j, j+3))

        return res
[[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]
