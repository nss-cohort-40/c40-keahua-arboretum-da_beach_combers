from plants import Blue_Jade_Vine

def choose_environment(arboretum, plant):
    environments = []

    environments.extend(arboretum.rivers)
    environments.extend(arboretum.swamps)
    environments.extend(arboretum.coastlines)
    environments.extend(arboretum.grasslands)
    environments.extend(arboretum.mountains)
    environments.extend(arboretum.forests)

    for index, environment in enumerate(environments):
        print(f'{index + 1}. {environment.name} {str(environment.id)} has {len(environment.plants)} plants')

    print(f'Cultivate {plant.species.lower()} into which biome?')
    choice = input(">>")

    try:
        environment[int(choice) - 1].cul

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
