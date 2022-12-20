from classes.result import Result
from constants import TRAY_HEIGHT, TRAY_WIDTH

def place_shapes(shapes):
     
    for shape in shapes:
        shape.isPlaced = False

    tray = empty_tray()

    number_of_unused_pixels = 0
    number_of_trays = 0
    # Result instance

    shapes_index = 0
    tray_x = 0
    tray_y = 0
    number_of_placed_shapes = 0
    new_tray = True
    new_section = True
    is_section_placeable = False

    section_start_position = 0
    section_width = 0

    while number_of_placed_shapes < len(shapes):
        is_section_placeable = False

        if new_tray is True:
            number_of_trays = number_of_trays + 1
            new_section = True
            new_tray = False
            section_start_position = 0

        if new_section is True:
            section_width = shapes[shapes_index].width
            new_section = False

        # shape return
        try:
            for tray_y in range(0, TRAY_HEIGHT - shapes[shapes_index].height + 1):
                for tray_x in range(section_start_position, section_start_position + section_width - shapes[shapes_index].width):
                    print("3")
                    print(is_shape_placeable(shapes[shapes_index], tray_x, tray_y, tray))
                    if is_shape_placeable(shapes[shapes_index], tray_x, tray_y, tray) is True:
                        print("yyyyy")
                        place_shape(shapes[shapes_index], tray_x, tray_y, tray)
                        shapes[shapes_index].isPlaced = True
                        number_of_placed_shapes = number_of_placed_shapes + 1
                        print("---> Now number of placed shapes is {}.".format(number_of_placed_shapes))
                        raise StopIteration
        except StopIteration:
            pass

        if number_of_placed_shapes is len(shapes):
            result =  Result(number_of_trays, number_of_unused_pixels, shapes)
            number_of_unused_pixels = 0
            return result

        try:
            shapes_index = 0
            for shapes_index in range(0, len(shapes)):
                if shapes[shapes_index].isPlaced is False:
                    # tray_x = 0
                    # tray_y = 0
                    for tray_y in range(0, TRAY_HEIGHT - shapes[shapes_index].height):
                        for tray_x in range(section_start_position, section_start_position + section_width - shapes[shapes_index].height):
                            if is_shape_placeable(shapes[shapes_index], tray_x, tray_y, tray):
                                print("xxxxx")
                                is_section_placeable = True
                                raise StopIteration
        except StopIteration:
            pass

        if is_section_placeable is False:
            try:
                new_section = False
                section_start_position = section_start_position + section_width
                if shapes[shapes_index].isPlaced is False:
                    if section_start_position + shapes[shapes_index] <= TRAY_WIDTH:
                        new_section = True
                        raise StopIteration
            except StopIteration:
                pass

            if new_section is False:
                new_tray = True  
                number_of_unused_pixels = number_of_unused_pixels + unused_pixel_counter(tray)
                # print_tray(tray)
                tray = empty_tray()
                shapes_index = 0
                while shapes[shapes_index].isPlaced:
                    shapes_index = shapes_index + 1                  

    return Result(number_of_trays, number_of_unused_pixels, shapes)

def is_shape_placeable(shape, tray_x, tray_y, tray):
    for i in range(0, shape.height):
        for j in range(0, shape.width):
            if tray[tray_x + j][tray_y + i] != 0:
                print("Shape #{} is not placeable.".format(shape.id))
                return False
    print("Shape #{} is placeable.".format(shape.id))
    return True

def place_shape(shape, tray_x, tray_y, tray):
    for i in range(0, shape.height):
        for j in range(0, shape.width):
           tray[tray_x + j][tray_y + i] = shape.id
    print("---> Shape #{} is placed.".format(shape.id))

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
    for y in range(0, len(tray)):
        for x in range(0, len(tray[0])):
            print("{: >4}".format(tray[y][x]), end='')
        print("\n")
    print("\n\n--------------------------------\n")