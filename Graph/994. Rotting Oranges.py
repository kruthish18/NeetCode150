from typing import Collection


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        fresh=0
        time=0
        q = Collection.deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    fresh+=1
                if grid[r][c]==2:
                    q.append((r,c))

        directions=[[1,0], [0, -1], [0,1], [-1,0]]
        while fresh>0 and q:
            length = len(q)
            for i in range(length):
                r,c = q.popleft()

                for dr,dc in directions:
                    row = r+ dr
                    col = c + dc
                    if row in range(rows) and col in range(cols) and grid[row][col]==1:
                        q.append((row, col))
                        grid[row][col]=2
                        fresh-=1

            time+=1

        if fresh==0:
            return time
        else:
            return -1        
        

# Time & Space Complexity 
# Time complexity: O ( m ∗ n )
# Space complexity: O ( m ∗ n )
#  Where m is the number of rows and n is the number of columns in the grid.     