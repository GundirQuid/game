class Entity:
    def __init__(self):
        self.y_pos = 0
        self.x_pos = 0

    def get_location(self) -> tuple:
        return self.x_pos, self.y_pos

    def move_axis(self, movement_tuple) -> None:
        self.x_pos += movement_tuple[0]
        self.y_pos += movement_tuple[1]
