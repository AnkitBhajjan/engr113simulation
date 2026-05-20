import sys
from pathlib import Path

# Add parent directory to path to import config
sys.path.insert(0, str(Path(__file__).parent.parent))

import numpy as np
from config import *
from calculations.link_budget import *
from calculations.snr import *
from calculations.ber import *
import matplotlib.pyplot as plt


# SNR (y axis) vs Distance (x axis) graph 


# Geometrically accurate operational range in km
distance_range_km = np.linspace(35000, 44000, 500)

# Example setup for your link budget array execution
path_losses = [freeSpacePathLoss(distance_km=d) for d in distance_range_km]
received_powers = [linkBudget(distance_km=d) for d in distance_range_km]
link_margins = [linkMargin(received_power_dBW=p) for p in received_powers]

# Plotting
plt.figure(figsize=(10, 5))
plt.plot(distance_range_km, link_margins, label='Link Margin (1024-QAM)', color='crimson')
plt.axhline(y=0, color='black', linestyle='--', label='Link Drop Threshold (0 dB)')
plt.title('ISS-to-GEO Link Margin Over Orbital Path')
plt.xlabel('Distance (km)')
plt.ylabel('Margin (dB)')
plt.grid(True, which="both", linestyle=":")
plt.legend()
plt.show()

# Link budget vs distance (x axis)graph


# snr vs ber graph



