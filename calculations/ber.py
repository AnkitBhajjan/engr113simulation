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

def snrToSymbol():
    """
    Normalize SNR to symbols per second using the spectral efficiency of the communication system.

    Returns
    -------
    float
        Normalized SNR in symbols per second
    """

    es_n0_db = signalToNoiseRatio() - linearToDb(spectralEfficiency() * BANDWIDTH / BAUD_RATE)  # Adjusting for bandwidth and symbol rate

    return es_n0_db

def bitErrorRate(eb_n0_db=snrToBit()):
    """
    Calculate the bit error rate (BER) for a given modulation scheme using the normalized SNR.

    Returns
    -------
    float
        Bit error rate (BER)
    """

    eb_n0_linear = dbToLinear(eb_n0_db)

    # Uses 256-QAM protocal for BER calculation, which is a common modulation scheme for high data rates
    ber = 0.5 * np.exp(-eb_n0_linear / 10) + ERROR_MARGIN  # Adding a small margin to prevent BER from being exactly zero

    return ber

def packetErrorRate(packet_size_bits=PACKET_SIZE_BITS, ber=bitErrorRate()):  # Assuming a standard Ethernet frame size of 1500 bytes
    """
    Calculate the packet error rate (PER) based on the bit error rate (BER) and the size of the packet.

    Parameters
    ----------
    packet_size_bits : int, optional
        Size of the packet in bits (default is 1500 bytes converted to bits)
    ber : float, optional
        Bit error rate (default is calculated from the current SNR)

    Returns
    -------
    float
        Packet error rate (PER)
    """
    
    # Assuming independent bit errors, the PER can be calculated as:
    per = 1 - (1 - ber) ** packet_size_bits

    return per

def packetTransmissionTime(packet_size_bits=PACKET_SIZE_BITS, data_rate=R_GROSS):
    """
    Calculate the time required to transmit a packet based on its size and the data rate.

    Parameters
    ----------
    packet_size_bits : int, optional
        Size of the packet in bits (default is 1500 bytes converted to bits)
    data_rate : float, optional
        Data rate of the communication link in bits per second (default is 1.5 Gbps)

    Returns
    -------
    float
        Time required to transmit the packet in seconds
    """

    transmission_time = packet_size_bits / data_rate

    return transmission_time

def packetsPerSecond(data_rate=R_GROSS, packet_size_bits=PACKET_SIZE_BITS):
    """
    Calculate the number of packets that can be transmitted per second based on the data rate and packet size.

    Parameters
    ----------
    data_rate : float, optional
        Data rate of the communication link in bits per second (default is 1.5 Gbps)
    packet_size_bits : int, optional
        Size of the packet in bits (default is 1500 bytes converted to bits)

    Returns
    -------
    float
        Number of packets that can be transmitted per second
    """

    pps = data_rate / packet_size_bits

    return pps