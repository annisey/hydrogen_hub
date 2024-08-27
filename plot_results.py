from oemof.solph import views
# import pprint as pp
import matplotlib.pyplot as plt


def plot_figures_for(element):
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


def plot_result(energy_system):
    main_results = energy_system.results['main']
    #pp.pprint(main_results)

    h2_storage = views.node(main_results, 'h2_storage')
    electricity_bus = views.node(main_results, 'electricity')

    plot_figures_for(electricity_bus)

    