import sys
import os
from animals import *
from environments import *
from actions import *
from plants import *
from characteristics import *
from arboretum import Arboretum
from actions.annex import annex_habitat
from actions.release_animal import release_animal
from actions.feed_animal import feed_animal
from actions.report import build_facility_report
from actions.cultivate import cultivate
from actions.feed_animal import feed_animal

keahua = Arboretum("Keahua Arboretum", "123 Paukauila Lane")


def build_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('''
    +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+
    |  K  e  a  h  u  a    A  r  b  o  r  e  t  u  m |
    +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+
    ''')
    print("1. Annex Habitat")
    print("2. Release Animal into Habitat")
    print("3. Feed Animal")
    print("4. Add Plant to Habitat")
    print("5. Display Facility Report")
    print("6. Exit")
    print('''
    ''')
    print(f'Choose a KILLER option.')


def main_menu():
    """Show Keahua Action Options
    Arguments: None
    """

    build_menu()
    choice = input(">> ")

    if choice == "1":
        annex_habitat(keahua)

    if choice == "2":
        release_animal(keahua)

    if choice == "3":
        feed_animal(keahua)

    if choice == "4":
        cultivate(keahua)

    if choice == "5":
        build_facility_report(keahua)
        pass

    if choice != "6":
        main_menu()


main_menu()
