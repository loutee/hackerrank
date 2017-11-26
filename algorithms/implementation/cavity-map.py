#!/bin/python

import sys


n = int(raw_input().strip())
grid = []
grid_i = 0
for grid_i in xrange(n):
    grid_t = list(raw_input().strip())
    grid.append(grid_t)

for i in range(1,n-1):
    for j in range(1,n-1):
        if (grid[i][j] > grid[i][j-1] and grid[i][j] > grid[i][j+1] and grid[i][j] > grid[i-1][j] and grid[i][j] > grid[i+1][j]):
            grid[i][j] = 'X'

for i in xrange(n):
    print(''.join(str(x) for x in grid[i]))
