## Constants and configuration parameters for the simulation
DATA_RATE = 1.5e9  # bps, 1.5gbps
ORBIT_TIME = 90 * 60  # seconds

EARTH_RADIUS = 1 # relative units, not to scale
ISS_RADIUS = 1.3
GEO_RADIUS = 2.2

coverage = { # percentage of ISS orbit covered by GEO relay satellites
    1: 0.35,
    2: 0.70,
    3: 0.99
    }

## Physical and Design Constants
C = 299792458 # m/s, speed of light in vacuum
TEMPERATURE = 290 # K, standard noise temperature
BOLTZMANN_CONSTANT = 1.380649e-23 # J/K, Boltzmann's constant
BANDWIDTH = 600e6 # Hz, bandwidth of the communication link (600 MHz for Ku-band)
FREQUENCY = 1.50034e10 # Hz, frequency of the signal (15.0034 GHz for Ku-band)
DISTANCE_KM = 37000 # km, distance between transmitter and receiver (GEO to ISS)
SHANNON_GAP = 3 # dB, gap from Shannon capacity to account for practical modulation and coding schemes
ERROR_MARGIN = 1e-12 # margin to prevent BER from being exactly zero, which can cause issues in logarithmic calculations

# Transmitter Parameters
TRANSMITTER_GAIN = 47.731 # dBi, watts leaving the HPA, gain of the transmitter antenna
TRANSMITTER_POWER = 17.781513 # dBW, power of the transmitter

# Receiver Parameters
RECEIVER_GAIN = 65.233 # dBi, gain of the receiver antenna

## Noise and Loss Assumptions
IMPLEMENTATION_MARGIN = 4 # dB, to account for implementation losses and non-idealities in the system.
LOSS_MISC = 3.3 + IMPLEMENTATION_MARGIN # dB, included feeder loss, pointing loss, polization loss, and other miscellaneous losses.

## Receiver Noise Factors and Gains
BANDPASS_FILTER_NOISE_FACTOR = 1 # dB, noise figure of the bandpass filter   
BANDPASS_FILTER_GAIN = 0.1 # dB, gain of the bandpass filter, assumed to be negligible 

LNA_NOISE_FACTOR = 3 # dB, noise figure of the Low Noise Amplifier (LNA)
LNA_GAIN = 30 # dB, gain of the Low Noise Amplifier (LNA)

MIXER_NOISE_FACTOR = 8.5 # dB, noise figure of the Mixer
MIXER_GAIN = -7.5 # dB, gain of the Mixer