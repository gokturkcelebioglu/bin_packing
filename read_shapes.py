from classes.shape import Shape

def read_shapes():
    shapes = []

    file = open("shapes.txt", "r")

    for line in file:
        split_line = line.split()
        shapes.append(Shape(id=int(split_line[0]), width=int(split_line[1]), height=int(split_line[2])))

    return shapes