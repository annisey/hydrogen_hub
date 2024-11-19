# Hydrogen Hub Energy System

## Project Overview

This is a simulation model of the hydrogen hub which was carried out wihin milestone M 2.2.2. It integrates various renewable energy sources, storage, electrolyzer and consumption components. Built using the `oemof` (Open Energy Modelling Framework) library, the system models the interactions between photovoltaic (PV) and wind power sources, hydrogen production and storage, and energy demand. The objective is to provide a working tool for further resilience assessment within AB 2.2.


## Installation
### CBC solver
For the optimization of the energy system, solvers are required. Currently, the oemof recommended solver "CBC" is used. For installation instructions, see [here](https://oemof-solph.readthedocs.io/en/stable/readme.html#installing-a-solver).

### Requirements
For running the program several libraries need to be installed, see [here](requirements.txt). <br>
Run the following command:
```
pip install -r requirements.txt
```

## Project Files

### `hydrogen_hub.py`

The `hydrogen_hub.py` script is the core of the project. It defines the energy system, including sources, converter, storage, and sink. The main components are:

- **`main()`**: Coordinates the flow of the program by loading the configuration, creating the energy system, optimizing it, and plotting results.
- **`load_config(file_path)`**: Loads configuration parameters from a YAML file.
- **`get_grid_nominal_value(grid_nominal_value_input)`**: Validates and converts the user's input of the grid nominal value from MW to W, ensuring it's within an acceptable range.
- **`create_energy_system(config)`**: Constructs the energy system based on configuration settings. It adds buses, sources (PV, wind, grid, h2 supply), converter (electrolyzer), storage (h2), and sink (steel mill).
- **`get_csv_data(data_path, column_name)`**: Reads normalized, hourly PV and wind power data over a year from CSV files.
- **`optimizer(energy_system, config)`**: Solves the optimization problem using the specified solver and processes the results.

### `config.yaml`

The `config.yaml` file provides all the configurable parameters for the energy system. It includes paths to data files, nominal values for sources, storage, electrolyzer, and solver settings. This file allows users to adjust inputs without modifying the code:

- **PV and Wind Settings**: File paths and nominal values for PV and wind power.
- **Grid Settings**: Nominal value and variable costs for grid electricity.
- **Hydrogen Ship Source**: Nominal value and variable costs for hydrogen shipping.
- **Electrolyzer Settings**: Nominal value for the electrolyzer.
- **Hydrogen Storage Settings**: Loss rate, capacity, and conversion factors for storage.
- **Solver Settings**: The solver used for optimization (e.g. CBC).

### `restore_hub.py`

The `restore_hub.py` script contains functionality to restore a previously saved energy system state:

- **`restore_energy_system(file_path)`**: Loads an energy system from a saved state. This allows different plot settings for analysis of previously computed results without re-running the entire simulation.

### `plot_results.py`

The `plot_results.py` script focuses on visualizing the results of the simulation:

- **`plot_results(energy_system)`**: Extracts and plots results from the energy system, currently focusing on electricity bus data. But may be adapted to other components as well.
- **`plot_figures_for(element)`**: Helper function for plot_results(). Plots time-series data for given elements such as storage or electricity buses.

### `plot_graph.py`

The `plot_graph.py` script is used to visualize the energy system structure:

- **`plot_energy_system(energy_system)`**: Creates and displays a network graph of the energy system using NetworkX, which provides a graphical representation of the components and their connections.

### `co2_emissions.py`

The `co2_emissions.py` calculates the co2_emissions as they are dependant on the grid supply which is known after the optimization.. 

## Future Enhancements
The simulation model may be further developed to analyze resilience for different scenarios.

