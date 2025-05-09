import re

def parse_cycles(input_str):
    """Parses input cycle notation and returns a list of cycles as lists of integers."""
    cycles = re.findall(r'\((.*?)\)', input_str)
    return [list(map(int, cycle.split())) for cycle in cycles]

def apply_permutation(cycles):
    """Applies the given cycles to compute the permutation mapping."""
    mapping = {}
    
    # Find all unique numbers in cycles
    all_elements = set(sum(cycles, []))
    
    # Start with identity mapping for all elements
    for elem in all_elements:
        mapping[elem] = elem
    
    # Apply cycles from right to left
    for cycle in reversed(cycles):
        first = cycle[0]
        for i in range(len(cycle) - 1):
            mapping[cycle[i]] = cycle[i + 1]
        mapping[cycle[-1]] = first
    
    return mapping, sorted(all_elements)

def to_two_line_notation(mapping, elements):
    """Generates two-line notation from the mapping."""
    top_row = " ".join(map(str, elements))
    bottom_row = " ".join(map(str, [mapping[k] for k in elements]))
    return f"{top_row}\n{bottom_row}"

def find_disjoint_cycles(mapping, elements):
    """Finds disjoint cycles from the mapping."""
    visited = set()
    cycles = []
    
    for start in elements:
        if start not in visited:
            cycle = []
            x = start
            while x not in visited:
                visited.add(x)
                cycle.append(x)
                x = mapping[x]
            if len(cycle) > 1:
                cycles.append(tuple(cycle))
    
    return cycles

def to_transpositions(cycles):
    """Converts disjoint cycles into a product of transpositions."""
    transpositions = []
    for cycle in cycles:
        for i in range(len(cycle) - 1, 0, -1):
            transpositions.append((cycle[0], cycle[i]))
    return transpositions

def main():
    input_str = input("Enter permutation in cycle notation (e.g. (1362)(2564)(2345)): ")
    cycles = parse_cycles(input_str)
    
    # Apply the permutation
    mapping, elements = apply_permutation(cycles)
    
    # Compute disjoint cycle notation
    disjoint_cycles = find_disjoint_cycles(mapping, elements)
    disjoint_cycle_str = " ".join(f"({ ' '.join(map(str, cycle)) })" for cycle in disjoint_cycles)
    
    # Compute two-line notation
    two_line_str = to_two_line_notation(mapping, elements)
    
    # Compute product of transpositions
    transpositions = to_transpositions(disjoint_cycles)
    transpositions_str = " ".join(f"({a} {b})" for a, b in transpositions)
    
    # Display results
    print("\nDisjoint Cycle Notation:")
    print(disjoint_cycle_str if disjoint_cycle_str else "(Identity permutation)")
    
    print("\nTwo-Line Notation:")
    print(two_line_str)
    
    print("\nProduct of Transpositions:")
    print(transpositions_str if transpositions_str else "(Identity permutation)")

if __name__ == "__main__":
    main()