import numpy as np
from calculations import link_budget
from config import *
from calculations.link_budget import free_space_path_loss
from calculations.snr import *

# Test parameters
test_distances = np.array([100, 500, 1000, 5000])  # km

print("=" * 60)
print("LINK BUDGET CALCULATION HARNESS")
print("=" * 60)

# Test 1a: Free Space Path Loss
print("\n1a. FREE SPACE PATH LOSS")
print(f"   Frequency: {FREQUENCY/1e9:.4f} GHz")
print(f"   Distances: {test_distances} km")
losses = free_space_path_loss(test_distances, FREQUENCY)
for d, loss in zip(test_distances, losses):
    print(f"   Distance {d:5} km → Path Loss: {loss:7.2f} dB")

# Test 1b: Link Budget Calculation
print("\n2. LINK BUDGET CALCULATION")
for d in test_distances:
    received_power = link_budget.linkBudget(distance_km=d)
    print(f"   Distance {d:5} km → Received Power: {received_power:7.2f} dBW")

print("=" * 60)
print("SIGNAL TO NOISE RATIO CALCULATION HARNESS")
print("=" * 60)

# Test 2: dB to Linear Conversion
print("\n3. dB TO LINEAR CONVERSION")
test_db_values = np.array([3, 6, 10, 20, 30])
for db in test_db_values:
    linear = dbToLinear(db)
    print(f"   {db:2} dB → {linear:8.3f} linear")

# Test 3: Linear to dB Conversion
print("\n4. LINEAR TO dB CONVERSION")
test_linear_values = np.array([1, 2, 10, 100, 1000])
for linear in test_linear_values:
    db = linearToDb(linear)
    print(f"   {linear:4} linear → {db:7.2f} dB")

# Test 4: Noise Power
print("\n5. NOISE POWER CALCULATION")
noise_pw = noisePower(TEMPERATURE, BANDWIDTH)
noise_dbw = 10 * np.log10(noise_pw)
print(f"   Temperature: {TEMPERATURE} K")
print(f"   Bandwidth: {BANDWIDTH/1e6:.0f} MHz")
print(f"   Noise Power: {noise_pw:.2e} W ({noise_dbw:.2f} dBW)")

# Test 5: Noise Figure Calculation
print("\n6. NOISE FIGURE CALCULATION")
nf_db = noiseFigureReciever()
print(f"   Noise Figure of Receiver: {nf_db:.2f} dB")

# Test 6: Signal-to-Noise Ratio Calculation
print("\n7. SIGNAL-TO-NOISE RATIO CALCULATION")
snr_db = signalToNoiseRatio()
print(f"   Received Power: {link_budget.linkBudget():.2f} dBW")
print(f"   Noise Power: {noisePower():.2e} W")
print(f"   SNR: {snr_db:.2f} dB")

print("\n" + "=" * 60)