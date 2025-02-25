def solve_treasure():
    possibilities = []
    treasure_locations = ['attic', 'cellar', 'porch']
    # Statement (iii): The house is next to a barn is always True.
    house_next_to_barn = True
    
    for treasure in treasure_locations:
        for red_roof in [True, False]:
            for brown_roof in [True, False]:
                # Statement (i): If house next to barn then treasure is not in the attic.
                if house_next_to_barn and treasure == 'attic':
                    continue

                # Statement (ii): If the hut has a red roof then the treasure is in the attic.
                if red_roof and treasure != 'attic':
                    continue

                # Statement (iv): Red roof or treasure is under porch.
                if not (red_roof or treasure == 'porch'):
                    continue

                # Statement (v): If the hut has a brown roof then the treasure is in the cellar.
                if brown_roof and treasure != 'cellar':
                    continue

                possibilities.append({
                    'treasure': treasure,
                    'red_roof': red_roof,
                    'brown_roof': brown_roof,
                    'house_next_to_barn': house_next_to_barn
                })
    return possibilities

result = solve_treasure()
print(result)