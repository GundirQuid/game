import operator


class GameBoard:
    def __init__(self, size_x: int = 3, size_y: int = 3):
        """
        :param size_x: integer, size of x-axis, between 3 and 1000
        :param size_y: integer, size of y-axis, between 3 and 1000
        """

        if type(size_x) != int:
            raise TypeError('GameBoard: size_x must be an integer')

        if type(size_y) != int:
            raise TypeError('GameBoard: size_y must be an integer')

        self.x_size = min(max(size_x, 3), 1000)
        self.y_size = min(max(size_y, 3), 1000)

    def get_board_size(self) -> tuple:
        return self.x_size, self.y_size

    def move_location(self, location: tuple, location_change: tuple):
        next_location = tuple(map(operator.add, location, location_change))
        if not self._verify_location(next_location):
            next_location = self._wrap_around_location(location, location_change)

        return next_location

    def _get_board_layout(self) -> list:
        """
        Private Method
        :return: Returns list[x-axis[x, y]]
        """
        x_size, y_size = self.get_board_size()

        # To center x, y at (0, 0)
        x = int(0 - x_size / 2)
        y = int(y_size / 2)
        game_board_list = []
        for _ in range(y_size):
            y_axis_board = []
            for _ in range(x_size):
                y_axis_board.append((x, y))
                x += 1
            game_board_list.append(y_axis_board)
            x = int(0 - x_size / 2)
            y -= 1

        return game_board_list

    def _verify_location(self, location: tuple = None) -> bool:
        """
        Private Method
        :param location: current location (x, y)
        :return: Iterates over each x_axis to see if (x, y) is located, return True if found, else False
        """
        for x_axis in self._get_board_layout():
            if location in x_axis:
                # (x, y) was found
                return True

        # (x, y) was not found
        return False

    def _wrap_around_location(self, location: tuple = None, update_location: tuple = (0, 0)) -> tuple:
        """
        Private Method
        :param location: takes in an Entity location
        :param update_location: go-to location (attempt to go-to but results in wrap-around)
        :return: Returns opposite border location, or initial location
        """
        board_layout = self._get_board_layout()
        initial_x_pos, initial_y_pos = location
        new_x_pos = new_y_pos = 0

        for x_axis in board_layout:
            if location in x_axis:
                # Update X location
                if update_location[0] != 0:

                    if x_axis.index(location) == 0:
                        new_x_pos = x_axis[len(x_axis) - 1][0]

                    elif x_axis.index(location) == len(x_axis) - 1:
                        new_x_pos = x_axis[0][0]

                # Update Y location
                if update_location[1] != 0:
                    if board_layout.index(x_axis) == 0:
                        x_axis_index = x_axis.index(location)
                        new_y_pos = board_layout[len(board_layout) - 1][x_axis_index][1]

                    elif board_layout.index(x_axis) == len(board_layout) - 1:
                        x_axis_index = x_axis.index(location)
                        new_y_pos = board_layout[0][x_axis_index][1]

        if new_x_pos == 0:
            new_x_pos = initial_x_pos + update_location[0]

        if new_y_pos == 0:
            new_y_pos = initial_y_pos + update_location[1]

        return new_x_pos, new_y_pos
