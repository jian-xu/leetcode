class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        #dfs maybe a good direction
        if not grid:
            return 0
        sum = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '0':
                    continue
                else:
                    sum += 1
                    stack = list()
                    stack.append([i,j])
                    while stack:
                        [p, q] = stack.pop()
                        if p > 0 and grid[p-1][q] == '1':
                            stack.append([p-1, q])
                        if q > 0 and grid[p][q-1] == '1':
                            stack.append([p, q-1])
                        if p < len(grid) - 1 and grid[p+1][q] == '1':
                            stack.append([p+1, q])
                        if q < len(grid[0]) - 1 and grid[p][q+1] == '1':
                            stack.append([p, q+1])
                        grid[p][q] = '0'
        return sum