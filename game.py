from castle import Castle
from player import Player
from room import Room
from diamond import Diamond

class Game:
    def __init__(self, player_count:int):
        self.castle= Castle()
        self.Players = []
        self.Finished = []

        for i in range(player_count):
            self.Players.append(Player(i))
            self.Finished.append(False)       

        self.Turn = -1
        
    def initialize_from_file(self, filename):
        file = open(filename,"r")
        lines = file.readlines()
        count = 0
        for line in lines:
            count += 1
            line =line.replace(",\n","\n")
            line = line.rstrip("\n")
            line= line.replace(':',',')
            line = line.rstrip(",")
            line = line.split(", ")

            if count != 1 and count != 2:
                if ( line.__len__()  == 6):
                    category = line[5]
                    if category.__len__() == 1 and category != 'D':
                        if category == 'W':
                            room_obj = self.build_room(int(line[0]),None, False, True)
                            self.castle.add_room(room_obj)
                        elif category == 'P':
                            room_obj = self.build_room(int(line[0]), None, True, False)
                            self.castle.add_room(room_obj)
                    else:
                        diamond_count = category.__len__()
                        diamond_obj = Diamond(diamond_count)
                        room_obj = self.build_room(int(line[0]), diamond_obj, False, False)
                        self.castle.add_room(room_obj)
                else:
                    room_obj = self.build_room(int(line[0]), None, False, False)
                    self.castle.add_room(room_obj)

        file.close()
        file = open(filename,"r")
        lines2 = file.readlines()
        count2 = 0
        entrance_room_no = '0'
        exit_room_no = '0'
        entrance_door = 'N'
        exit_door = 'N'
        for line in lines2:
            count2 += 1
            line = line.replace(",\n","\n")
            line = line.rstrip("\n")
            line = line.replace(':',',')
            line = line.rstrip(",")
            line = line.split(", ")

            if(count2 == 1):
                entrance_room_no = line[1]
                entrance_door = line[2]
            elif count2 == 2:
                exit_room_no = line[1]
                exit_door = line[2]
            else:
                north_room, south_room, east_room , west_room = None, None, None , None
                north = line[1]
                south = line[2]
                east = line[3]
                west = line[4]
                if line[0] == entrance_room_no:
                    if entrance_door == 'N':
                        north = 'entrance'
                        north_room = 'entrance'
                    elif entrance_door == 'S':
                        south = 'entrance'
                        south_room = 'entrance'
                    elif entrance_door == 'E':
                        east = 'entrance'
                        east_room = 'entrance'
                    elif entrance_door == 'W':
                        west = 'entrance'
                        west_room = 'entrance'
                elif line[0] == exit_room_no:
                    if exit_door == 'N':
                        north = 'exit'
                        north_room = 'exit'
                    if exit_door == 'S':
                        south = 'exit'
                        south_room = 'exit'
                    if exit_door == 'E':
                        east = 'exit'
                        east_room = 'exit'
                    if exit_door == 'W':
                        west = 'exit'
                        west_room = 'exit'
                if not(isinstance(north_room, str)):
                    if north == '0':
                        north_room = None
                    else:
                        north_room = self.castle.get_room(int(north))
                if not(isinstance(south_room, str)):
                    if south == '0':
                        south_room = None
                    else:
                        south_room = self.castle.get_room(int(south))
                if not(isinstance(east_room, str)):
                    if east == '0':
                        east_room = None
                    else:
                        east_room = self.castle.get_room(int(east))
                if not(isinstance(west_room, str)):
                    if west == '0':
                        west_room = None
                    else:
                        west_room = self.castle.get_room(int(west))

                cur_room = self.castle.get_room(int(line[0]))
                cur_room.set_link("north", north_room)
                cur_room.set_link("south", south_room)
                cur_room.set_link("east", east_room)
                cur_room.set_link("west", west_room)

        for player in self.Players:
            player.set_position(self.castle.get_entrance_id())
            room = self.castle.get_room(self.castle.get_entrance_id())

            if room.get_door("north") == "entrance":    
                player.add_to_path(self.castle.get_entrance_id(), "North")
            elif room.get_door("south") == "entrance":
                player.add_to_path(self.castle.get_entrance_id(), "South")
            elif room.get_door("east") == "entrance":
                player.add_to_path(self.castle.get_entrance_id(), "East")
            elif room.get_door("west") == "entrance":
                player.add_to_path(self.castle.get_entrance_id(), "West")


    def get_turn(self):
        return self.Turn
    
    def set_turn(self, turn):
        self.Turn = turn
    
    def get_player(self, player_id):
        return self.Players[ player_id ]
    
    def build_room(self, room_id, diamond, portal, wormhole):
        room_object = Room(ID= room_id, portal=portal, wormhole=wormhole, diamond=diamond)
        return room_object

    def move(self):
        user_response = input(f"Player: {self.Turn} Enter the direction where you want to move: ")
        cur_player = self.Players[self.Turn]
        room_id = self.castle.get_next_room(cur_player.get_position(),user_response)
        if room_id == "exit":
            self.Finished[self.Turn] = True
        else:
            cur_player.set_position(room_id)
            cur_player.add_to_path(room_id, user_response.capitalize())
            room = self.castle.get_room(room_id)
            dimaond_obj = room.get_diamond()
            if( dimaond_obj != None ):
                self.update_diamonds()

    def is_finished(self):
        for entry in self.Finished:
            if entry == False:
                return False
        return True

    def update_diamonds(self):
        cur_player = self.Players[self.Turn]
        cur_diamonds = cur_player.get_diamonds()

        cur_room = self.castle.get_room(cur_player.get_position())
        room_diamonds = cur_room.get_diamond().get_diamonds()
        
        final_count =  cur_diamonds + room_diamonds
        cur_player.set_diamonds(final_count)
        
        cur_room.get_diamond().set_diamonds(0)
