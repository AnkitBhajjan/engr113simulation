## Constants and configuration parameters for the simulation
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

## Link Budget Parameters
C = 299792458 # m/s, speed of light in vacuum
BOLTZMANN_CONSTANT = 1.380649e-23 # J/K, Boltzmann's constant
BANDWIDTH = 600e6 # Hz, bandwidth of the communication link (600 MHz for Ku-band)
FREQUENCY = 1.50034e10 # Hz, frequency of the signal (15.0034 GHz for Ku-band)

# Transmitter Parameters
TRANSMITTER_GAIN = 47.731 # dBi, gain of the transmitter antenna
TRANSMITTER_POWER = 17.781513 # dBW, power of the transmitter

# Receiver Parameters
RECEIVER_GAIN = 65.233 # dBi, gain of the receiver antenna
RECIEVER_POWER_THRESHOLD = -120 # dBW, minimum power required at the receiver for successful communication [TEMPORTARY VALUE, TO BE UPDATED]

## Noise and Loss Assumptions
IMPLEMENTATION_MARGIN = 2 # dB, to account for implementation losses and non-idealities in the system.
LOSS_MISC = 3.3 + IMPLEMENTATION_MARGIN # dB, included feeder loss, pointing loss, polization loss, and other miscellaneous losses.
