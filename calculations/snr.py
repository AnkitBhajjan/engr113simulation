import numpy as np
from config import *
import calculations.link_budget as link_budget

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

def signalToNoiseRatio():
    """
    Calculate the signal-to-noise ratio (SNR) in decibels (dB) given the received power in dBW and the noise power in watts.
    
    Parameters
    ----------
    received_power_dBW : float
        Received power at the receiver in dBW
    noise_power_watts : float
        Noise power in watts
        
    Returns
    -------
    float
        Signal-to-noise ratio in dB
    """
    received_power_dBW = linkBudget()
    noise_power_watts = noisePower()
    
    # Convert received power from dBW to watts
    received_power_watts = dbToLinear(received_power_dBW)
    
    # Calculate SNR in linear scale
    snr_linear = received_power_watts / noise_power_watts
    
    # Convert SNR to dB
    snr_db = linearToDb(snr_linear)
    
    return snr_db