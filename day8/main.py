grid = open('main.in', 'r').read().splitlines()

grid = [list(map(int, x)) for x in grid]
print(grid)

def is_viewable(row, col):
    if row == 0 or col == 0 or row == len(grid) - 1 or col == len(grid[row]) - 1:
        return True
    found = True
    for top in range(row):
        if grid[top][col] >= grid[row][col]:
            found = False
    if found:
        return True
    found = True
    for bot in range(len(grid) - 1, row, -1):
        if grid[bot][col] >= grid[row][col]:
            found = False            
    if found:
        return True

    found = True
    for left in range(col):
        if grid[row][left] >= grid[row][col]:
            found = False
    if found:
        return True

    found = True
    for right in range(len(grid[0]) - 1, col, -1):
        if grid[row][right] >= grid[row][col]:
            found = False
    if found:
        return True

    return False

def f(row, col):
    rowv = [-1, 0, 1, 0]
    colv = [0, 1, 0, -1]
    ans = []
    for k in range(len(rowv)):
        i,j = row,col
        cur = 0
        while i >= 0 and j >= 0 and i < len(grid) and j < len(grid[row]):
            i += rowv[k]
            j += colv[k]
            if i >= 0 and j >= 0 and i < len(grid) and j < len(grid[row]):
                cur += 1
            if i >= 0 and j >= 0 and i < len(grid) and j < len(grid[row]) and grid[i][j] >= grid[row][col]:
                break
        ans.append(cur)
    ret = 1
    for thing in ans:
        ret *= thing
    #print(row, col, ret)
    return ret

ans=0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        ans = max(ans, f(i,j))
print(ans)
