import numpy as np


def rules(grid: np.ndarray, i: int,  j: int):
    live_neighbors = 0
    n, m = grid.shape
    for y in range(-1, 2):
        for x in range(-1, 2):
            if y == 0 and x == 0:
                continue
            if i+y < 0 or i+y >= n or j+x < 0 or j+x >= m:
                continue
            if grid[i+y, j+x] == 255:
                live_neighbors += 1

    # Returns an int value that activates or deactivates the life of one pixel in the image
    if grid[i, j] == 255 and (live_neighbors == 2 or live_neighbors == 3):
        return 255
    elif grid[i, j] == 0 and live_neighbors == 3:
        return 255
    return 0


def count_cells(grid: np.ndarray, x_limit: int, y_limit: int):
    quantity = 0
    for x in range(x_limit):
        for y in range(y_limit):

            if grid[x, y] == 255:
                quantity += 1
    return quantity
