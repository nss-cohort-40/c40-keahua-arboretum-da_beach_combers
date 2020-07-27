from animals import *
import os

def feed_animal(arboretum):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("1. Gold Dust Day Gecko")
    print("2. Nene Goose")
    print("3. Kīkākapu")
    print("4. Ope'ape'a")
    print("5. Pueo")
    print("6. River dolphin")
    print("7. Happy Face Spider")
    print("8. Ulae")

    choice = input("Choose animal to feed. > ")

    selected_animal_list = []

    environments = [arboretum.coastlines, arboretum.forests, arboretum.grasslands, arboretum.mountains, arboretum.rivers, arboretum.swamps]

    def animal_list(selected_animal):
      for environment in environments:
        for habitat in environment:
          for animal in habitat.animals:
            if isinstance(animal, selected_animal):
              selected_animal_list.append(animal)
      


    if choice == "1":
      animal_list(GoldDustDayGecko)

    if choice == "2":
      animal_list(NeneGoose)

    if choice == "3":
      animal_list(Kikakapu)

    if choice == "4":
      animal_list(Opeapea)

    if choice == "5":
      animal_list(Pueo)

    if choice == "6":
      animal_list(RiverDolphin)

    if choice == "7":
      animal_list(HappyFaceSpider)
    
    if choice == "8":
      animal_list(Ulae)

    for index, animal in enumerate(selected_animal_list):
      print(f'{index + 1}. {animal}')
    print(f'Choose an animal:')
    choice = input(">> ")
    chosen = selected_animal_list[int(choice) -1]
    foods = list(chosen.prey)

    for index, food in enumerate(foods):
      print(f'{index +1}. {food}')
    picked_food = input('>> ')
    animal.feed(foods[int(picked_food) -1])
    input('Press enter to return to main menu\n')