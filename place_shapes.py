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
        shape = shapes[shapes_index]
        print(shape.id)
        if new_tray == True:
            number_of_trays = number_of_trays + 1
            shapes_index = 0
            new_tray = False
        
        if shape.isPlaced == False:
            tray = try_to_place_the_shape(shape, tray, number_of_placed_shapes, shapes_index)
            if number_of_placed_shapes == len(shapes):
                return Result(number_of_trays, number_of_unused_pixels, shapes)
            elif shapes_index == len(shapes):
                new_tray = True
                number_of_unused_pixels = number_of_unused_pixels + count_number_of_unused_pixels(tray)
                tray = empty_tray()
        else: shapes_index = shapes_index + 1

    return Result(number_of_trays, number_of_unused_pixels, shapes)

def empty_tray():
    tray = []
    for h in range(0,TRAY_HEIGHT):
        tray.append([])
        for w in range(0,TRAY_WIDTH):
            tray[h].append(0)
    return tray

def try_to_place_the_shape(shape, tray, number_of_placed_shapes, shapes_index):
    for h in range(0,TRAY_HEIGHT - shape.height):
        for w in range(0, TRAY_WIDTH - shape.height):
            if(is_shape_placeable(shape, w, h, tray)):
                print("Shape #{} placed in ({},{})".format(shape.id,w,h))
                place_shape(shape, w, h, tray)
                shape.isPlaced = True
                # print_tray(tray)
                number_of_placed_shapes = number_of_placed_shapes + 1
                return tray
    return tray

def is_shape_placeable(shape, x, y, tray):
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

def place_shape(shape, x, y, tray):
    for h in range(0, shape.height):
        for w in range(0, shape.width):
            tray[y+h][x+w] = shape.id
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