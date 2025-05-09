import itertools

def fac(N):
    res = 1
    for i in range(1, N + 1):
        res *= i
    return res

def all_pairs(lst):
    """ Generate all possible ways to split a list into pairs. """
    if len(lst) % 2 == 1:
        return  # Cannot pair an odd number of elements
    
    if len(lst) == 2:
        yield [(lst[0], lst[1])]
        return

    first = lst[0]
    for i in range(1, len(lst)):
        pair = (first, lst[i])
        rest = lst[1:i] + lst[i+1:]
        for sub_pairs in all_pairs(rest):
            yield [pair] + sub_pairs

def is_valid_pairing(original, new_pairing):
    """ Check if new_pairing does not contain any original pairs. """
    original_pairs = set(original)
    for pair in new_pairing:
        if pair in original_pairs or (pair[1], pair[0]) in original_pairs:
            return False
    return True

def part_a(N):
    """ Compute the number of valid re-pairings where no original pairs remain together. """
    people = list(range(N))
    
    # Generate all possible initial pairings
    first_round_pairings = list(all_pairs(people))
    
    valid_rearrangements = 0
    
    # Iterate through each possible initial pairing
    for first_round in first_round_pairings:
        # Generate all possible second pairings
        second_round_pairings = list(all_pairs(people))
        
        # Count valid rearrangements
        for second_round in second_round_pairings:
            if is_valid_pairing(first_round, second_round):
                valid_rearrangements += 1
    
    print(f"Valid rearrangements for N={N}: {valid_rearrangements}")
    return valid_rearrangements

# Testing
print(part_a(4))  # Expected output: 6
print(part_a(6))  # Expected output: 60