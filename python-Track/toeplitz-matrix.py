class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        n = min(len(matrix) , len(matrix[0]))

        for i in range(1 ,len(matrix)):
            for j in range(1 , len(matrix[0])):
                if j>=i and matrix[i][j] != matrix[0][j-i] or j<=i and matrix[i][j] != matrix[i-j][0]:
                    return False
        return True



