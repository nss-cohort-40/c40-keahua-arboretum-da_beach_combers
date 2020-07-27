from plants import *


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
        environments[int(choice) - 1].add_plant(plant)
    except:
        print(f'error')
        choose_environment(arboretum, plant)

def cultivate(arboretum):
    plant = None

    print("1. Blue Jade Vine")
    print("2. Mountain Apple Tree")
    print("3. Rainbow Eucalyptus Tree")
    print("4. Silversword")

    choice = input("Choose plant to cultivate > ")

    if choice == "1":
        plant = Blue_Jade_Vine()
        
    if choice == "2":
        plant = Mountain_Apple_Tree()
        
    if choice == "3":
        plant = Rainbow_Eucalyptus_Tree()
        
    if choice == "4":
        plant = silversword()

    choose_environment(arboretum, plant)
