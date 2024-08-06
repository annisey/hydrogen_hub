import oemof.solph as solph
from oemof.solph.components import Sink, Source, Converter, GenericStorage
from oemof.solph import create_time_index, Bus, Flow
#for plotting
import networkx
from oemof.network.graph import create_nx_graph
import matplotlib.pyplot as plt

index = create_time_index(2020) #range of a year, hourly

#create system
h2_hub = solph.EnergySystem(timeindex=index, infer_last_interval=False) #einlesen ob infer_last_interval true or false

#add buses
electricity_bus = Bus(label='electricity') #, inputs, outputs
h2_to_storage_bus = Bus(label='h2_to_storage') #inputs, outputs to add
h2_to_production_bus = Bus(label='h2_to_production') #, inputs, outputs

h2_hub.add(electricity_bus, h2_to_production_bus, h2_to_storage_bus)

#add sources
pv_source = Source(label='pv', outputs={electricity_bus: Flow(fix=0.5, nominal_value=5000000)}) # 5MW (?)
wind_source = Source(label='wind', outputs={electricity_bus: Flow(fix=0.5, nominal_value=10000000)}) #10MW (?) 
grid_source = Source(label='grid', outputs={electricity_bus: Flow(fix=1, nominal_value=100000000)}) #100MW (?)

h2_ship_source = Source(label='h2_ship', outputs={h2_to_storage_bus: Flow(fix=1, nominal_value=500, variable_costs=50)}) # Einheit check
electrolyzer = Converter(label='electrolyzer', inputs={electricity_bus: Flow()},outputs={h2_to_storage_bus: Flow()}, conversion_factors={h2_to_storage_bus: 0.25}) #conversion factor and Flow tbd

h2_hub.add(pv_source, wind_source, grid_source, h2_ship_source, electrolyzer)

#add storage
h2_storage = GenericStorage(label= 'h2_storage', inputs={h2_to_storage_bus: Flow()},outputs={h2_to_production_bus: Flow()},
                            loss_rate=0.001, nominal_storage_capacity=200,inflow_conversion_factor=0.98, outflow_conversion_factor=0.8) #parameters tbd

h2_hub.add(h2_storage)

#add sink
steel_mill = Sink(label='steel_mill', inputs={h2_to_production_bus: Flow(), electricity_bus: Flow()})

h2_hub.add(steel_mill)


#plot
graph = create_nx_graph(h2_hub)
networkx.draw(graph, with_labels=True, font_size=8)
plt.show()