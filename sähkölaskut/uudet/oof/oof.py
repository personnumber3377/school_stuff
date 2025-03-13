import matplotlib.pyplot as plt
import networkx as nx

def draw_sci_fi_energy_device():
    fig, ax = plt.subplots(figsize=(10, 6))
    G = nx.DiGraph()
    
    # Nodes representing different components of the sci-fi energy device
    G.add_nodes_from([
        "Power Core", "Energy Amplifier", "Stabilizer", "Trigger Circuit", "Containment Field", "Discharge Coils", "Final Detonation Module"
    ])
    
    # Edges representing the energy flow
    G.add_edges_from([
        ("Power Core", "Energy Amplifier"),
        ("Energy Amplifier", "Stabilizer"),
        ("Stabilizer", "Trigger Circuit"),
        ("Trigger Circuit", "Containment Field"),
        ("Containment Field", "Discharge Coils"),
        ("Discharge Coils", "Final Detonation Module"),
    ])
    
    pos = {
        "Power Core": (0, 3),
        "Energy Amplifier": (2, 3),
        "Stabilizer": (4, 3),
        "Trigger Circuit": (6, 3),
        "Containment Field": (8, 3),
        "Discharge Coils": (10, 3),
        "Final Detonation Module": (12, 3)
    }
    
    nx.draw(G, pos, with_labels=True, node_size=3000, node_color="lightblue", edge_color="gray", font_size=10, font_weight="bold", ax=ax)
    
    # Annotations for sci-fi tech details
    annotations = {
        "Power Core": "Fusion-based energy source",
        "Energy Amplifier": "Quantum resonance enhancer",
        "Stabilizer": "Field stabilization unit",
        "Trigger Circuit": "High-energy ignition logic",
        "Containment Field": "Plasma containment matrix",
        "Discharge Coils": "Electromagnetic pulse generator",
        "Final Detonation Module": "Controlled energy release"
    }
    
    for node, text in annotations.items():
        x, y = pos[node]
        ax.text(x, y - 0.5, text, fontsize=9, ha='center', bbox=dict(facecolor='white', alpha=0.6, edgecolor='black'))
    
    plt.title("Sci-Fi Energy Explosion Device Schematic")
    plt.show()

# Call function to draw the schematic
draw_sci_fi_energy_device()
