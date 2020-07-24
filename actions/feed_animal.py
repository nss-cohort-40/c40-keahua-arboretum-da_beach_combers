import os
from animals import RiverDolphin

def feed_animal(arboretum):

    prey = None
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

    if choice == "1":
        pass

    if choice == "2":
        pass

    if choice == "3":
        pass

    if choice == "4":
        pass

    if choice == "5":
        pass

    if choice == "6":

        for river in arboretum.rivers:
          for index, animal in enumerate(river.animals):
            if animal.species == "River dolphin":
              print(f'{index + 1}. River Dolphin {animal.id}')
          choice = input("> ")
          os.system('cls' if os.name == 'nt' else 'clear')
          print(f"What is on the menu for the River Dolphin today?")
          for index, prey in enumerate(animal.prey):
            print(f'{index + 1}. {prey}')
          choice = input("Choose your prey? > ")
          # animal.feed(choice)

          if choice == "1":
            prey = "Salmon"
            animal.feed(prey)
          
          # if choice = "2":
          #   prey = "Sardine"
          #   animal.feed(prey)
          # if choice = "3":
          #   prey = "Trout"
          #   animal.feed(prey)
          # if choice = "4":
          #   prey = "Mackarel"
          #   animal.feed(prey)

    if choice == "7":
      pass

    if choice == "8":
      pass
