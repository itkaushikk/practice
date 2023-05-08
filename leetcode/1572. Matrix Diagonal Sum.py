class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        no_of_rows = len(mat)
        elements_in_diagonal = []

        for i in range(no_of_rows):
            if i == (no_of_rows-i-1):
                elements_in_diagonal.append(mat[i][i])
            else:
                elements_in_diagonal.append(mat[i][i])
                elements_in_diagonal.append(mat[i][no_of_rows-i-1])
        
        return sum(elements_in_diagonal)
