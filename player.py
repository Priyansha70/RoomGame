class Player:
    def __init__(self, player_id: int):
        self.player_id = player_id
        self.position = -1
        self.path = []  # list of (room_id, direction)
        self.diamonds_count = 0

    def __str__(self):
        return f"Player {self.player_id} | Diamonds: {self.diamonds_count}"

    def get_position(self):
        return self.position

    def set_position(self, position):
        if position < 1:
            raise ValueError("Position must be >= 1")
        self.position = position

    def get_player_id(self):
        return self.player_id

    def get_diamonds(self):
        return self.diamonds_count

    def set_diamonds(self, count):
        self.diamonds_count = count

    def print_path(self):
        path_str = " → ".join(f"{room_id}→{direction}" for room_id, direction in self.path)
        print(path_str)

    def add_to_path(self, room_id, direction):
        self.path.append((room_id, direction))
