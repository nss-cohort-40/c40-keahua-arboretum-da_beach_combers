from plants import blue_jade_vine

def release_plant(arboretum):
    plant = None

    print("1. River Dolphin")
    print("2. Dragonfly")

    choice = input("Choose plant to release > ")

    if choice == "1":
        plant = blue_jade_vine()

    if choice == "2":
        pass


    for index, river in enumerate(arboretum.rivers):
        print(f'{index + 1}. River {river.id}')

    print("Release the plant into which biome?")
    choice = input("> ")

    arboretum.rivers[int(choice) - 1].animals.append(animal)


