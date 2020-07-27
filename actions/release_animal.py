import os
from animals import GoldDustDayGecko
from animals import NeneGoose
from animals import Kikakapu
from animals import Opeapea
from animals import Pueo
from animals import RiverDolphin
from animals import HappyFaceSpider
from animals import Ulae

def choose_environment(arboretum, animal, placement):
    environments = []
    # if placement == "gecko":
    #     environments.extend(arboretum.rivers)
    #     environments.extend(arboretum.coastlines)

    environments.extend(arboretum.rivers)
    environments.extend(arboretum.swamps)
    environments.extend(arboretum.coastlines)
    environments.extend(arboretum.grasslands)
    environments.extend(arboretum.mountains)
    environments.extend(arboretum.forests)

    for index, environment in enumerate(environments):
        print(f'{index + 1}. {environment.name} {str(environment.id)} has {len(environment.animals)} animals')

    print(f"Release {animal.species.lower()} into which biome?")
    choice = input(">")

    try:
            # arboretum.rivers[int(choice) - 1].animals.append(animal)
        environments[int(choice) - 1].add_animal(animal)
    except IndexError:
        print("Error")
        choose_biome(arboretum, animal)

def release_animal(arboretum):
    os.system('cls' if os.name == 'nt' else 'clear')

    animal = None
    placement = None

    print("1. Gold Dust Day Gecko")
    print("2. Nene Goose")
    print("3. Kīkākapu")
    print("4. Ope'ape'a")
    print("5. Pueo")
    print("6. River dolphin")
    print("7. Happy Face Spider")
    print("8. Ulae")
    
    choice = input("Choose animal to release > ")

    if choice == "1":
        animal = GoldDustDayGecko()
        arboretum.gold_dust_day_gecko.append(animal)
        placement = "gecko"
    if choice == "2":
        animal = NeneGoose()
        arboretum.nene_goose.append(animal)

    if choice == "3":
        animal = Kikakapu()
        arboretum.kikakapu.append(animal)

    if choice == "4":
        animal = Opeapea()
        arboretum.opeapea.append(animal)

    if choice == "5":
        animal = Pueo()
        arboretum.pueo.append(animal)

    if choice == "6":
        animal = RiverDolphin()
        arboretum.river_dolphins.append(animal)
        placement = "notrivers"

    if choice == "7":
        animal = HappyFaceSpider()
        arboretum.happy_face_spider.append(animal)

    if choice == "8":
        animal = Ulae()
        arboretum.ulae.append(animal)

    choose_environment(arboretum, animal, placement)
    # for index, river in enumerate(arboretum.rivers):
    #     print(f'{index + 1}. River {river.id}')

    # print("Release the animal into which biome?")
    # choice = input("> ")

    # arboretum.rivers[int(choice) - 1].animals.append(animal)

