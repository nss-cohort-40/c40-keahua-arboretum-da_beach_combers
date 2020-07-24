# import os

def build_facility_report(arboretum):
    # os.system('cls' if os.name == 'nt' else 'clear')

    for river in arboretum.rivers:
        print(f'River [{river.id}]')
        for plant in river.plants:
            print(f'   {plant.species} [{plant.id}]')

    input("\n\nPress any key to continue...")