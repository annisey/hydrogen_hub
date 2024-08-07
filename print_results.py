import oemof.solph as solph
import pprint as pp
import matplotlib.pyplot as plt
import pandas as pd


def restore_energy_system(file_path):
    energy_system = solph.EnergySystem()
    energy_system.restore(file_path, 'h2_hub_dump.oemof')   
    print(energy_system) 
    return energy_system

def plot_results(energy_system):
    main_results = energy_system.results['main']
    pp.pprint(main_results)

    # Extract time index
    time_index = energy_system.timeindex

    # Extract PV and Wind generation data
    #Key does not work, I don't unterstand why
    pv_key = ("<oemof.solph.components._source.Source: 'pv'>", "<oemof.solph.buses._bus.Bus: 'electricity'>")
    

    wind_key = ("<oemof.solph.components._source.Source: 'wind'>", "<oemof.solph.buses._bus.Bus: 'electricity'>")
    
     # Debug print for key existence
    if pv_key in main_results:
        print(f"PV key found: {pv_key}")
        pv_generation = main_results[pv_key]['sequences']['flow']
    else:
        print(f"PV key not found")
        pv_generation = pd.Series([])
        print(pv_generation)


    # # Access sequences for flow values
    # pv_generation = main_results[pv_key]['sequences']['flow']
    # print(pv_generation)

   
    # # Ensure there are no NaN values for the plot
    # pv_generation = pv_generation.dropna()
    # wind_generation = wind_generation.dropna()

    # # Make sure the length of generation data aligns with the time index
    # time_index_pv = time_index[:len(pv_generation)]
    # time_index_wind = time_index[:len(wind_generation)]

    # print(pv_generation.head())
    # print(wind_generation.head())

    # print(len(time_index))
    # print(len(pv_generation))
    # print(len(wind_generation))
    # print(main_results.keys())
    # print(pv_generation.isna().sum())
    # print(wind_generation.isna().sum())


    # # Plot PV and Wind generation for one year
    # plt.figure(figsize=(12, 6))
    # plt.plot(time_index_pv, pv_generation, label='PV Generation', color='orange')
    # plt.plot(time_index_wind, wind_generation, label='Wind Generation', color='blue')
    # plt.xlabel('Time')
    # plt.ylabel('Electricity Generation (MW)')
    # plt.legend()
    # plt.title('Electricity Generation from PV and Wind for One Year')
    # plt.grid(True)
    # plt.tight_layout()
    # plt.show()

h2_hub = restore_energy_system(file_path='U:\\ann82611\\04_Code\\hydrogen_hub\\hydrogen_hub\\h2_hub_dumps')
#plot_results(h2_hub)