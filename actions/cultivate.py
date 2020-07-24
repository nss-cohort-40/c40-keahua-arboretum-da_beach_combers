from plants import Blue_Jade_Vine

def cultivate(arboretum):
    plant = None

    print("1. Blue Jade Vine")
    print("2. Mountain Apple Tree")
    print("2. Rainbow Eucalyptus Tree")
    print("2. Silversword")

    choice = input("Choose plant to cultivate > ")

    if choice == "1":
        plant = Blue_Jade_Vine()
        for index, swamp in enumerate(arboretum.swamps):
            print(f'{index + 1}. Swamp {swamp.id}')
          
    print("Cultivate the plant into which biome?")
    choice = input("> ")

    arboretum.swamps[int(choice) - 1].plants.append(plant)
    if choice == "2":
        plant = Mountain_Apple_Tree()
        for index, mountain in enumerate(arboretum.mountains):
            print(f'{index + 1}. Mountain {mountain.id}')
          
    print("Cultivate the plant into which biome?")
    choice = input("> ")

    arboretum.mountains[int(choice) - 1].plants.append(plant)
    if choice == "3":
        plant = Rainbow_Eucalyptus_Tree()
        for index, forest in enumerate(arboretum.forests):
            print(f'{index + 1}. River {forest.id}')
          
    print("Cultivate the plant into which biome?")
    choice = input("> ")

    arboretum.forests[int(choice) - 1].plants.append(plant)
    if choice == "4":
        plant = silversword()
        for index, grassland in enumerate(arboretum.grasslands):
            print(f'{index + 1}. Grassland {grassland.id}')
          
    print("Cultivate the plant into which biome?")
    choice = input("> ")

    arboretum.grasslands[int(choice) - 1].plants.append(plant)
