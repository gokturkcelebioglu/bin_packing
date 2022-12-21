import random
from math import exp

from constants import INITIAL_TEMPERATURE, FINAL_TEMPERATURE, COOLING_COEFFICIENT
from export_trays import export_trays
from place_shapes import place_shapes
from swap_shapes import swap_shapes

# Implemantation of simulated annealing
def Algorithm(shapes, stdscr):

    # print_shapes(shapes)
    shapes.sort(key=lambda shape: shape.height, reverse=True)
    # print_shapes(shapes)
    shapes.sort(key=lambda shape: shape.width, reverse=True)
    # print_shapes(shapes)
    
    best_result = place_shapes(shapes)
    neighbour_result = None

    print("First result: ")
    # best_result.print_result()

    temperature = INITIAL_TEMPERATURE
    stdscr.clear()
    stdscr.addstr(0,0,str(temperature))
    stdscr.refresh()

    # delta = 0
    # acceptance_probability = 0
    # random_double = 0

    while(temperature > FINAL_TEMPERATURE):
        swap_shapes(shapes=shapes)
        neighbour_result = place_shapes(shapes)
        # neighbour_result.print_result()

        if(neighbour_result.number_of_trays < best_result.number_of_trays):
            best_result = neighbour_result
            # print("New better result:")
            # best_result.print_result()
        else:
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
        
        temperature = temperature * COOLING_COEFFICIENT
        stdscr.clear()
        stdscr.addstr(0,0, "Current temperature: {} °C".format(str(temperature)))
        stdscr.addstr(1,0, "Best result:" )
        stdscr.addstr(2,0, "Number of trays: {}".format(str(best_result.number_of_trays)))
        stdscr.addstr(3,0, "Number of unused pixels: {}".format(str(best_result.number_of_unused_pixels)))
        stdscr.refresh()

        if best_result.number_of_trays == 7:
            break

    export_trays(best_result.trays, len(shapes))

def print_shapes(shapes):
    print("\n\n")
    for shape in shapes:
        print("{} - {}/{}".format(shape.id, shape.width, shape.height) )
