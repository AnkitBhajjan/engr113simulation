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
signal_to_noise_ratios = [signalToNoiseRatio(distance_km=d) for d in distance_range_km]

#ber calc
ebn0_sweep = np.linspace(0, 30)
ber_vals = [bitErrorRate(eb_n0_db=eb) for eb in ebn0_sweep]

# Formatting
fontname = "serif"

# Link margin graph
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

# Path loss graph
plt.figure(figsize=(10, 5))
plt.plot(distance_range_km, path_losses, label='Free Space Path Loss', color='crimson')
plt.title('ISS-to-GEO Free Space Path Losses Over Orbital Path', fontname=fontname, fontsize=14)
plt.xlabel('Distance (km)', fontname=fontname)
plt.ylabel('Path Loss (dB)', fontname=fontname)
plt.grid(True, which="both", linestyle=":")
plt.legend()
plt.show()

# SNR graph
plt.figure(figsize=(10, 5))
plt.plot(distance_range_km, signal_to_noise_ratios, label='Signal-to-Noise Ratio', color='crimson')
plt.title('ISS-to-GEO Signal-to-Noise Ratio Over Orbital Path', fontname=fontname, fontsize=14)
plt.xlabel('Distance (km)', fontname=fontname)
plt.ylabel('SNR (dB)', fontname=fontname)
plt.grid(True, which="both", linestyle=":")
plt.legend()
plt.show()

# snr vs ber graph
plt.figure(figsize=(10, 5))
plt.plot(ebn0_sweep, ber_vals, label='Bit Error Rate (1024-QAM)', color='crimson')
plt.yscale('log')
plt.title('Bit Error Rate vs Normalized SNR (Eb/N0)', fontname=fontname, fontsize=14)
plt.xlabel('Eb/N0 (dB)', fontname=fontname)
plt.ylabel('Bit Error Rate (BER)', fontname=fontname)
plt.grid(True, which="both", linestyle=":")
plt.legend()
plt.show()


