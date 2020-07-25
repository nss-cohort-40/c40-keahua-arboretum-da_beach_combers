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

          for index, rDolph in enumerate(arboretum.river_dolphins):
              print(f'{index + 1}. River Dolphin {rDolph.id}')
          choice = input("> ")
          os.system('cls' if os.name == 'nt' else 'clear')
          print(f"What is on the menu for the River Dolphin today?")
          for index, prey in enumerate(rDolph.prey):
            print(f'{index + 1}. {prey}')
          choice = input("> ")
          prey = rDolph.prey[int(choice) - 1] 
          print(rDolph.feed(prey))
          input("\n\nPress enter to continue...")

    if choice == "7":
      pass

    if choice == "8":
      pass
