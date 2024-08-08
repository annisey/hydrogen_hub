import networkx
import matplotlib.pyplot as plt
from oemof.network.graph import create_nx_graph


#plot energy system
def plot_energy_system(energy_system):
    graph = create_nx_graph(energy_system)
    networkx.draw(graph, with_labels=True, font_size=8)
    plt.show()
