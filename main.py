from algorithm import Algorithm
from read_shapes import read_shapes
from curses import wrapper

from nf_algorithm import nf_algorithm

shapes = read_shapes()


def main(stdscr):
    nf_algorithm(shapes, stdscr)

# # TODO: Time counter will be added.
# # TODO: Export will be an option.

wrapper(main)