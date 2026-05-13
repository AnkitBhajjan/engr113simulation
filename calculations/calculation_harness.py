import sys
from pathlib import Path

# Add parent directory to path to import config
sys.path.insert(0, str(Path(__file__).parent.parent))

import numpy as np
from config import *
from calculations.link_budget import *
from calculations.snr import *

print("=" * 60)
print("ENGR113 Simulation Project - Signal-to-Noise Ratio Calculation")
print("=" * 60)

print("\nSIGNAL-TO-NOISE RATIO CALCULATION")
snr_db = signalToNoiseRatio()
print(f"   Free Space Path Loss: {freeSpacePathLoss():.2f} dB")
print(f"   Received Power: {linkBudget():.2f} dBW")
print(f"   Noise Power: {noisePower():.2e} W")
print(f"   SNR: {snr_db:.2f} dB")

print("\nLINK MARGIN CALCULATION")
print(f"   Receiver Power Threshold: {recieverThreshold():.2f} dBW")
print(f"   Link Margin: {linkMargin():.2f} dB")

print("Project Calculations Complete")

print("\n" + "=" * 60)

