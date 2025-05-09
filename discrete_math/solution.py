
def fac(N):
    numbers = list(range(1, N+1))
    res = 1
    for i in numbers:
        res *= i
    return res

def check_sol(n, ans): # Produces the correct answer.
    #actual_ans = fac(n)/((2**(n//2)*fac(n//2)))
    actual_ans = actual(n)
    assert actual_ans == ans
    return


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

def part_a(N):
    # N = 6
    people = list(range(N))
    
    # Generate all possible initial pairings
    first_round_pairings = list(all_pairs(people))
    print("first_round_pairings == "+str(first_round_pairings))
    valid_rearrangements = 0
    
    # Iterate through each possible initial pairing
    for first_round in first_round_pairings:
        # Generate all possible second pairings
        second_round_pairings = list(all_pairs(people))
        for second_round in second_round_pairings:
            if is_valid_pairing(first_round, second_round):
                valid_rearrangements += 1
    print(valid_rearrangements)
    return valid_rearrangements

# part_a()

def actual(n):
    return fac(n)//(2**(n//2)*fac(n//2))*(2**(n//2 - 1))   # fac(n)//((2**(n//2)*fac(n//2)))*fac((n//2)) # fac(n)//((2**(n//2)*fac(n//2)))

if __name__=="__main__":
    for N in range(4,1000):
        if N % 2 != 0: # Require even.
            continue
        our_ans = part_a(N)
        print("Our ans: "+str(our_ans))
        actual_ans = actual(N)
        # actual = actual_ans = fac(N)/((2**(n//2)*fac(n//2)))
        print("Actual: "+str(actual_ans))
        check_sol(N, our_ans)

    exit(0)
