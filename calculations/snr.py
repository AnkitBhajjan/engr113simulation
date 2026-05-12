import numpy as np
from config import *

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

def cascadedNoiseFigureReciever():
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

    # Noise figures of individual components in dB
    noise_figure_LNA = LNA_NOISE_FACTOR
    noise_figure_Mixer = MIXER_NOISE_FACTOR - 1 / LNA_GAIN
    


    return 0