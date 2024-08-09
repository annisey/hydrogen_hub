import oemof.solph as solph
from oemof.solph.components import Sink, Source, Converter, GenericStorage
from oemof.solph import create_time_index, Bus, Flow, Model, processing

#for plotting
from plot_graph import plot_energy_system
# import pprint as pp
from print_results import plot_results
 
#for config file and opening data
import yaml
import pandas as pd


#load config file (where parameters are set)
def load_config(file_path):
    with open(file_path, 'r') as file:
        config = yaml.safe_load(file)
    return config


def get_csv_data(data_path, column_name):
    df = pd.read_csv(data_path)
    fixed_value = df[column_name]
    return fixed_value


def create_energy_system(config):

    index = create_time_index(2023) #range of a year, hourly

    #create system
    h2_hub = solph.EnergySystem(timeindex=index, infer_last_interval=False) #einlesen ob infer_last_interval true or false

    #add buses
    electricity_bus = Bus(label='electricity') #, inputs, outputs
    h2_to_storage_bus = Bus(label='h2_to_storage') #inputs, outputs to add
    h2_to_production_bus = Bus(label='h2_to_production') #, inputs, outputs

    h2_hub.add(electricity_bus, h2_to_production_bus, h2_to_storage_bus)

    #open and get data from csv
    #pfad übergeben und Spaltenname für normed fixed value (Flow) (eingegeben im Config file)
    pv_data = get_csv_data(config['pv_data_path'], config['pv_data_column']) 
    wind_data = get_csv_data(config['wind_data_path'], config['wind_data_column'])

    #add sources
    pv_source = Source(label='pv', outputs={electricity_bus: Flow(fix=pv_data, nominal_value=config['pv_nominal_value'])}) # 5MW (?)
    wind_source = Source(label='wind', outputs={electricity_bus: Flow(fix=wind_data, nominal_value=config['wind_nominal_value'])}) #10MW (?) 
    grid_source = Source(label='grid', outputs={electricity_bus: Flow(fix=1, nominal_value=100000000)}) #100MW (?)

    h2_ship_source = Source(label='h2_ship', outputs={h2_to_storage_bus: Flow(fix=1, nominal_value=500, variable_costs=50)}) # Einheit check
    electrolyzer = Converter(label='electrolyzer', inputs={electricity_bus: Flow(fix=1, nominal_value=50000000)},outputs={h2_to_storage_bus: Flow()}, conversion_factors={h2_to_storage_bus: 0.25}) #conversion factor and Flow tbd

    h2_hub.add(pv_source, wind_source, grid_source, h2_ship_source, electrolyzer)

    #add storage
    h2_storage = GenericStorage(label= 'h2_storage', inputs={h2_to_storage_bus: Flow()},outputs={h2_to_production_bus: Flow()},
                                loss_rate=0.001, nominal_storage_capacity=200,inflow_conversion_factor=0.98, outflow_conversion_factor=0.8) #parameters tbd

    h2_hub.add(h2_storage)

    #add sink
    steel_mill = Sink(label='steel_mill', inputs={h2_to_production_bus: Flow(), electricity_bus: Flow()})

    h2_hub.add(steel_mill)

    return h2_hub


def optimizer(energy_system, config):
    model = Model(energy_system)
    model.solve(solver=config['solver']) # "solve_kwargs={'tee': True}" to display solver's output
    #main results contain data of each component and flow in energy system
    #processing.results function gives back results as a python dictionary as pandas 
    energy_system.results['main'] = processing.results(model) 
    #meta results contain data of solver's performance and outcome
    energy_system.results['meta'] = processing.meta_results(model)
    # # Dump the energy system including the results (saving) for later analyzing of the results without running the whole code
    energy_system.dump('U:\\ann82611\\04_Code\\hydrogen_hub\\hydrogen_hub\\h2_hub_dumps', 'h2_hub_dump.oemof')
    #pp.pprint(energy_system.results['main'])
    #pp.pprint(energy_system.results['meta'])
    return energy_system





def main():
    config = load_config('config.yaml') #enter relative file path config file
    h2_hub = create_energy_system(config)
    h2_hub = optimizer(h2_hub, config) #Ergebnisse sind unter .results gespeichert
    plot_energy_system(h2_hub)
    plot_results(h2_hub)
    

if __name__ == "__main__":
    main() 
    # push test fred