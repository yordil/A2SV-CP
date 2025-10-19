class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        row , col = len(grid) , len(grid[0])

        visited = set()

        direction = [(0 , -1) , (-1 , 0) , (0 , 1) , (1 , 0)]

        def inbound(r ,c ):
            return 0 <= r < row and 0<= c < col
        def search(r , c):

            myque = deque([(r ,c)])

            while myque:
                
                r  , c  = myque.popleft()
                

                for nx , ny in direction:
                    nr , nc  = nx + r , c+ ny

                    if inbound(nr , nc) and (nr , nc) not in visited and grid[nr][nc] == "1":
                        myque.append((nr , nc))

                        visited.add((nr , nc))





        island = 0

        for i in range(row):
            for j in range(col):
                if (i , j) not in visited and grid[i][j] == "1":
                    visited.add((i ,j))
                    search(i , j)
                    island +=1

        
        return island 
