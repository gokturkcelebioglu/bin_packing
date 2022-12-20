from classes.result import Result
from constants import TRAY_HEIGHT, TRAY_WIDTH

def place_shapes(shapes):
     
    for shape in shapes:
        shape.isPlaced = False

    tray = empty_tray()

    number_of_unused_pixels = 0
    number_of_trays = 0

    shapes_index = 0
    number_of_placed_shapes = 0
    new_tray = True

    while number_of_placed_shapes < len(shapes):
        print("Number of Placed Shapes = {}".format(number_of_placed_shapes))
        shape = shapes[shapes_index]

        if new_tray is True:
            number_of_trays = number_of_trays + 1
            print("New tray created!")
            print("Number of Trays = {}".format(number_of_trays))
            new_tray = False
        
        tray = try_to_place_the_shape(shape, tray, number_of_placed_shapes, shapes_index)
        if number_of_placed_shapes is len(shapes):
            return Result(number_of_trays, number_of_unused_pixels, shapes)
        elif shapes_index == len(shapes):
            new_tray = True
            print_tray(tray)
            number_of_unused_pixels = number_of_unused_pixels + count_number_of_unused_pixels(tray)
            tray = empty_tray()
            shapes_index = 0
        
        while shapes[shapes_index].isPlaced is True:
               shapes_index = shapes_index + 1

def empty_tray():
    tray = []
    for h in range(0,TRAY_HEIGHT):
        tray.append([])
        for w in range(0,TRAY_WIDTH):
            tray[h].append(0)
    return tray

def try_to_place_the_shape(shape, tray, number_of_placed_shapes, shapes_index):
    print("Trying to place Shape #{}".format(shapes_index))
    for tray_y in range(0,TRAY_HEIGHT - shape.height):
        for tray_x in range(0, TRAY_WIDTH - shape.height):
            if is_shape_placeable(shape, tray_x, tray_y, tray):
                print("Shape #{} placed in ({},{})".format(shape.id,tray_x,tray_y))
                place_shape(shape, tray_x, tray_y, tray)
                shape.isPlaced = True
                # print_tray(tray)
                number_of_placed_shapes = number_of_placed_shapes + 1
                return tray
    print("Shape #{} cannot be placed.".format(shapes_index))
    return tray

def is_shape_placeable(shape, x, y, tray):
    print("Shape #{} is placeable.".format(shape.id))
    for h in range(y, TRAY_HEIGHT - shape.height):
        for w in range(x, TRAY_WIDTH - shape.width):
            # print("{} {} {} {}".format(x,y,h,w))
            try:
                if(tray[h][w] != 0):
                    return False
            except:
                print("ERROR! - y/h: {}/{} - x/w: {}/{}".format(y,h,x,w))
                print("Shape ID: {} | isShape Placed: {} | X Coordinate: {} | Y Coordinate: {}".format(shape.id, shape.isPlaced, x, y))
                exit()
                
    return True

def place_shape(shape, tray_x, tray_y, tray):
    for shape_y in range(0, shape.height):
        for shape_x in range(0, shape.width):
            tray[tray_y + shape_y][tray_x + shape_x] = shape.id
    shape.isPlaced = True

def count_number_of_unused_pixels(tray):
    number_of_unused_pixels = 0
    for x in range(0,len(tray)):
        for y in range(0,len(tray[0])):
            if(tray[x,y] == 0):
                number_of_unused_pixels = number_of_unused_pixels + 1
    return number_of_unused_pixels

def print_tray(tray):
    for y in range(0, len(tray)):
        for x in range(0, len(tray[0])):
            print("{: >4}".format(tray[y][x]), end='')
        print("\n")
    print("\n\n--------------------------------\n")