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

    def food_list(animal):
        print(animal)
        i = 1
        for snack in animal.prey:
             print(f'{i}. {snack}')
             i+=1

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
      food_list(RiverDolphin)

    if choice == "7":
      pass
    
    if choice == "8":
      pass
    