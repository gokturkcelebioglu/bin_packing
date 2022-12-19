class Result:
    def __init__(self, number_of_trays, number_of_unused_pixels, shape_list):
        self.number_of_trays = number_of_trays
        self.number_of_unused_pixels = number_of_unused_pixels
        self.shape_list = shape_list

    def print_result(self):
        print("New neighbour => Number of trays: {self.number_of_trays},  Number of unused pixels: {self.number_of_unused_pixels}")
