import os
from plants import *


def choose_environment(arboretum, plant, placement):
    environments = []
    if placement == "blue_jade_vine":
        environments.extend(arboretum.grasslands)
        environments.extend(arboretum.swamps)

    if placement == "mountain_apple_tree":
        environments.extend(arboretum.mountains)

    if placement == "rainbow_eucalyptus_tree":
        environments.extend(arboretum.forests)

    if placement == "silversword":
        environments.extend(arboretum.grasslands)

    for index, environment in enumerate(environments):
        print(
            f'{index + 1}. {environment.name} [{str(environment.id)[:8]}] has {len(environment.plants)} plants')
    if len(environments) == 0:
        print('There is no Biome available for this plant!')
        input('Press enter to continue')
    else:
        choice = input(">>")
        print(f'Cultivate {plant.species.lower()} into which biome?')

        try:
            environments[int(choice) - 1].add_plant(plant)
        except:
            print(f'error')
            choose_environment(arboretum, plant)


def cultivate(arboretum):
    os.system('cls' if os.name == 'nt' else 'clear')
    plant = None
    placement = None

    print("1. Blue Jade Vine")
    print("2. Mountain Apple Tree")
    print("3. Rainbow Eucalyptus Tree")
    print("4. Silversword")

    choice = input("Choose plant to cultivate > ")

    if choice == "1":
        plant = Blue_Jade_Vine()
        placement = "blue_jade_vine"
    if choice == "2":
        plant = Mountain_Apple_Tree()
        placement = "mountain_apple_tree"
    if choice == "3":
        plant = Rainbow_Eucalyptus_Tree()
        placement = "rainbow_eucalyptus_tree"
    if choice == "4":
        plant = silversword()
        placement = "silversword"

    choose_environment(arboretum, plant, placement)
