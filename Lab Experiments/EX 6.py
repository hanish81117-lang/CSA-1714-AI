
def vacuum_cleaner():
    rooms = {
        'A': 'Dirty',
        'B': 'Dirty'
    }

    location = 'A'

    print("Initial State:", rooms)

    while 'Dirty' in rooms.values():
        print("\nVacuum is in Room", location)

        if rooms[location] == 'Dirty':
            rooms[location] = 'Clean'
            print("Room", location, "is cleaned")
        else:
            print("Room", location, "is already clean")

        if location == 'A':
            location = 'B'
        else:
            location = 'A'

    print("\nAll rooms are clean!")
    print("Final State:", rooms)

vacuum_cleaner()
