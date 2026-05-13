import sys
from pathlib import Path

# Add parent directory to path to import config
sys.path.insert(0, str(Path(__file__).parent.parent))

import numpy as np
from config import *
from calculations.link_budget import *
from calculations.snr import *

def snrToBit():
    """
    Normalize SNR to bits per symbol using the spectral efficiency of the communication system.

    Returns
    -------
    float
        Normalized SNR in bits per symbol
    """

    eb_n0_db = signalToNoiseRatio() - linearToDb(spectralEfficiency())  

    return eb_n0_db

def bitErrorRate():
    """
    Calculate the bit error rate (BER) for a given modulation scheme using the normalized SNR.

    Returns
    -------
    float
        Bit error rate (BER)
    """

    eb_n0_linear = dbToLinear(snrToBit())

    # Uses 256-QAM protocal for BER calculation, which is a common modulation scheme for high data rates
    ber = 0.5 * np.exp(-eb_n0_linear / 10) + ERROR_MARGIN  # Adding a small margin to prevent BER from being exactly zero

    return ber

def packetErrorRate(packet_size_bits=PACKET_SIZE_BITS):  # Assuming a standard Ethernet frame size of 1500 bytes
    """
    Calculate the packet error rate (PER) based on the bit error rate (BER) and the size of the packet.

    Parameters
    ----------
    packet_size_bits : int, optional
        Size of the packet in bits (default is 1500 bytes converted to bits)

    Returns
    -------
    float
        Packet error rate (PER)
    """

    ber = bitErrorRate()
    
    # Assuming independent bit errors, the PER can be calculated as:
    per = 1 - (1 - ber) ** packet_size_bits

    return per