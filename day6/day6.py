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

            if current_planet in numlist:
                self.count += numlist[current_planet]
                break
            if current_planet == 'COM': break
    
    def calc_orbits_with_history(self, orblist):
        current_planet = self.name  # Set current planet to self
        self.count = 0
        self.hist = [self.name]
        # Loop over orbits until reaching COM
        while True:
            current_orbit = orblist.loc[orblist['Planet'] == current_planet]
            current_planet = current_orbit.values[0,0]
            self.count += 1

            self.hist.append(current_planet)
            if current_planet == 'COM': break


orblist = pd.read_csv("./list.txt",header=None, delimiter=")",names=["Orbits", "Planet"])

tot_count = 0

############
# Part One #
############

# numlist = {}
# print("Analyzing orbits...")
# for p in tqdm(orblist['Planet']):
#     planet = Planet(p)
#     planet.calc_orbits(orblist)
#     numlist[p] = planet.count
#     tot_count += planet.count
# print(tot_count)

############
# Part Two #
############

santa = Planet("SAN")
you = Planet("YOU")

santa.calc_orbits_with_history(orblist)
you.calc_orbits_with_history(orblist)

pd.DataFrame(santa.hist).to_csv("santa.csv")
pd.DataFrame(you.hist).to_csv("you.csv")
