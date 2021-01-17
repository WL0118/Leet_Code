from collections import deque
import numpy as np
class Solution(object):


        
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        grid = np.array(grid)
        n, m = grid.shape
        #print(n,m)
        
        dx = [1,1,0,-1,1]
        dy = [1,0,1,1,-1]
        
        queue = deque()
        if(n==1 and m==1 and grid[n-1][m-1]==0):
            return 1
        if(grid[0][0]==1):
            return -1

        queue.append((0,0))

        while queue:
            x, y = queue.popleft()
            for i in range(5):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if grid[nx][ny]!=0:
                    continue
                if grid[nx][ny]==0:
                    grid[nx][ny] = grid[x][y]+1
                    queue.append((nx,ny))
                    #print(nx,ny,grid[nx][ny])
                    if nx==n-1 and ny == m-1:
                        return grid[x][y]+2

        return -1
            
        


                
                
                
                
                
                
                
                