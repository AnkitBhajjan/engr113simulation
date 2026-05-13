import sys
from pathlib import Path

# Add parent directory to path to import config
sys.path.insert(0, str(Path(__file__).parent.parent))

import numpy as np
from config import *
from calculations.link_budget import *

def dbToLinear(db):
    """
    Convert a value from decibels (dB) to linear scale.
    
    Parameters
    ----------
    db : float or np.ndarray
        Value in decibels to be converted
        
    Returns
    -------
    float or np.ndarray
        Value in linear scale
    """
    
    linear = 10 ** (db / 10)
    
    return linear

def linearToDb(linear):
    """
    Convert a value from linear scale to decibels (dB).
    
    Parameters
    ----------
    linear : float or np.ndarray
        Value in linear scale to be converted
        
    Returns
    -------
    float or np.ndarray
        Value in decibels
    """
    
    db = 10 * np.log10(linear)
    
    return db

def spectralEfficiency(data_rate=DATA_RATE, bandwidth=BANDWIDTH):
    """
    Calculate the spectral efficiency of the communication system in bits per second per hertz (bps/Hz) using Shannon's capacity formula.
    
    Parameters
    ----------
    data_rate : float, optional
        Data rate in bits per second (default from config)
    bandwidth : float, optional
        Bandwidth in Hz (default from config)
        
    Returns
    -------
    float
        Spectral efficiency in bps/Hz
    """
    
    spectral_efficiency = data_rate / bandwidth
    
    return spectral_efficiency

def noisePower(temperature=TEMPERATURE, bandwidth=BANDWIDTH):
    """
    Calculate the noise power in watts using the formula P = kTB, where k is Boltzmann's constant, T is the noise temperature in Kelvin, and B is the bandwidth in Hz.
    
    Parameters
    ----------
    temperature : float, optional
        Noise temperature in Kelvin (default from config)
    bandwidth : float, optional
        Bandwidth in Hz (default from config)
        
    Returns
    -------
    float
        Noise power in watts
    """
    
    noise_power = BOLTZMANN_CONSTANT * temperature * bandwidth
    
    return noise_power

def noiseFigureReciever():
    """
    Calculate the noise figure of the system using the noise figures of the individual components and the Friis formula for noise figure.
    
    Returns
    -------
    float
        Noise figure in dB

    Notes
    ------
    Uses constants in config.py for the noise figures of the individual components. The order of the components in the signal chain is the following:
        1. Bandpass Filter 
        2. Low Noise Amplifier (LNA)
        3. Mixer
        4. Filter 2
        5. Intermediate Frequency Amplifier (IFA)
        6. Balun
        7. Track and Hold Amplifier (THA)
        8. Analog-to-Digital Converter (ADC)
        9. FPGA (assumed to have negligible noise figure)

    In the current implementation, we will only consider the noise figures of the LNA and Mixer, as they are the dominant contributors to the overall noise figure of the system. The other components are assumed to have negligible noise figures for this analysis.
    """

    # Convert dB to linear
    nf_lna_linear = dbToLinear(LNA_NOISE_FACTOR)
    gain_lna_linear = dbToLinear(LNA_GAIN)

    nf_mixer_linear = dbToLinear(MIXER_NOISE_FACTOR)
    gain_mixer_linear = dbToLinear(MIXER_GAIN)

    # Friis formula for cascaded noise figure
    f_total = nf_lna_linear + (nf_mixer_linear - 1) / gain_lna_linear

    # Convert back to dB for readability
    nf_total_db = linearToDb(f_total)

    return nf_total_db

def signalToNoiseRatio(distance_km=DISTANCE_KM):
    """
    Calculate the signal-to-noise ratio (SNR) in decibels (dB) given the received power in dBW and the noise power in watts.
    
    Parameters
    ----------
    distance_km : float, optional
        Distance between transmitter and receiver in kilometers (default from config)
        
    Returns
    -------
    float
        Signal-to-noise ratio in dB
    """
    received_power_dBW = linkBudget(distance_km=distance_km)
    noise_power_watts = noisePower()
    
    # Convert received power from dBW to watts
    received_power_watts = dbToLinear(received_power_dBW)
    
    # Calculate SNR in linear scale
    snr_linear = received_power_watts / noise_power_watts
    
    # Convert SNR to dB
    snr_db = linearToDb(snr_linear)
    
    return snr_db

def recieverThreshold():
    """
    Calculate the minimum required received power at the receiver for successful communication, based on the noise figure of the receiver and the required SNR for the given data rate.
    
    Returns
    -------
    float
        Minimum required received power in dBW
    """
    
    # Calculate noise figure of the receiver
    nf_receiver_db = noiseFigureReciever()
    
    # Calculate noise power in watts
    noise_power_watts = noisePower()
    
    # Convert noise power to dBW
    noise_power_dBW = linearToDb(noise_power_watts)
    
    # Calculate required SNR for the given data rate using Shannon's capacity formula
    snr_required_linear = (2 ** (spectralEfficiency()) - 1)
    snr_required_db = linearToDb(snr_required_linear)
    
    # Calculate minimum required received power in dBW
    required_received_power_dBW = noise_power_dBW + nf_receiver_db + snr_required_db + SHANNON_GAP + IMPLEMENTATION_MARGIN
    
    return required_received_power_dBW