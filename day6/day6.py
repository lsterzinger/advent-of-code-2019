import numpy as np
import pandas as pd
from tqdm import tqdm

# Define planet class
class Planet():
    def __init__(self, name):
        self.name = name

    # Calculate orbits
    def calc_orbits(self, orblist):
        current_planet = self.name  # Set current planet to self
        self.count = 0
        
        # Loop over orbits until reaching COM
        while True:
            current_orbit = orblist.loc[orblist['Planet'] == current_planet]
            current_planet = current_orbit.values[0,0]
            self.count += 1
            if current_planet == 'COM': break

orblist = pd.read_csv("./list.txt",header=None, delimiter=")",names=["Orbits", "Planet"])

tot_count = 0

print("Analyzing orbits...")
for p in tqdm(orblist['Planet']):

    planet = Planet(p)
    planet.calc_orbits(orblist)
    tot_count += planet.count
    
print(tot_count)
