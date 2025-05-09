from itertools import combinations, permutations

def all_pairs(lst):
    """ Generate all possible ways to split a list into pairs. """
    if len(lst) < 2:
        yield []
        return
    if len(lst) % 2 == 1:
        return  # Cannot pair an odd number of elements
    a = lst[0]
    for i in range(1, len(lst)):
        pair = (a, lst[i])
        for rest in all_pairs(lst[1:i] + lst[i+1:]):
            yield [pair] + rest

def is_valid_pairing(original, new_pairing):
    """ Check if new_pairing does not contain any original pairs. """
    original_pairs = set(original)
    for pair in new_pairing:
        if pair in original_pairs or tuple(reversed(pair)) in original_pairs:
            return False
    return True

def part_a():
    N = 6
    people = list(range(N))
    
    # Generate all possible initial pairings
    first_round_pairings = list(all_pairs(people))
    
    valid_rearrangements = 0
    
    # Iterate through each possible initial pairing
    for first_round in first_round_pairings:
        # Generate valid second pairings (avoiding previous pairs)
        second_round_pairings = [p for p in all_pairs(people) if is_valid_pairing(first_round, p)]
        
        # The mistake was counting both (A, B), (C, D), (E, F) -> (A, C), (B, E), (D, F)
        # and (A, C), (B, E), (D, F) -> (A, B), (C, D), (E, F) separately
        valid_rearrangements += len(second_round_pairings) // 2  # Avoid double-counting

    print(valid_rearrangements)  # Should print 45
    return valid_rearrangements

part_a()
