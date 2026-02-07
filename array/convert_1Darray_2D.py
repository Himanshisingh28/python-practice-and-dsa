class Solution(object):
    def construct2DArray(self, original, m, n):
        if len(original) != m * n:
            return []

        matrix = []
        idx = 0   # pointer for original array

        for i in range(m):
            row = []
            for j in range(n):
                row.append(original[idx])
                idx += 1
            matrix.append(row)

        return matrix
