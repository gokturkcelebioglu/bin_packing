from random import randint

# Changes random two shapes' places
def swap_shapes(shapes):
    random1 = randint(0, len(shapes)-1)
    random2 = randint(0, len(shapes)-1)

    while(random1 == random2):
        random2 = randint(0, len(shapes)-1)

    temp = shapes[random1]
    shapes[random1] = shapes[random2]
    shapes[random2] = temp