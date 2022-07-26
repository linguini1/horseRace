# Graphs results of the game

# Imports
from sys import _debugmallocstats
import matplotlib.pyplot as plt
from classes.stats import Stats

# Constants

# Fetch and unpack data
data = Stats().data
horses = data.keys()
wins = [data[_]["wins"] for _ in horses]
debts = [data[_]["debts"] for _ in horses]

# Plotting
plt.plot(horses, wins, "-")
plt.plot(horses, debts, "-")

# Plot labeling
plt.xlabel("Horses")
plt.ylabel("Count (rounds)")

# Show
plt.savefig("graph")