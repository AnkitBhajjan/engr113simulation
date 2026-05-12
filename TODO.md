# Project TODO List

## Current Features - Refinements
- [ ] Add input validation for coverage dictionary values
- [ ] Implement error handling for invalid data rate or orbit time values
- [ ] Add docstrings to all functions using NumPy style
- [ ] Optimize animation frame rate and performance
- [ ] Add command-line argument parsing for configuration parameters
- [ ] Implement logging for data transmission calculations
- [ ] Add distance for GEO to ISS animation

## Link Budget Tool
- [ ] Create `link_budget.py` module
- [ ] Implement free-space path loss calculation using NumPy
- [ ] Calculate Friis transmission equation components
- [ ] Model atmospheric attenuation effects
- [ ] Implement multipath propagation effects
- [ ] Create SNR (Signal-to-Noise Ratio) calculation functions
- [ ] Implement link margin analysis
- [ ] Calculate bit error rate (BER) curves

## SNR Analysis
- [ ] Calculate receiver noise temperature
- [ ] Implement noise figure calculations
- [ ] Create SNR vs. distance curves using NumPy arrays
- [ ] Model SNR degradation over time
- [ ] Implement Eb/N0 (Energy per bit / Noise power spectral density) calculations
- [ ] Create SNR threshold analysis
- [ ] Generate SNR visualization plots with Matplotlib
- [ ] Implement SNR margin requirements for different modulation schemes
- [ ] Model thermal noise and interference effects
- [ ] Create SNR comparison tables for different configurations

## Signal Propagation Module
- [ ] Create `propagation.py` module
- [ ] Implement distance-dependent path loss models
- [ ] Model rain attenuation for different frequencies
- [ ] Add ionospheric effects calculation
- [ ] Create antenna gain pattern functions
- [ ] Implement polarization mismatch loss calculations

## Testing & Validation
- [ ] Create unit tests for link budget calculations
- [ ] Validate results against theoretical models
- [ ] Test edge cases (minimum/maximum distances)
- [ ] Verify NumPy calculations with alternative methods
- [ ] Add integration tests for complete workflows

## Code Organization
- [ ] Refactor main simulation into functions (URGENT)
- [x] Add constants module for physical parameters
- [ ] Create class structure for satellite objects
- [ ] Implement ISS and GEO satellite classes

## Documentation
- [ ] Add detailed docstrings to all functions
- [ ] Create API documentation
- [ ] Add example notebooks or scripts
- [ ] Document mathematical models used
- [ ] Create troubleshooting guide

