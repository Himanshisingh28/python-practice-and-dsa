class Solution(object):
    def searchMatrix(self, matrix, target):
        
        # This is the first way to solve it but not optimized
        # n=len(matrix)
        # m=len(matrix[0])
        # for i in range(0,n):
        #     for j in range(0,m):
        #         if matrix[i][j]==target:
        #             return True
        # return False

        n=len(matrix)
        m=len(matrix[0])
        low=0
        high=n*m-1
        while low<=high:
            guess=(low+high)//2
            row=guess//m
            col=guess%m
            if matrix[row][col]==target:
                return True
            if matrix[row][col]<target:
                low=guess+1
            else:
                high=guess-1
        return False