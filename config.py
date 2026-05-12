## Contains constants and configuration parameters for the simulation

DATA_RATE = 600  # Mbps
ORBIT_TIME = 90 * 60  # seconds

EARTH_RADIUS = 1 # relative units, not to scale
ISS_RADIUS = 1.3
GEO_RADIUS = 2.2

coverage = { # percentage of ISS orbit covered by GEO relay satellites
    1: 0.35,
    2: 0.70,
    3: 0.99
    }