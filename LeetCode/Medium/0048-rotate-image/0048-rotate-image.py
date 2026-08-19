class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        row, col = len(matrix), len(matrix[0])

        matrix.reverse()
        # now rotate the matrix w.r.t diagonal
        for r in range(row):
            for c in range(r):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

        