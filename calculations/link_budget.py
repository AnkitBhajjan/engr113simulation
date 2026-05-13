import numpy as np
from config import *

def freeSpacePathLoss(distance_km=DISTANCE_KM, frequency_hz=FREQUENCY):
    """
    Calculate free space path loss using Friis equation.
    
    Parameters
    ----------
    distance_km : float or np.ndarray
        Distance between transmitter and receiver in kilometers (default from config)
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

def linkBudget(transmitter_power_dBW=TRANSMITTER_POWER, transmitter_gain_dBi=TRANSMITTER_GAIN, receiver_gain_dBi=RECEIVER_GAIN, distance_km=DISTANCE_KM):
    """
    Calculate the received power at the receiver using the link budget equation.
    
    Parameters
    ----------
    transmitter_power_dBW : float, optional
        Power of the transmitter in dBW (default from config)
    transmitter_gain_dBi : float, optional
        Gain of the transmitter antenna in dBi (default from config)
    receiver_gain_dBi : float, optional
        Gain of the receiver antenna in dBi (default from config)
    distance_km : float, optional
        Distance between transmitter and receiver in kilometers (default from config)
        
    Returns
    -------
    float
        Received power at the receiver in dBW
    """
    
    path_loss_dB = freeSpacePathLoss(distance_km)
    
    received_power_dBW = transmitter_power_dBW + transmitter_gain_dBi + receiver_gain_dBi - path_loss_dB - LOSS_MISC
    
    return received_power_dBW

def linkMargin(received_power_dBW=linkBudget(), receiver_threshold_dBW=RECIEVER_POWER_THRESHOLD):
    """
    Calculate the link margin in dB, which is the difference between the received power and the receiver sensitivity threshold.
    
    Parameters
    ----------
    received_power_dBW : float, optional
        Received power at the receiver in dBW (default calculated from link budget)
    receiver_threshold_dBW : float, optional
        Minimum power required at the receiver for successful communication in dBW (default from config)
        
    Returns
    -------
    float
        Link margin in dB
    """
    
    margin_dB = received_power_dBW - receiver_threshold_dBW
    
    return margin_dB