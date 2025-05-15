from room import Room

class Castle:
    def __init__(self):
        self.rooms = {}

    def add_room(self, room: Room):
        room_id = room.get_id()
        if room_id in self.rooms:
            raise ValueError(f"Room {room_id} already exists in the castle.")
        self.rooms[room_id] = room

    def get_room(self, room_id: int):
        if room_id not in self.rooms:
            raise KeyError(f"Room ID {room_id} not found in the castle.")
        return self.rooms[room_id]

    def change_room(self, room_id: int, new_room: Room):
        if not (1 <= room_id <= 25):
            raise ValueError("Room ID must be between 1 and 25.")
        self.rooms[room_id] = new_room

    def get_entrance_id(self):
        return self._find_room_with_door("entrance")

    def get_exit_id(self):
        return self._find_room_with_door("exit")

    def _find_room_with_door(self, door_type: str):
        for room_id, room in self.rooms.items():
            for direction in ("north", "south", "east", "west"):
                try:
                    if room.get_door(direction) == door_type:
                        return room_id
                except Exception:
                    continue
        raise ValueError(f"No room with a(n) {door_type} door found.")

    def get_next_room(self, room_id: int, door: str):
        current_room = self.get_room(room_id)
        next_room = current_room.get_door(door.lower())

        if next_room in ("entrance", "exit", None):
            return next_room

        while next_room.get_wormhole():
            next_id = next_room.generate_random_room_id()
            next_room = self.get_room(next_id)
            if not next_room.get_wormhole():
                return next_id

        if next_room.get_portal():
            return self.get_entrance_id()

        return next_room.get_id()
