import numpy as np

def main():
    rows, cols = 15, 15
    rowgrid = np.zeros(cols)
    grid = np.repeat(rowgrid, rows, axis=0).reshape(rows, cols)
    # print(grid)
    # bresenham(0, 1, 6, 4, grid)
    # circle(5, 5, 2, grid)
    print(grid)

# note this only works for gradient < 45 deg
# if > 45 deg then swap x and y
def bresenham(x0, y0, x1, y1, grid):
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

def draw_circle(x, y, p, q, grid):
    grid[y + q][x + p] = 1
    grid[y + q][x - p] = 1
    grid[y - q][x + p] = 1
    grid[y - q][x - p] = 1
    grid[y + p][x + q] = 1
    grid[y + p][x - q] = 1
    grid[y - p][x + q] = 1
    grid[y - p][x - q] = 1

def circle(x, y, r, grid):
    p, q = 0, r
    d = 3 - 2 * r
    while p < q:
        draw_circle(x, y, p, q, grid)
        p += 1
        if d < 0:
            d = d + (4 * x) + 6
        else:
            y = y + 1
            d = d + 4 * (x-y) + 10

if __name__ == "__main__":
    main()
