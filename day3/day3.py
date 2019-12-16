import numpy as np
import re
import pandas as pd
import matplotlib.pyplot as plt


# Create line class
class Line():
    def __init__(self):
        # Initialize at (0,0)
        self.x = 0
        self.y = 0
        self.loc_hist = [(0, 0)]

    def move(self, instruction):
        # Match instruction with Letter+Number
        match = re.match(r"([A-Z]+)([0-9]+)", instruction)
        direction, num = match.groups()
        num = int(num)

        if match is None:
            print("No match to understood coordinates")

        if direction == 'U':
            for j in range(num):
                self.y += 1
                self.loc_hist.append(self.loc())

        elif direction == 'D':
            for j in range(num):
                self.y -= 1
                self.loc_hist.append(self.loc())

        elif direction == 'L':
            for j in range(num):
                self.x -= 1
                self.loc_hist.append(self.loc())

        elif direction == 'R':
            for j in range(num):
                self.x += 1
                self.loc_hist.append(self.loc())

        else:
            print(f"No understood direction {direction}")

    def loc(self):
        location = (self.x, self.y)
        return(location)


# Read move instructions from files
move1 = pd.read_csv("./line1.csv", header=None, dtype=str).values[0, :]
move2 = pd.read_csv("./line2.csv", header=None, dtype=str).values[0, :]

# Initialize empty lines
line1 = Line()
line2 = Line()

# Create the lines
print("Creating line 1")
for move in move1:
    line1.move(move)

print("Creating line 2")
for move in move2:
    line2.move(move)

# Find matches
print("Looking for points")
print(len(line1.loc_hist))
for len1, points1 in enumerate(line1.loc_hist):
    for len2, points2 in enumerate(line2.loc_hist):
        if points1 == points2:
            print(
                f"Match found with Manhattan Distance of {sum(points1)} and a combined step count of {len1+len2}")
