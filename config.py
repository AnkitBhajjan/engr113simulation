## Constants and configuration parameters for the simulation
import math


ORBIT_TIME = 90 * 60  # seconds
HANDOFF_TIME = 3 * 60 # 3 minutes in seconds, time taken for handoff between satellites

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
DISTANCE_KM = 42000 # km, distance between transmitter and receiver (GEO to ISS)

# System Design Assumptions
IMPLEMENTATION_MARGIN = 4 # dB, to account for implementation losses and non-idealities in the system.
SHANNON_GAP = 3 # dB, gap from Shannon capacity to account for practical modulation and coding schemes
ERROR_MARGIN = 1e-10 # margin to prevent BER from being exactly zero, which can cause issues in logarithmic calculations
ROLL_OFF_FACTOR = 0.25 # Roll-off factor for the pulse shaping filter, which affects the occupied bandwidth of the signal.

# System Parameters
DATA_RATE = 1.05e9  # bps, 1.05 Gbps
BANDWIDTH = 500e6 # Hz, bandwidth of the communication link (500 MHz for Ku-band)
FREQUENCY = 1.50034e10 # Hz, frequency of the signal (15.0034 GHz for Ku-band)

# Link Design Parameters
CODE_RATE = 0.75 # 3/4 coding rate for error correction, for every 4 bits transmitted, 3 are data and 1 is error correction
R_GROSS = DATA_RATE / CODE_RATE # Gross data rate before error correction
BYTES_PER_PACKET = 1518 # bytes, size of the data packet being transmitted (including headers and payload)
BITS_PER_SYMBOL = 10 # Specific to 1024-QAM
PACKET_SIZE_BITS = BITS_PER_SYMBOL * BYTES_PER_PACKET # Total bits in the container
BAUD_RATE = R_GROSS / (math.log2(BITS_PER_SYMBOL)) # Symbols per second
OCCUPIED_BANDWIDTH = BAUD_RATE * 1 + (ROLL_OFF_FACTOR) # Occupied bandwidth with roll-off factor

# Transmitter Parameters
TRANSMITTER_GAIN = 47.731 # dBi, watts leaving the HPA, gain of the transmitter antenna
TRANSMITTER_POWER = 17.781513 # dBW, power of the transmitter

# Receiver Parameters
RECEIVER_GAIN = 65.233 # dBi, gain of the receiver antenna

## Noise and Loss Assumptions
LOSS_MISC = 3.3 + IMPLEMENTATION_MARGIN # dB, included feeder loss, pointing loss, polization loss, and other miscellaneous losses.

## Receiver Noise Factors and Gains
BANDPASS_FILTER_NOISE_FIGURE = 1 # dB, noise figure of the bandpass filter   
BANDPASS_FILTER_GAIN = 0.1 # dB, gain of the bandpass filter, assumed to be negligible 

LNA_NOISE_FIGURE = 3 # dB, noise figure of the Low Noise Amplifier (LNA)
LNA_GAIN = 30 # dB, gain of the Low Noise Amplifier (LNA)

MIXER_NOISE_FIGURE = 8.5 # dB, noise figure of the Mixer
MIXER_GAIN = -7.5 # dB, gain of the Mixer