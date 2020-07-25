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
          for index, gecko in enumerate(arboretum.gold_dust_day_gecko):
              print(f'{index + 1}. Gold Dust Day Gecko {gecko.id}')
          choice = input("> ")
          os.system('cls' if os.name == 'nt' else 'clear')
          print(f"What is on the menu for the Gold Dust Day Gecko today?")
          for index, prey in enumerate(gecko.prey):
            print(f'{index + 1}. {prey}')
          choice = input("> ")
          prey = gecko.prey[int(choice) - 1] 
          gecko.feed(prey)

    if choice == "2":
          for index, goose in enumerate(arboretum.nene_goose):
              print(f'{index + 1}. Nene Goose {goose.id}')
          choice = input("> ")
          os.system('cls' if os.name == 'nt' else 'clear')
          print(f"What is on the menu for the Nene Goose today?")
          for index, prey in enumerate(goose.prey):
            print(f'{index + 1}. {prey}')
          choice = input("> ")
          prey = goose.prey[int(choice) - 1] 
          goose.feed(prey)

    if choice == "3":
          for index, kika in enumerate(arboretum.kikakapu):
              print(f'{index + 1}. Kīkākapu {kika.id}')
          choice = input("> ")
          os.system('cls' if os.name == 'nt' else 'clear')
          print(f"What is on the menu for the Kīkākapu today?")
          for index, prey in enumerate(kika.prey):
            print(f'{index + 1}. {prey}')
          choice = input("> ")
          prey = kika.prey[int(choice) - 1] 
          kika.feed(prey)

    if choice == "4":
          for index, ope in enumerate(arboretum.opeapea):
              print(f'{index + 1}. Opeapea {ope.id}')
          choice = input("> ")
          os.system('cls' if os.name == 'nt' else 'clear')
          print(f"What is on the menu for the Opeapea today?")
          for index, prey in enumerate(ope.prey):
            print(f'{index + 1}. {prey}')
          choice = input("> ")
          prey = ope.prey[int(choice) - 1] 
          ope.feed(prey)

    if choice == "5":
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

          for index, rDolph in enumerate(arboretum.river_dolphins):
              print(f'{index + 1}. River Dolphin {rDolph.id}')
          choice = input("> ")
          os.system('cls' if os.name == 'nt' else 'clear')
          print(f"What is on the menu for the River Dolphin today?")
          for index, prey in enumerate(rDolph.prey):
            print(f'{index + 1}. {prey}')
          choice = input("> ")
          prey = rDolph.prey[int(choice) - 1] 
          rDolph.feed(prey)

    if choice == "7":
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