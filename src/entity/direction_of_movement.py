class DirectionOfMovement:
    def __init__(self):
        """
        Direction of movement as follows:
        NW | N | NE
        W  | C | E
        SW | S | SE
        measured in x, y, so north_west = -1 for west, 1 for north, thus (-1, 1)
        """
        self.north_west = (-1, 1)
        self.north = (0, 1)
        self.north_east = (1, 1)
        self.west = (-1, 0)
        self.center = (0, 0)
        self.east = (1, 0)
        self.south_west = (-1, -1)
        self.south = (0, -1)
        self.south_east = (1, -1)

    def all_movement(self):
        """
        Returns a list of all possible movements
        """
        return [self.north_west,
                self.north,
                self.north_east,
                self.west,
                self.center,
                self.east,
                self.south_west,
                self.south,
                self.south_east]

    def x_movement(self):
        """
        Returns a list of all possible movements along the x-axis
        """
        return [self.west,
                self.center,
                self.east]

    def y_movement(self):
        """
        Returns a list of all possible movements along the y-axis
        """
        return [self.north,
                self.center,
                self.south]

    def z_movement(self):
        """
        Returns a list of all possible movements along the z-axis (diagonal)
        """
        return [self.north_west,
                self.north_east,
                self.center,
                self.south_west,
                self.south_east]





