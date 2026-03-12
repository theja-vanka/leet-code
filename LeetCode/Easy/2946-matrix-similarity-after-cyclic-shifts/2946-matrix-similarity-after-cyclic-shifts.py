class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        rows: int = len(mat)
        cols: int = len(mat[0])

        k = k % cols

        for i in range(rows):
            if i % 2 == 0:
                shifted = mat[i][k:] + mat[i][:k]
            else:
                shifted = mat[i][-k:] + mat[i][:-k]
        
            if shifted != mat[i]:
                return False
        
        return True