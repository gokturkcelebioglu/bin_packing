from algorithm import Algorithm
from read_shapes import read_shapes
import curses
from curses import wrapper

shapes = read_shapes()

def main(stdscr):
    Algorithm(shapes, stdscr)

# TODO: Time counter will be added.
# TODO: Export will be an option.

wrapper(main)