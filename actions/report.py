# import os
def build_facility_report(arboretum):
    # os.system('cls' if os.name == 'nt' else 'clear')
    for river in arboretum.rivers:
        print(f'River [{str(river.id)[:8]}] has {len(river.animals)} animals and {len(river.plants)} plants')
        for animal in river.animals:
            print(f'      {animal.species} [{animal.id}]')
        for plant in river.plants:
            print(f'      {plant.species} [{plant.id}]')
    for coastline in arboretum.coastlines:
        print(f'Coastline [{str(coastline.id)[:8]}] has {len(coastline.animals)} animals and {len(coastline.plants)} plants')
        for animal in coastline.animals:
            print(f'      {animal.species} [{animal.id}]')
        for plant in coastline.plants:
            print(f'      {plant.species} [{plant.id}]')
    for forest in arboretum.forests:
        print(f'Forest [{str(forest.id)[:8]}] has {len(forest.animals)} animals and {len(forest.plants)} plants')
        for animal in forest.animals:
            print(f'      {animal.species} [{animal.id}]')
        for plant in forest.plants:
            print(f'      {plant.species} [{plant.id}]')
    for grassland in arboretum.grasslands:
        print(f'Grassland [{str(grassland.id)[:8]}] has {len(grassland.animals)} animals and {len(grassland.plants)} plants')
        for animal in grassland.animals:
            print(f'      {animal.species} [{animal.id}]')
        for plant in grassland.plants:
            print(f'      {plant.species} [{plant.id}]')
    for mountain in arboretum.mountains:
        print(f'Mountain [{str(mountain.id)[:8]}] has {len(mountain.animals)} animals and {len(mountain.plants)} plants')
        for animal in mountain.animals:
            print(f'      {animal.species} [{animal.id}]')
        for plant in mountain.plants:
            print(f'      {plant.species} [{plant.id}]')
    for swamp in arboretum.swamps:
        print(f'Swamp [{str(swamp.id)[:8]}] has {len(swamp.animals)} animals and {len(swamp.plants)} plants')
        for animal in swamp.animals:
            print(f'      {animal.species} [{animal.id}]')
        for plant in swamp.plants:
            print(f'      {plant.species} [{plant.id}]')
    input("\n\nPress any key to continue...")