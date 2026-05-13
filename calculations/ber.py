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