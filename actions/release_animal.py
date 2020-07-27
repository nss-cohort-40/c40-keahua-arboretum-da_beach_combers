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
    if placement == "gecko":
        environments.extend(arboretum.forests)

    if placement == "goose":
        environments.extend(arboretum.grasslands)

    if placement == "kikakapu":
        environments.extend(arboretum.rivers) 
        environments.extend(arboretum.swamps)

    if placement == "opeapea":
        environments.extend(arboretum.forests)
        environments.extend(arboretum.mountains)

    if placement == "pueo":
        environments.extend(arboretum.grasslands)
        environments.extend(arboretum.forests)

    if placement == "river_dolphin":
        environments.extend(arboretum.rivers)
        environments.extend(arboretum.coastlines)
    
    if placement == "spider":
        environments.extend(arboretum.swamps)

    if placement == "ulae":
        environments.extend(arboretum.coastlines)
   
    for index, environment in enumerate(environments):
        print(f'{index + 1}. {environment.name} {[str(environment.id)[:8]]} has {len(environment.animals)} animals')

    print(f"Release {animal.species.lower()} into which biome?")
    choice = input(">")

    try:
        environments[int(choice) - 1].add_animal(animal)
    except IndexError:
        print("Error")
        choose_environment(arboretum, animal, placement)

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
        placement = "goose"

    if choice == "3":
        animal = Kikakapu()
        arboretum.kikakapu.append(animal)
        placement = "kikakapu"

    if choice == "4":
        animal = Opeapea()
        arboretum.opeapea.append(animal)
        placement = "opeapea"

    if choice == "5":
        animal = Pueo()
        arboretum.pueo.append(animal)
        placement = "pueo"

    if choice == "6":
        animal = RiverDolphin()
        arboretum.river_dolphins.append(animal)
        placement = "river_dolphin"

    if choice == "7":
        animal = HappyFaceSpider()
        arboretum.happy_face_spider.append(animal)
        placement = "spider"

    if choice == "8":
        animal = Ulae()
        arboretum.ulae.append(animal)
        placement = "ulae"

    choose_environment(arboretum, animal, placement)
   

