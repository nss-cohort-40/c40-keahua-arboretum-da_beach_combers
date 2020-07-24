from plants import Blue_Jade_Vine

def cultivate(arboretum):
    plant = None

    print("1. Blue Jade Vine")
    print("2. Dragonfly")

    choice = input("Choose plant to cultivate > ")

    if choice == "1":
        plant = Blue_Jade_Vine()

    if choice == "2":
        pass


    for index, plant in enumerate(arboretum.pl):
        print(f'{index + 1}. River {river.id}')

    print("Cultivate the plant into which biome?")
    choice = input("> ")

    arboretum.plants[int(choice) - 1].plants.append(plant)