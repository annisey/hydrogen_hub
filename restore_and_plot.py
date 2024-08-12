import os
import oemof.solph as solph
from plot_results import plot_results


def restore_energy_system(file_path):
    energy_system = solph.EnergySystem()
    energy_system.restore(file_path, 'h2_hub_dump.oemof')    
    return energy_system


def main():
    relative_path = os.path.join(os.path.dirname(__file__), 'h2_hub_dumps')
    h2_hub = restore_energy_system(file_path=relative_path)
    plot_results(h2_hub) 
    return 0


if __name__ == "__main__":
    main()
