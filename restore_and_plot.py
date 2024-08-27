import oemof.solph as solph
from plot_results import plot_result



def restore_energy_system(file_path):
    energy_system = solph.EnergySystem()
    energy_system.restore(file_path, 'h2_hub_dump.oemof')    
    return energy_system


def main():
    h2_hub = restore_energy_system(file_path='U:\\ann82611\\04_Code\\hydrogen_hub\\hydrogen_hub\\h2_hub_dumps')
    plot_result(h2_hub)


if __name__ == "__main__":
    main()
