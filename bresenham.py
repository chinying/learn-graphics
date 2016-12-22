import numpy as np

def main():
    rows, cols = 10, 10
    rowgrid = np.zeros(cols)
    grid = np.repeat(rowgrid, rows, axis=0).reshape(rows, cols)
    # print(grid)
    bersenham(0, 1, 6, 4, grid)

def bersenham(x0, y0, x1, y1, grid):
    dx = x1 - x0
    dy = y1 - y0
    delta = 2 * dy - dx
    y = y0
    for x in range(x0, x1+1):
        grid[y][x] = 1
        if delta > 0:
            y += 1
            delta -= dx
        delta += dy

    print(grid)

main()
