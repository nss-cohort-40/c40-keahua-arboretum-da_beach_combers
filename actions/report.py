def build_facility_report(arboretum):
    for river in arboretum.rivers:
        print(f'River [{river.id}]')
        for animal in river.animals:
            print(f'      {animal.species} [{animal.id}]')
        for plant in river.plants:
            print(f'      {plants.species} [{plant.id}]')

    input("\n\nPress any key to continue...")