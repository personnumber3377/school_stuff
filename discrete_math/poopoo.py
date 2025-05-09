from itertools import permutations

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

def count_valid_repairings(n):
    """ Compute the number of valid re-pairings where no original pairs remain together. """
    if n % 2 == 1:
        return 0  # Must be even
    
    people = list(range(n))
    
    # Generate all possible initial pairings
    first_round_pairings = list(all_pairs(people))
    
    valid_rearrangements = 0
    
    # Iterate through each possible initial pairing
    for first_round in first_round_pairings:
        # Generate all derangements of the pairs themselves (i.e., valid reassignments)
        pairs_as_indices = list(range(len(first_round)))
        
        for perm in permutations(pairs_as_indices):
            if all(perm[i] != i for i in range(len(perm))):  # Check if it's a valid derangement
                valid_rearrangements += 1
    
    return valid_rearrangements

# Testing
print(count_valid_repairings(4))  # Expected output: 6
print(count_valid_repairings(6))  # Expected output: 60
print(count_valid_repairings(8))  # Expected output: 2520