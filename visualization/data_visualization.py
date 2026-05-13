import sys
from pathlib import Path

# Add parent directory to path to import config
sys.path.insert(0, str(Path(__file__).parent.parent))

from config import *


#data transmitted in ONE iss orbit
data = []
for sats in coverage:
    connected_time = ORBIT_TIME * coverage[sats]

    total_megabits = DATA_RATE / 1e6 * connected_time
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
#add ground control center locations
import numpy as np
from matplotlib.animation import FuncAnimation

# satellite angles
geo_angles = np.radians([0, 120, 240])

fig, ax = plt.subplots(figsize=(6,6))
ax.set_xlim(-2.5, 2.5)
ax.set_ylim(-2.5, 2.5)
ax.set_aspect('equal')

earth = plt.Circle((0,0), EARTH_RADIUS, color='blue')
ax.add_patch(earth)

geo_x = GEO_RADIUS * np.cos(geo_angles)
geo_y = GEO_RADIUS * np.sin(geo_angles)

ax.scatter(geo_x, geo_y, color='red', s=100, label='GEO Satellites')

iss_dot, = ax.plot([], [], 'ko', markersize=8)

lines = []

for _ in range(3):
    line, = ax.plot([], [], 'y--')
    lines.append(line)

def update(frame):

    angle = np.radians(frame)

    iss_x = ISS_RADIUS * np.cos(angle)
    iss_y = ISS_RADIUS * np.sin(angle)

    iss_dot.set_data([iss_x], [iss_y])

    for i in range(3):

        dx = geo_x[i] - iss_x
        dy = geo_y[i] - iss_y

        distance = np.sqrt(dx**2 + dy**2)

        if distance < 3:
            lines[i].set_data([iss_x, geo_x[i]],
                              [iss_y, geo_y[i]])
        else:
            lines[i].set_data([], [])

    return [iss_dot] + lines

ani = FuncAnimation(fig, update,
                    frames=np.arange(0,360,2),
                    interval=50)

plt.legend()
plt.title("ISS Communication with GEO Relay Satellites")

plt.show()