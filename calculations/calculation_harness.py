import sys
from pathlib import Path

# Add parent directory to path to import config
sys.path.insert(0, str(Path(__file__).parent.parent))

import numpy as np
from config import *
from calculations.link_budget import *
from calculations.snr import *
from calculations.ber import *

print("=" * 60)
print("ENGR113 Simulation Project - Signal-to-Noise Ratio Calculation")
print("=" * 60)

print("\nSIGNAL-TO-NOISE RATIO CALCULATION")
print("=" * 20)
print(f"   Free Space Path Loss: {freeSpacePathLoss():.2f} dB")
print(f"   Received Power: {dbToLinear(linkBudget())*1e9:.2f} nW")
print(f"   Noise Power: {noisePower()*1e12:.2f} pW")
print(f"   SNR: {signalToNoiseRatio():.2f} dB")

print("\nLINK MARGIN CALCULATION")
print("=" * 20)
print(f"   Spectral Efficiency: {spectralEfficiency():.2f} bps/Hz")
print(f"   Receiver Power Threshold: {dbToLinear(receiverThreshold())*1e9:.2f} nW")
print(f"   Link Margin: {linkMargin():.2f} dB")

print("\nBIT ERROR RATE CALCULATION")
print("=" * 20)
print(f"   Normalized SNR (Eb/N0): {snrToBit():.2f} dB/bit")
print(f"   Bit Error Rate: {bitErrorRate():.2e}")
print(f"   Packet Error Rate: {packetErrorRate():.2e}")


print("\nProject Calculations Complete")
print("" + "=" * 60)

