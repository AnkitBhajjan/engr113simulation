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

# Calculate path loss, received power, and link margin for each distance in the range
path_losses = [freeSpacePathLoss(distance_km=d) for d in distance_range_km]
received_powers = [linkBudget(distance_km=d) for d in distance_range_km]
link_margins = [linkMargin(received_power_dBW=p) for p in received_powers]

# Formatting
fontname = "serif"

# Plotting
plt.figure(figsize=(10, 5))
plt.plot(distance_range_km, link_margins, label='Link Margin (1024-QAM)', color='crimson')
plt.ylim(15, 18.5)
plt.yticks(np.arange(15, 18.6, 0.5))
plt.title('ISS-to-GEO Link Margin Over Orbital Path', fontname=fontname, fontsize=14)
plt.xlabel('Distance (km)', fontname=fontname)
plt.ylabel('Margin (dB)', fontname=fontname)
plt.grid(True, which="both", linestyle=":")
plt.legend()
plt.show()

# snr vs ber graph


