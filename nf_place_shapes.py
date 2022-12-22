from classes.result import Result
from constants import TRAY_HEIGHT, TRAY_WIDTH

def nf_place_shapes(shapes):
     
    for shape in shapes:
        shape.isPlaced = False

    number_of_trays = 1
    # Result instance

    shapes_index = 0
    number_of_placed_shapes = 0
    trays = []
    
    trays.append(empty_tray())

    while number_of_placed_shapes < len(shapes):
        try:
            shape = shapes[shapes_index]
            for tray in trays:
                for tray_y in range(0,TRAY_HEIGHT - shape.height + 1):
                    for tray_x in range(0,TRAY_WIDTH  - shape.width + 1):
                        if is_shape_placeable(shape, tray_x, tray_y, tray):
                            place_shape(shape, tray_x, tray_y, tray)
                            shape.isPlaced = True
                            number_of_placed_shapes = number_of_placed_shapes + 1
                            shapes_index = shapes_index + 1
                            raise StopIteration
            turn_shape(shape)
            for tray in trays:
                for tray_y in range(0,TRAY_HEIGHT - shape.height + 1):
                    for tray_x in range(0,TRAY_WIDTH  - shape.width + 1):
                        if is_shape_placeable(shape, tray_x, tray_y, tray):
                            place_shape(shape, tray_x, tray_y, tray)
                            shape.isPlaced = True
                            number_of_placed_shapes = number_of_placed_shapes + 1
                            shapes_index = shapes_index + 1
                            print("Shape #{} placed by turning to Tray#{}.".format(shape.id, trays.index(tray) + 1))
                            raise StopIteration

            if shape.isPlaced is False:
                turn_shape(shape)
                print("Shape #{} placed by turning to Tray#{}.".format(shape.id, trays.index(tray) + 1))
                trays.append(empty_tray())
                number_of_trays = number_of_trays + 1
            
        except StopIteration:
            if shape.isPlaced is True:
                print("---> Shape #{} ({}w,{}h) to Tray#{}.".format(shape.id, shape.width, shape.height, trays.index(tray) + 1))

    number_of_unused_pixels = 0
    
    for tray in trays:
        number_of_unused_pixels = number_of_unused_pixels + unused_pixel_counter(tray)

    return Result(number_of_trays, number_of_unused_pixels, shapes, trays)

def is_shape_placeable(shape, tray_x, tray_y, tray):
    for y in range(0, shape.height):
        for x in range(0, shape.width):
            if tray[tray_x + x][tray_y + y ] != 0:
                # print("Shape #{} is not placeable.".format(shape.id))
                return False
    # print("Shape #{} is can be placed in ({},{}).".format(shape.id,section_x,section_y))
    return True

def place_shape(shape, tray_x, tray_y, tray):
    for i in range(0, shape.height):
        for j in range(0, shape.width):
           tray[tray_x + j][tray_y + i] = shape.id
    # print("---> Shape #{} is placed in ({},{}).".format(shape.id,j,i))

def unused_pixel_counter(tray):
    counter = 0
    for tray_y in range(0, TRAY_HEIGHT):
        for tray_x in range(0, TRAY_WIDTH):
            if tray[tray_x][tray_y] == 0:
                counter = counter + 1
    return counter

def empty_tray():
    tray = []
    for tray_x in range(0,TRAY_WIDTH):
        tray.append([])
        for tray_y in range(0,TRAY_HEIGHT):
            tray[tray_x].append(0)
    return tray

def print_tray(tray):
    for y in range(0, TRAY_HEIGHT):
        for x in range(0, TRAY_WIDTH):
            print("{: >4}".format(tray[x][y]), end='')
        print("\n")
    print("\n\n--------------------------------\n")

def turn_shape(shape):
    print("Shape#{} was {}w and {}h.".format(shape.id, shape.width, shape.height))
    temp = shape.width
    shape.width = shape.height
    shape.height = temp
    print("Then it turned and became {}w and {}h.".format(shape.width, shape.height))
    shape.isTurned = not shape.isTurned