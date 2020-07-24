import os
from environments import River
from environments import Coastline
from environments import Forest
from environments import Grassland
from environments import Mountain
from environments import Swamp


def annex_habitat(arboretum):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("1. River")
    print("2. Costline")
    print("3. Forest")
    print("4. Grassland")
    print("5. Mountain")
    print("6. Swamp")

    choice = input("Choose your habitat > ")

    if choice == "1":
        river = River("River")
        arboretum.rivers.append(river)

    if choice == "2":
        coastline = Coastline("Coastline")
        arboretum.coastlines.append(coastline)

    if choice == "3":
        forest = Forest("Forest")
        arboretum.forests.append(forest)

    if choice == "4":
        grassland = Grassland("Grassland")
        arboretum.grasslands.append(grassland)

    if choice == "5":
        mountain = Mountain("Mountain")
        arboretum.mountains.append(mountain)

    if choice == "6":
        swamp = Swamp("Swamp")
        arboretum.swamps.append(swamp)
