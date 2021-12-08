class Entity:
    def __init__(self):
        self.y_pos = 0
        self.x_pos = 0

    def get_location(self):
        return self.x_pos, self.y_pos

    def move_y_axis(self, movement_direction):
        self.y_pos += movement_direction

    def move_x_axis(self, movement_direction):
        self.x_pos += movement_direction

    def move_z_axis(self, movement_x_direction, movement_y_direction):
        self.x_pos += movement_x_direction
        self.y_pos += movement_y_direction
