import numpy as np

ORGS_DICTIONATY = pattern = [
    np.array([[0,    255, 255, 0], [255,  0, 0, 255], [0, 255, 255, 0]]),
    np.array([[255, 255], [255, 255]]),
    np.array([[0, 255, 0], [0, 0, 255], [255, 255, 255]]),
    np.array([[0, 255, 255, 0, 0], [255, 255, 255, 255, 0],
             [255, 255, 0, 255, 255], [0, 0, 255, 255, 0]]),
    np.array([[255], [255], [255]]),
    np.array([[0, 255, 255, 255], [255, 255, 255, 0]]),
    np.array([[255, 255, 0, 0], [255, 255, 0, 0],
             [0, 0, 255, 255], [0, 0, 255, 255]]),
    np.array([[0, 255, 255, 0], [255, 0, 0, 255], [0, 255, 0, 255], [
             0, 0, 255, 0]]), np.array([[255, 255, 0], [255, 0, 255], [0, 255, 0]]),
    np.array([[0, 255, 0], [255, 0, 255], [0, 255, 0]])]

ORGS_DICT_STR2INT = {
    "beehive": 0,

    "block": 1,

    "glider": 2,

    "spaceship_4": 3,

    "blinker": 4,

    "toad": 5,

    "beacon": 6,

    "loaf": 7,

    "boat": 8,

    "tub": 9
}


class Organism:
    def __init__(self, type_of_org: int):
        self.__array = ORGS_DICTIONATY[type_of_org]

    def get_array(self):
        return self.__array
