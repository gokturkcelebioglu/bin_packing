import random
from math import exp

from constants import INITIAL_TEMPERATURE, FINAL_TEMPERATURE, COOLING_COEFFICIENT, TRAY_HEIGHT, TRAY_WIDTH
from export_trays import export_trays
from nf_place_shapes import nf_place_shapes
from swap_shapes import swap_shapes

# Implemantation of simulated annealing
def nf_algorithm(shapes, stdscr):

    # print_shapes(shapes)
    shapes.sort(key=lambda shape: shape.height, reverse=True)
    # print_shapes(shapes)
    shapes.sort(key=lambda shape: shape.width, reverse=True)
    # print_shapes(shapes)
    
    best_result = nf_place_shapes(shapes)

    neighbour_result = None

    temperature = INITIAL_TEMPERATURE

    delta = 0
    acceptance_probability = 0
    random_double = 0

    # The minimum size of used area will be the sum of areas of all shapes. If we divide this sum to area of one tray, we arrive the minimum number of trays. 
    sum = 0
    for shape in shapes:
        sum = sum + shape.width * shape.height
    finish_condition_min_tray = round(sum/(TRAY_HEIGHT*TRAY_WIDTH))

    while(temperature > FINAL_TEMPERATURE):
        swap_shapes(shapes)
        neighbour_result = nf_place_shapes(shapes)
        # neighbour_result.print_result()

        if(neighbour_result.number_of_unused_pixels <= best_result.number_of_unused_pixels):
            best_result = neighbour_result
            # print("New better result:")
            # best_result.print_result()
        else:
            delta = neighbour_result.number_of_unused_pixels - best_result.number_of_unused_pixels
            acceptance_probability = exp(-delta/temperature)
            random_double = random.random()
            if(random_double < acceptance_probability):
                best_result = neighbour_result
                # print("New better result:")
                    # best_result.print_result()

        if best_result.number_of_trays == finish_condition_min_tray:
            break

        temperature = temperature * COOLING_COEFFICIENT
        stdscr.clear()
        stdscr.addstr(0,0, "Current temperature: {} °C".format(str(temperature)))
        stdscr.addstr(1,0, "Best result:" )
        stdscr.addstr(2,0, "Number of trays: {}".format(str(best_result.number_of_trays)))
        stdscr.addstr(3,0, "Number of unused pixels: {}".format(str(best_result.number_of_unused_pixels)))
        stdscr.refresh()

    stdscr.addstr(4,0, "------------------------------------------------------------------")
    if best_result.number_of_trays == finish_condition_min_tray:
        stdscr.addstr(5,0, "Program finished by arriving to amount of minimum trays.")
    else:
        stdscr.addstr(5,0, "Program finished by arriving to final temperature.")

    stdscr.addstr(6,0, "Best result:" )
    stdscr.addstr(7,0, "Number of trays: {}".format(str(best_result.number_of_trays)))
    stdscr.addstr(8,0, "Number of unused pixels: {}".format(str(best_result.number_of_unused_pixels)))
    stdscr.refresh()

    export_trays(best_result.trays, len(shapes))

# def print_shapes(shapes):
#     print("\n\n")
#     for shape in shapes:
#         print("{} - {}/{}".format(shape.id, shape.width, shape.height) )
