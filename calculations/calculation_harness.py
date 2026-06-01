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
print("ENGR113 Simulation Project - Communication Link Analysis")
print("=" * 60)

print("\nSIGNAL-TO-NOISE RATIO CALCULATION")
print("=" * 20)
print(f"   Free Space Path Loss: {freeSpacePathLoss():.0f} dB")
print(f"   Noise Figure of the Receiver: {noiseFigureReciever():.3f} dB")
print(f"   Received Power: {linkBudget() + 30:.1f} dBm")
print(f"   Noise Power: {linearToDb(noisePower()) + 30:.1f} dBm")
print(f"   SNR: {signalToNoiseRatio():.1f} dB")

print("\nLINK MARGIN CALCULATION")
print("=" * 20)
print(f"   Spectral Efficiency: {spectralEfficiency():.2f} b/s/Hz")
print(f"   Receiver Power Threshold: {receiverThreshold() + 30:.1f} dBm")
print(f"   Link Margin: {linkMargin():.1f} dB")

print("\nBIT ERROR RATE CALCULATION")
print("=" * 20)
print(f"   Normalized SNR (Eb/N0): {snrToBit():.1f} dB/bit")
print(f"   Bit Error Rate: {bitErrorRate():.2e}")
print(f"   Packet Error Rate: {packetErrorRate():.2e}")

print("\nDATA RATE CALCULATIONS")
print("=" * 20)
print(f"   Packet Transmission Time: {packetTransmissionTime()*1e6:.1f} ms")
print(f"   Packets Per Second: {packetsPerSecond():.0f} packets/s")
print(f"   Expected Packets in One Orbit: {packetsPerSecond() * ORBIT_TIME:,.0f}")
print(f"   Data Transmitted in One Orbit: {(packetsPerSecond() * ORBIT_TIME * PACKET_SIZE_BITS / (8 * 1024 * 1024))*1e-3:,.2f} TB")

print("\nTIME IN VIEW DURING ONE ORBIT CALCULATION")
print("=" * 20)
print(f"   Time seen by one satellite: {(ORBIT_TIME / 180)-((HANDOFF_TIME/60)*3):.2f} minutes")
print(f"   Time seen by two satellites: {HANDOFF_TIME * 3 / 60:.2f} minutes")

print("\nProject Calculations Complete")
print("" + "=" * 60)

