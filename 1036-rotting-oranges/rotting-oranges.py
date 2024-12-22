class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        direction=[[0,1],[0,-1],[1,0],[-1,0]]
        rows,cols=len(grid),len(grid[0])
        queue=deque()
        fresh_count=0

        minutes=0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==2:
                    queue.append((i,j))
                if grid[i][j]==1:
                    fresh_count+=1

        while queue and fresh_count>0:
           minutes+=1
           for i in range(len(queue)):
            i,j=queue.popleft()


            for dx,dy in direction:
                x,y=dx+i,dy+j
                if 0<=x<rows and  0<=y<cols and grid[x][y]==1: 
                    fresh_count-=1
                    grid[x][y]=2
                    queue.append((x,y))

        if fresh_count==0:
            return minutes
        else:
            return -1

           



        
        
        
     





