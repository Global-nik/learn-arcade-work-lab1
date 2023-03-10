

class Room:
    def __init__(self, description, north, south, east, west):
        """ """
        self.description = description
        self.north = north
        self.south = south
        self.east = east
        self.west = west


def main():

    current_room = 0
    next_room = 0
    done = False
    room_list = []

# EAST
#0
    room = Room("~~~You are at the INDOOR POOL~~~\nThere is a hallway to your south", None, 1, None, None)
    room_list.append(room)
#1
    room = Room("~~~You are in the NE MAIN HALL~~~\nThere is a door to the north, hallway to the south, "
                "and a door to the west...", 0, 2, None, 6)
    room_list.append(room)
#2
    room = Room("~~~You are in the SE MAIN HALL~~~\nThere is a hallway to the north, a FOYER to the south, "
                "and a door to the west...", 1, 3, None, 7 )
    room_list.append(room)
#3
    room = Room("~~~You are in the FOYER~~~\nThe front porch is south, there is a dining room to your west, "
                "and a hallway to the north...", 2, 4, None, 8)
    room_list.append(room)
#4
    room = Room("~~~Front porch/Outside~~~\n There is a yard due south, and a foyer due north", 3, 5, None, None)
    room_list.append(room)
#NEW
#5
    room = Room("~~~You are in the FRONT YARD~~~, nothing much here but some grass and stuff.... pretty average, it"
                " does have the criss cross grass lines though, so thats a plus...\n There is a porch to the north"
                , 4, None, None, None)
    room_list.append(room)

#MIDDLE
#6
    room = Room("~~~You are in the N COURTYARD~~~\nThere is a hallway to your east and west, and more courtyard "
                "south", None, 7, 1, 11)
    room_list.append(room)
#7
    room = Room("~~~You are in the S COURTYARD~~~\nThere is a hallway to your east and west, and more courtyard "
                "north", 6, None, 2, 12)
    room_list.append(room)
#8
    room = Room("~~~You are in the DINING ROOM~~~\nThere is a foyer to your east, and a kitchen "
                "to your west", None, None, 3, 10)
    room_list.append(room)

#West
#9
    room = Room("~~~You are in the GARAGE~~~\nThere is a door to the north, and the garage door to the south... "
                "you cant open it though...", 10, None, None, None)
    room_list.append(room)
#10
    room = Room("~~~You are in the Kitchen~~~\nThere is a hallway to the north, a door to the south, "
                "and a dining room to the east", 12, 9, 8, None)
    room_list.append(room)
#11
    room = Room("~~~You are in the NW MAIN HALL~~~\nThere is a door to the north, a door to the west, "
                "hallway to the south, and a door to the east...", 13, 12, 6, 14)
    room_list.append(room)
#12
    room = Room("~~~You are in the SW MAIN HALL~~~\nThere is a hallway to the north, a KITCHEN to the south, "
                "and doors to the east and west...", 11, 10, 7, 15)
    room_list.append(room)
#13
    room = Room("~~~You are in the MASTER BEDROOM~~~\nThere is a door to your south and east", None, 11, 17, None)
    room_list.append(room)
#14
    room = Room("~~~You are in the NW BEDROOM~~~\n There is a door to the east, and a door south", None, 16, 11, None)
    room_list.append(room)
#15
    room = Room("~~~You are in the SW BEDROOM~~~\nThere is a door to the east, and a door north", 16, None, 12, None)
    room_list.append(room)
#16
    room = Room("~~~You are in the WEST BEDROOMS BATHROOM~~~\nThere are doors north and south...", 14, 15, None, None)
    room_list.append(room)
#17
    room = Room("~~~You are in the MASTER BATHROOM~~~\nThere is a door to the west...", None, None, None, 13)
    room_list.append(room)


    while not done:
        print(room_list[current_room].description)
        direction = input("Which way would you like to go (N, S, E, W)? \n").lower()



        if direction[0] == 'n':
            next_room = room_list[current_room].north
        elif direction[0] == 's':
            next_room = room_list[current_room].south
        elif direction[0] == 'e':
            next_room = room_list[current_room].east
        elif direction[0] == 'w':
            next_room = room_list[current_room].west
        elif direction[0] == 'q':
            print("Tootles!!")
            break


        else:
            print("North, South, East, or West\n....")
            continue

        if next_room is None:
            print("Yeaaaa... cant go that way bud...\n")
            continue
        current_room = next_room




main()

