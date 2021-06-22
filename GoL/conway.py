"""
conway.py
A simple Python/matplotlib implementation of Conway's Game of Life.
"""

import sys
import argparse
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from Organism import ORGS_DICT_STR2INT, Organism
from json import load
from Rules import rules, count_cells
ON = 255
OFF = 0
vals = [ON, OFF]


def read_config_file(config_doc_name: str):
    with open(config_doc_name, "r") as doc:
        return load(doc)


def add_organism(grid: np.ndarray, array: np.ndarray, start_x: int, start_y: int, limit_x: int, limit_y: int, fig_x: int, fig_y: int):
    " Checking if the figure is not out of range"
    if start_x + fig_x < limit_x:
        if start_y + fig_y < limit_y:
            # Adding every spot of the pattern into the grid
            for i in range(start_x, start_x+fig_x):
                for j in range(start_y, start_y+fig_y):

                    idx = i - start_x
                    idy = j - start_y
                    grid[i, j] = array[idx, idy]


def randomGrid(N):
    """returns a grid of NxN random values"""
    return np.random.choice(vals, N*N, p=[0.2, 0.8]).reshape(N, N)


def update(frameNum, img, grid, N, M):
    # copy grid since we require 8 neighbors for calculation
    # and we go line by line
    newGrid = grid.copy()
    number_cells = count_cells(grid, N, M)
    print("# Number of Cells {}".format(number_cells))
    # TODO: Implement the rules of Conway's Game of Life
    for i in range(N):
        for j in range(M):
            newGrid[i, j] = rules(grid, i, j)
    # update data
    img.set_data(newGrid)
    grid[:] = newGrid[:]
    return img,

# main() function


def main():
    # Command line args are in sys.argv[1], sys.argv[2] ..
    # sys.argv[0] is the script name itself and can be ignored
    # parse arguments
    parser = argparse.ArgumentParser(
        description="Runs Conway's Game of Life system.py.")
    parser.add_argument("--config-file", dest="config_file",
                        default="config1.json", required=True)
    # TODO: add arguments
    config_file = read_config_file(parser.parse_args().config_file)
    # set grid size
    N = config_file["size"]["x"]
    M = config_file["size"]["y"]
    # set animation update interval
    updateInterval = 50

    # declare grid
    grid = np.array([])
    # populate grid with random on/off - more off than on
    grid = randomGrid(N)
    # Uncomment lines to see the "glider" demo
    grid = np.zeros(N*M).reshape(N, M)

    for organism in config_file["organisms"]:

        organism_instance = Organism(
            type_of_org=ORGS_DICT_STR2INT[organism["type"]])
        organism_figure = organism_instance.get_array()

        add_organism(grid=grid, array=organism_figure,
                     start_x=organism["position"]["x"], start_y=organism["position"]["y"], limit_x=N, limit_y=M, fig_x=organism_figure.shape[0], fig_y=organism_figure.shape[1])

    # set up animation
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')
    ani = animation.FuncAnimation(fig, update, fargs=(img, grid, N, M, ),
                                  frames=10,
                                  interval=updateInterval,
                                  save_count=50)

    plt.show()


# call main
if __name__ == '__main__':
    main()
