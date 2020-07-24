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


    for index, river in enumerate(arboretum.rivers):
        print(f'{index + 1}. River {river.id}')

    for river in arboretum.rivers:
        for index, animal in enumerate(river.animals):
          if animal.species == "River dolphin":
          print(f'{index + 1}. River Dolphin {animal.id}')
          
    print("Cultivate the plant into which biome?")
    choice = input("> ")

    arboretum.rivers[int(choice) - 1].plants.append(plant)