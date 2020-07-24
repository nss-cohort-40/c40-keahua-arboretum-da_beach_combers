from plants import blue_jade_vine
from plants import mountain_apple_tree
from plants import rainbow_eucalyptus_tree
from plants import silversword

def release_plant(arboretum):
    plant = None

    print("1. Blue Jade Vine")
    print("2. Mountain Apple Tree")
    print("3. Rainbow Eucalyptus Tree")
    print("4. Silversword")

    choice = input("Add Plant > ")

    if choice == "1":
        plant = blue_jade_vine()

    if choice == "2":
        plant = mountain_apple_tree()

    if choice == "3":
        plant = rainbow_eucalyptus_tree()

    if choice == "4":
        plant = silversword()
   


    for index, environment in enumerate(arboretum.environments):
        print(f'{index + 1}. Environment {environment.id}')

    print("Cultivate the plant into which environment?")
    choice = input("> ")

    arboretum.environments[int(choice) - 1].plant.append(plant)


