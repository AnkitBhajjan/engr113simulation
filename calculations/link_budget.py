import numpy as np
from config import *

def freeSpacePathLoss(distance_km, frequency_hz=FREQUENCY):
    """
    Calculate free space path loss using Friis equation.
    
    Parameters
    ----------
    distance_km : float or np.ndarray
        Distance between transmitter and receiver in kilometers
    frequency_hz : float, optional
        Transmission frequency in Hz (default from config)
        
    Returns
    -------
    float or np.ndarray
        Path loss in dB
    """
    
    distance_m = distance_km * 1e3  # Convert km to m
    path_loss = 20 * np.log10((4 * np.pi * distance_m * frequency_hz) / C)

    return path_loss