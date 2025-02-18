# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # if not grid:
        #     return 0

        rows=len(grid)
        cols=len(grid[0])
        directions = [[1,0] , [0,1], [0,-1], [-1,0] ]

        islands=0

        def bfs(r,c):
            q=deque()
            grid[r][c]="0"
            q.append((r,c))

            while q:
                row,col=q.popleft()
                for dr, dc in directions:
                    nr= dr + row
                    nc= dc + col
                    if(nr<0 or nc<0 or nr>=rows or nc>=cols or grid[nr][nc]=="0"):
                        continue    
                    q.append((nr,nc))
                    grid[nr][nc]="0"    


        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1":
                    bfs(r,c)
                    islands+=1    

        return islands


#Time & Space Complexity 
#Time complexity: O(m * n) 
#Space complexity: O(m*n) 