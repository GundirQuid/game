class DirectionOfMovement:
    def __init__(self):
        """
        Direction of movement as follows:
        NW0 N1 NE2
        W3  C4 E5
        SW6 S7 SE8
        """
        self.north_west = 0
        self.north = 1
        self.north_east = 2
        self.west = 3
        self.center = 4
        self.east = 5
        self.south_west = 6
        self.south = 7
        self.south_east = 8

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





