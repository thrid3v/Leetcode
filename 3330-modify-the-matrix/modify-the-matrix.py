class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])

        ans = [row[:] for row in matrix]
                    
        for j in range(n):
            col = max(matrix[i][j] for i in range(m))
            for i in range(m):
                if ans[i][j] == -1:
                    ans[i][j] = col
        
        return ans


        
        