import os
from animals import RiverDolphin
import time

def feed_animal(arboretum):
    all_animals = []
    all_animals.extend(arboretum.gold_dust_day_gecko)
    all_animals.extend(arboretum.nene_goose)
    all_animals.extend(arboretum.kikakapu)
    all_animals.extend(arboretum.opeapea)
    all_animals.extend(arboretum.pueo)
    all_animals.extend(arboretum.river_dolphins)
    all_animals.extend(arboretum.happy_face_spider)
    all_animals.extend(arboretum.ulae)

    if len(all_animals) == 0:
        print('There is no animal to feed!')
        input("\n\nPress enter to return to menu...")

    else:

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
          if len(arboretum.gold_dust_day_gecko) == 0:
            print("There is no Gecko to feed!")
            input("\n\nPress enter to return to menu...")

          else:

            for index, gecko in enumerate(arboretum.gold_dust_day_gecko):
              print(f'{index + 1}. Gold Dust Day Gecko [{str(gecko.id)[:8]}]')
            choice = input("> ")
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"What is on the menu for the Gold Dust Day Gecko today?")
            for index, prey in enumerate(gecko.prey):
              print(f'{index + 1}. {prey}')
            choice = input("> ")
            prey = gecko.prey[int(choice) - 1] 
            gecko.feed(prey)

    if choice == "2":
          if len(arboretum.nene_goose) == 0:
            print("There is no goose to feed!")
            input("\n\nPress enter to return to menu...")

          else:

            for index, goose in enumerate(arboretum.nene_goose):
              print(f'{index + 1}. Nene Goose [{str(goose.id)[:8]}]')
            choice = input("> ")
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"What is on the menu for the Nene Goose today?")
            for index, prey in enumerate(goose.prey):
              print(f'{index + 1}. {prey}')
            choice = input("> ")
            prey = goose.prey[int(choice) - 1] 
            goose.feed(prey)

    if choice == "3":

          if len(arboretum.kikakapu) == 0:
            print("There is no Kikakapu to feed!")
            input("\n\nPress enter to return to menu...")

          else:

            for index, kika in enumerate(arboretum.kikakapu):
                print(f'{index + 1}. Kīkākapu [{str(kika.id)[:8]}]')
            choice = input("> ")
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"What is on the menu for the Kīkākapu today?")
            for index, prey in enumerate(kika.prey):
              print(f'{index + 1}. {prey}')
            choice = input("> ")
            prey = kika.prey[int(choice) - 1] 
            kika.feed(prey)

    if choice == "4":

          if len(arboretum.opeapea) == 0:
                print("There is no Opeapea to feed!")
                input("\n\nPress enter to return to menu...")

          else:
              
            for index, ope in enumerate(arboretum.opeapea):
                print(f'{index + 1}. Opeapea [{str(ope.id)[:8]}]')
            choice = input("> ")
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"What is on the menu for the Opeapea today?")
            for index, prey in enumerate(ope.prey):
              print(f'{index + 1}. {prey}')
            choice = input("> ")
            prey = ope.prey[int(choice) - 1] 
            ope.feed(prey)

    if choice == "5":

          if len(arboretum.pueo) == 0:
                print("There is no Pueo to feed!")
                input("\n\nPress enter to return to menu...")

          else:
              
            for index, pue in enumerate(arboretum.pueo):
                print(f'{index + 1}. Pueo {pue.id}')
            choice = input("> ")
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"What is on the menu for the Pueo today?")
            for index, prey in enumerate(pue.prey):
              print(f'{index + 1}. {prey}')
            choice = input("> ")
            prey = pue.prey[int(choice) - 1] 
            pue.feed(prey)

    if choice == "6":

          if len(arboretum.river_dolphins) == 0:
                print("There is no River Dolphin to feed!")
                input("\n\nPress enter to return to menu...")

          else:

            for index, rDolph in enumerate(arboretum.river_dolphins):
                print(f'{index + 1}. River Dolphin [{str(rDolph.id)[:8]}]')
            choice = input("> ")
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"What is on the menu for the River Dolphin today?")
            for index, prey in enumerate(rDolph.prey):
              print(f'{index + 1}. {prey}')
            choice = input("> ")
            prey = rDolph.prey[int(choice) - 1] 
            rDolph.feed(prey)

    if choice == "7":

          if len(arboretum.happy_face_spider) == 0:
                print("There is no Spider to feed!")
                input("\n\nPress enter to return to menu...")

          else:

            for index, spider in enumerate(arboretum.happy_face_spider):
                print(f'{index + 1}. Happy Face Spider {spider.id}')
            choice = input("> ")
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"What is on the menu for the Happy Face Spider today?")
            for index, prey in enumerate(spider.prey):
              print(f'{index + 1}. {prey}')
            choice = input("> ")
            prey = spider.prey[int(choice) - 1] 
            spider.feed(prey)

    if choice == "8":

          if len(arboretum.ulae) == 0:
                print("There is no Ulae to feed!")
                input("\n\nPress enter to return to menu...")

          else:

            for index, ula in enumerate(arboretum.ulae):
                print(f'{index + 1}. Ulae {ula.id}')
            choice = input("> ")
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"What is on the menu for the Ulae today?")
            for index, prey in enumerate(ula.prey):
              print(f'{index + 1}. {prey}')
            choice = input("> ")
            prey = ula.prey[int(choice) - 1] 
            ula.feed(prey)