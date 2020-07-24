def build_facility_report(arboretum):
    for river in arboretum.rivers:
        print(f'River [{river.id}]')
        for animal in river.animals:
            print(f'   {animal.species} [{animal.id}]')

    input("\n\nPress any key to continue...")