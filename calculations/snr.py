import numpy as np
from config import *

def cascadedNoiseFigure():
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
    
    return noise_figure_dB