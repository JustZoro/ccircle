import ccircle


class rooms:
    room = {"name": "Hall"}
    roomName = room["name"]
    rooms = {1: {"name": "hall"}, 2: {"name": "Bedroom"}}


print(rooms)

rooms = {
    1: {"name": "Hall"},
    2: {"name": "Bedroom"},
    3: {"name": "Kitchen"},
    4: {"name": "Bathroom"}
}

rooms = {
    1: {"name": "Hall",
        "east": 2,
        "south": 3},
    2: {"name": "Bedroom",
        "west": 1,
        "south": 4},
    3: {"name": "Kitchen",
        "north": 1},
    4: {"name": "Bathroom",
        "north": 2}

}

def showInstructions():
    print("RPG Game")
    print("========")
    print("Commands")
    print("'go [direction'")