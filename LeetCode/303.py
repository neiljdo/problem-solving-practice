from typing import List, Tuple


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        deltas = [(-1,0), (1,0), (0,1), (0,-1)]
        islands = 0
        def _bfs(grid: List[List[str]], s: Tuple[int, int]):
            queue = []
            queue.append(s)
            r,c = s
            grid[r][c] = "0"
            
            while queue:
                s = queue.pop()
                r,c = s
                
                for delta in deltas:
                    rr = r+delta[0]
                    cc = c+delta[1]
                    if 0 <= rr < rows and 0 <= cc < cols and grid[rr][cc] == "1":
                        grid[rr][cc] = "0"
                        queue.append((rr,cc))
                print(queue)
                
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    _bfs(grid, (r,c))
                    islands += 1

        return islands



obj = Solution()
print(obj.numIslands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]))
print(obj.numIslands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))
