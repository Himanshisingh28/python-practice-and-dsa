from collections import deque
class Solution(object):
    def valid(self,i ,j, n, m):
        if i<0 or i>=n or j<0 or j>=m:
            return False
        return True

    def orangesRotting(self, grid):
        x = [-1,1,0,0]
        y = [0,0,-1,1]

        n=len(grid)
        m=len(grid[0])
        q=deque()
        fresh=0
        time=0

        for i in range(n):
            for j in range(m):
                if grid[i][j]==2:
                    q.append((i,j))
                    grid[i][j]=-2
                elif grid[i][j]==1:
                    fresh+=1

        while q and fresh>0:
            time+=1
            s=len(q)

            for _ in range(s):
                r,c = q.popleft()
                for k in range(4):
                    row = r + x[k]
                    col = c + y[k]
                    if self.valid(row,col,n,m) and grid [row][col]==1:
                        q.append((row,col))
                        grid[row][col]=-2
                        fresh-=1

        if fresh>0:
            return -1
        return time
      
        