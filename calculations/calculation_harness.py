import sys
from pathlib import Path

# Add parent directory to path to import config
sys.path.insert(0, str(Path(__file__).parent.parent))

import numpy as np
from config import *
from calculations.link_budget import *
from calculations.snr import *
from calculations.ber import *


def print_section(title):
    print(f"\n{title}")
    print("=" * 20)


print("=" * 60)
print("ENGR113 Simulation Project - Communication Link Analysis")
print("=" * 60)

print_section("SYSTEM PARAMETERS")
print(f"   Data Rate: {DATA_RATE/1e9:.2f} Gbps")
print(f"   Code Rate: {CODE_RATE:.2f}")
print(f"   Gross Data Rate: {R_GROSS/1e9:.2f} Gbps")
print(f"   Bandwidth: {BANDWIDTH/1e6:.1f} MHz")
print(f"   Frequency: {FREQUENCY/1e9:.4f} GHz")
print(f"   Packet Size: {BYTES_PER_PACKET} bytes")
print(f"   Bits Per Symbol: {BITS_PER_SYMBOL}")
print(f"   Link Distance: {DISTANCE_KM:,.0f} km")

print_section("ORBIT AND HANDOFF PARAMETERS")
print(f"   Orbit Time: {ORBIT_TIME/60:.1f} minutes")
print(f"   Handoff Time: {HANDOFF_TIME/60:.1f} minutes")

print_section("LINK DESIGN PARAMETERS")
print(f"   Transmitter Power: {TRANSMITTER_POWER:.2f} dBW")
print(f"   Transmitter Gain: {TRANSMITTER_GAIN:.2f} dBi")
print(f"   Receiver Gain: {RECEIVER_GAIN:.2f} dBi")
print(f"   Miscellaneous Losses: {LOSS_MISC:.1f} dB")
print(f"   Implementation Margin: {IMPLEMENTATION_MARGIN:.1f} dB")
print(f"   Shannon Gap: {SHANNON_GAP:.1f} dB")

print_section("RECEIVER CHAIN PARAMETERS")
print(f"   Bandpass Filter Noise Figure: {BANDPASS_FILTER_NOISE_FIGURE:.1f} dB")
print(f"   Bandpass Filter Gain: {BANDPASS_FILTER_GAIN:.1f} dB")
print(f"   LNA Noise Figure: {LNA_NOISE_FIGURE:.1f} dB")
print(f"   LNA Gain: {LNA_GAIN:.1f} dB")
print(f"   Mixer Noise Figure: {MIXER_NOISE_FIGURE:.1f} dB")
print(f"   Mixer Gain: {MIXER_GAIN:.1f} dB")

print_section("RF LINK BUDGET")
print(f"   Free Space Path Loss: {freeSpacePathLoss():.0f} dB")
print(f"   Received Power: {linkBudget() + 30:.1f} dBm")

print_section("RECEIVER NOISE")
print(f"   Noise Figure of the Receiver: {noiseFigureReciever():.2f} dB")
print(f"   Noise Power: {linearToDb(noisePower()) + 30:.1f} dBm")

print_section("CAPACITY AND LINK MARGIN")
print(f"   Spectral Efficiency: {spectralEfficiency():.1f} b/s/Hz")
print(f"   SNR: {signalToNoiseRatio():.1f} dB")
print(f"   Receiver Power Threshold: {receiverThreshold() + 30:.1f} dBm")
print(f"   Link Margin: {linkMargin():.1f} dB")

print_section("BIT AND PACKET ERROR RATES")
print(f"   Normalized SNR to Bit (Eb/N0): {snrToBit():.1f} dB/bit")
print(f"   Normalized SNR to Symbol (Es/N0): {snrToSymbol():.1f} dB/symbol")
print(f"   Bit Error Rate: {bitErrorRate():.2e}")
print(f"   Packet Error Rate: {packetErrorRate():.2e}")

print_section("DATA RATE CALCULATIONS")
print(f"   Baud Rate: {BAUD_RATE/1e6:.1f} Msymbols/s")
print(f"   Roll-off Factor: {ROLL_OFF_FACTOR:.0%}")
print(f"   Occupied Bandwidth: {OCCUPIED_BANDWIDTH/1e6:.1f} MHz")
print(f"   Packet Transmission Time: {packetTransmissionTime()*1e6:.1f} ms")
print(f"   Packets Per Second: {packetsPerSecond():.0f} packets/s")
print(f"   Expected Packets in One Orbit: {packetsPerSecond() * ORBIT_TIME:,.0f}")
print(f"   Data Transmitted in One Orbit: {(packetsPerSecond() * ORBIT_TIME * PACKET_SIZE_BITS / (8 * 1024 * 1024))*1e-3:,.2f} TB")

print_section("TIME IN VIEW DURING ONE ORBIT CALCULATION")
print(f"   Time seen by one satellite: {(ORBIT_TIME / 180)-((HANDOFF_TIME/60)*3):.2f} minutes")
print(f"   Time seen by two satellites: {HANDOFF_TIME * 3 / 60:.2f} minutes")

print("\nProject Calculations Complete")
print("" + "=" * 60)
