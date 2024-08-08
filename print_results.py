import oemof.solph as solph
from oemof.solph import views
# import pprint as pp
import matplotlib.pyplot as plt

from restore_and_plot import restore_energy_system


def plot_figures_for(element: dict) -> None:
    figure, axes = plt.subplots(figsize=(10, 5))
    element["sequences"].plot(ax=axes, kind="line", drawstyle="steps-post")
    plt.legend(
        loc="upper center",
        prop={"size": 8},
        bbox_to_anchor=(0.5, 1.25),
        ncol=2,
    )
    figure.subplots_adjust(top=0.8)
    plt.show()


def plot_results(energy_system):
    main_results = energy_system.results['main']
    #pp.pprint(main_results)

    h2_storage = views.node(main_results, 'h2_storage')
    electricity_bus = views.node(main_results, 'electricity')

    plot_figures_for(electricity_bus)


def main():
    h2_hub = restore_energy_system(file_path='U:\\ann82611\\04_Code\\hydrogen_hub\\hydrogen_hub\\h2_hub_dumps')
    plot_results(h2_hub)


if __name__ == "__main__":
    main()
