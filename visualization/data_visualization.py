import sys
from pathlib import Path

# Add parent directory to path to import config
sys.path.insert(0, str(Path(__file__).parent.parent))

from config import *


#data transmitted in ONE iss orbit
data = []
for sats in coverage:
    connected_time = ORBIT_TIME * coverage[sats]

    total_megabits = R_GROSS / 1e6 * connected_time
    total_gigabits = total_megabits / 1000
    total_gigabytes = total_gigabits / 8
    data.append(total_gigabytes)
    print(f"{sats} GEO satellites:")
    print(f" Connected time: {connected_time/60:.1f} minutes")
    print(f" Data transmitted: {total_gigabits:.1f} Gigabits or {total_gigabytes:.1f} GB")
    print()

#percent increase from 1 to 2 to 3 satellites
oneToTwo = ((283.5 - 141.7) / 141.7) * 100
twoToThree = ((400.9 - 283.5) / 283.5) * 100
oneToThree = ((400.9 - 141.7) / 141.7) * 100

print("Percent increase from 1 to 2 GEO relay satellites:")
print(f"{oneToTwo:.2f}%")

print("Percent increase from 2 to 3 GEO relay satellites:") #this makes sense to be lower bc 2 satellites is 85% coverage and 3 satellites is 99% coverage
print(f"{twoToThree:.2f}%") 

print("Percent increase from 1 to 3 GEO relay satellites:")
print(f"{oneToThree:.2f}%")

#bar graph with matplotlib
import matplotlib.pyplot as plt
numSatellites = [1, 2, 3]

plt.bar(numSatellites, data)
plt.xlabel("Number of GEO Relay Satellites")
plt.ylabel("Data Transmitted per ISS Orbit (GB)")
plt.title("ISS Data Transmission Capability")
plt.show()

#animation
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.animation import PillowWriter

# -----------------------------
# Constants
# -----------------------------
EARTH_RADIUS = 1.0
ISS_RADIUS = 1.2
GEO_RADIUS = 2.2

# GEO satellite positions (0°, 120°, 240°)
geo_angles = np.radians([0, 120, 240])

# Handoff settings
HANDOFF_ANGLE = 6   # degrees (~scaled version of 3 min overlap)

# -----------------------------
# Figure setup
# -----------------------------
fig, ax = plt.subplots(figsize=(7,7))

ax.set_xlim(-2.6, 2.6)
ax.set_ylim(-2.6, 2.6)
ax.set_aspect('equal')
ax.set_facecolor("black")

# Earth
earth = plt.Circle((0,0), EARTH_RADIUS,
                   color='royalblue')
ax.add_patch(earth)

# -----------------------------
# GEO satellites
# -----------------------------
geo_x = GEO_RADIUS * np.cos(geo_angles)
geo_y = GEO_RADIUS * np.sin(geo_angles)

ax.scatter(geo_x, geo_y,
           color='red',
           s=120,
           label='GEO Satellites',
           zorder=5)

# -----------------------------
# ISS point
# -----------------------------
iss_dot, = ax.plot([], [],
                   'wo',
                   markersize=8,
                   label='ISS')

# -----------------------------
# Communication lines
# -----------------------------
lines = []

for _ in range(3):
    line, = ax.plot([], [],
                    color='lime',
                    linestyle='-',
                    linewidth=2.5,
                    alpha=0.9)
    lines.append(line)

# -----------------------------
# Sector boundary lines
# -----------------------------
# These divide Earth into 120° regions
boundary_angles = np.radians([60, 180, 300])

for ang in boundary_angles:

    x = 2.5 * np.cos(ang)
    y = 2.5 * np.sin(ang)

    ax.plot([0, x],
            [0, y],
            color='cyan',
            linestyle='--',
            alpha=0.25,
            linewidth=2)

# -----------------------------
# Animation update
# -----------------------------
def update(frame):
    angle_deg = frame
    angle = np.radians(angle_deg)

    # ISS position
    iss_x = ISS_RADIUS * np.cos(angle)
    iss_y = ISS_RADIUS * np.sin(angle)
    iss_dot.set_data([iss_x], [iss_y])

    # -------------------------
    # Determine closest GEO
    # -------------------------
    distances = []
    for i in range(3):
        dx = geo_x[i] - iss_x
        dy = geo_y[i] - iss_y
        distances.append(np.sqrt(dx**2 + dy**2))
    closest = np.argmin(distances)

    # -------------------------
    # Determine handoff region
    # -------------------------
    normalized_angle = angle_deg % 360

    # Each boundary sits between two known satellites:
    #   60°  → handoff between sat 0 (at 0°)  and sat 1 (at 120°)
    #  180°  → handoff between sat 1 (at 120°) and sat 2 (at 240°)
    #  300°  → handoff between sat 2 (at 240°) and sat 0 (at 0°)
    handoff_pairs = {
        60:  (0, 1),
        180: (1, 2),
        300: (2, 0),
    }

    active_sats = [closest]
    for center, (sat_a, sat_b) in handoff_pairs.items():
        diff = abs(normalized_angle - center)
        # Also handle wrap-around at 0°/360°
        diff = min(diff, 360 - diff)
        if diff < HANDOFF_ANGLE:
            active_sats = [sat_a, sat_b]
            break

    # -------------------------
    # Draw lines
    # -------------------------
    for i in range(3):
        if i in active_sats:
            lines[i].set_data([iss_x, geo_x[i]], [iss_y, geo_y[i]])
        else:
            lines[i].set_data([], [])

    return [iss_dot] + lines

# -----------------------------
# Animation
# -----------------------------
ani = FuncAnimation(
    fig,
    update,
    frames=np.arange(0, 360, 2),
    interval=50
)

# Save GIF
ani.save("iss_geo_handoff.gif",
         writer=PillowWriter(fps=20))

# Labels
plt.legend(loc='upper right')
plt.title("ISS Communication with GEO Relay Satellites",
          color='white')

# Make axes cleaner
ax.set_xticks([])
ax.set_yticks([])

plt.show()