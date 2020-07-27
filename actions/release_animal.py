from animals import *

def choose_environment(arboretum, animal):
    environments = []

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
        environments[int(choice) - 1].add_animal(animal)
    except IndexError:
        print("Error")
        choose_biome(arboretum, animal)

def release_animal(arboretum):

    animal = None

    print("1. Gold Dust Day Gecko")
    print("2. River Dolphin")
    print("3. Nene Goose")
    print("4. Kīkākapu")
    print("5. Pueo")
    print("6. 'Ulae")
    print("7. Ope'ape'a")
    print("8. Happy-Face Spider")
    
    choice = input("Choose animal to release > ")

    try:
        if choice == "1":
            animal = GoldDustDayGecko()

        if choice == "2":
            animal = RiverDolphin()

        if choice == "3":
            animal = NeneGoose()

        if choice == "4":
            animal = Kikakapu()

        if choice == "5":
            animal = Ulae()

        if choice == "6":
            animal = Opeapea()

        if choice == "8":
            animal = HappyFaceSpider()

        choose_environment(arboretum, animal)

    except AttributeError:
        print("error")
        release_animal(arboretum)