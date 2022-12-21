import curses
from curses import wrapper
import time


def main(stdscr):
    stdscr.clear()
    txt = "BİR"
    stdscr.addstr(0, 0, txt)
    stdscr.refresh()
    time.sleep(5)
    stdscr.clear()
    txt = "İKİ"
    stdscr.addstr(0, 0, txt)
    stdscr.refresh()
    stdscr.getch()


wrapper(main)