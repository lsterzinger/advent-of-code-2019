import numpy as np
import math

def calc_fuel(mass):
    fuel = math.floor(mass/3) - 2
    return(fuel)


modules = np.genfromtxt('./puzzle_input.txt')
# modules = [83285]
tot_fuel = 0

for mass in modules:
    mod_fuel = calc_fuel(mass)  # Calculate fuel needed for module

    if mod_fuel > 0:  # If the fuel needed for the module is > 0
        extra_fuel = calc_fuel(mod_fuel)  # Calculate extra fuel needed for initial fuel

        mod_fuel += extra_fuel

        while extra_fuel > 0:
            extra_fuel = calc_fuel(extra_fuel)
            if extra_fuel <= 0:
                break

            mod_fuel += extra_fuel


    tot_fuel += mod_fuel  # Add fuel needed for module to total needed fuel
print(f"The total required fuel is: {tot_fuel}")