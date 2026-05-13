# Project TODO List

## Visualization - Refinements
- [ ] Output percent uptime for number of GEO to png for presentation
- [ ] Refactor into seperate functions for expandability
- [ ] Create function getDistance, use in simulation

## Visualization
- [ ] Create BER(dB) vs. SNR(dB) graph
- [ ] BER Curve
- 

## Simulation
- [ ] Pass distance to calculation functions to simulate realistic data transfer amounts

## Link Budget Tool
- [X] Create `link_budget.py` module
- [X] Implement free-space path loss calculation using NumPy
- [X] Calculate Friis transmission equation components
- [X] Create SNR (Signal-to-Noise Ratio) calculation functions
- [X] Implement link margin analysis

## SNR Analysis
- [X] Create `snr.py` module
- [X] Calculate receiver noise temperature
- [X] Implement noise figure calculations
- [ ] Create SNR vs. distance curves using NumPy arrays
- [ ] Model SNR degradation over time
- [ ] Generate SNR visualization plots with Matplotlib
- [ ] Implement SNR margin requirements for different modulation schemes
- [ ] Model thermal noise and interference effects
- [ ] Create SNR comparison tables for different configurations

## Bit Error Rate Module
- [ ] Calculate bit error rate (BER) curves
- [X] Determine adequate protocal
- [X] Implement Eb/N0 (Energy per bit / Noise power spectral density) calculations
- [X] Packet Error Rate
- [ ] Compression/Spirious DR

## Code Organization
- [x] Add constants module for physical parameters
- [ ] Create class structure for satellite objects
- [ ] Implement ISS and GEO satellite classes
- [ ] Update README


