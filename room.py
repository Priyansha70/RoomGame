import random
from diamond import Diamond


class Room:
    def __init__(self, ID=None, north=None, south=None, east=None, west=None,
                 portal=False, wormhole=False, diamond: Diamond = None):
        self.ID = ID
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.portal = portal
        self.wormhole = wormhole
        self.diamond = diamond

    def get_id(self):
        return self.ID

    def set_id(self, ID):
        if not isinstance(ID, int):
            raise TypeError("ID must be an integer.")
        self.ID = ID

    def generate_random_room_id(self):
        if not self.wormhole:
            raise ValueError("No wormhole present in this room.")
        room_id = random.randint(1, 25)
        while room_id == self.ID:
            room_id = random.randint(1, 25)
        return room_id

    def get_portal(self):
        return self.portal

    def get_wormhole(self):
        return self.wormhole

    def get_diamond(self):
        return self.diamond

    def set_portal(self, portal: bool):
        if portal and (self.wormhole or self.diamond):
            raise ValueError("Room cannot be both portal and another type.")
        self.portal = portal

    def set_wormhole(self, wormhole: bool):
        if wormhole and (self.portal or self.diamond):
            raise ValueError("Room cannot be both wormhole and another type.")
        self.wormhole = wormhole

    def set_diamond(self, diamond: Diamond):
        if diamond and (self.portal or self.wormhole):
            raise ValueError("Room cannot have diamond and another type.")
        self.diamond = diamond

    def get_door(self, direction: str):
        direction = direction.lower()
        if direction not in {"north", "south", "east", "west"}:
            raise ValueError("Invalid direction")

        return getattr(self, direction)

    def set_link(self, direction: str, value):
        direction = direction.lower()
        if direction not in {"north", "south", "east", "west"}:
            raise ValueError("Invalid direction")

        if value not in {"entrance", "exit", None} and not isinstance(value, Room):
            raise TypeError("Invalid value for room link")

        setattr(self, direction, value)

    def has_entrance_or_exit(self):
        return any(
            getattr(self, dir) in {"entrance", "exit"}
            for dir in ["north", "south", "east", "west"]
        )
