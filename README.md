# ISS Link Budget and Data Transmission Simulator

A comprehensive simulation tool for analyzing ISS (International Space Station) communication capabilities through GEO (Geostationary Orbit) relay satellites. This project combines data transmission analysis with signal propagation modeling to evaluate link budgets and system performance.

## Project Overview

This project models the communication link between the ISS and ground control centers via GEO relay satellites. The current implementation calculates data transmission rates and visualizes coverage patterns. The extended link budget tool will simulate realistic signal degradation and propagation characteristics.

## Current Features

### Data Transmission Analysis
- **Orbital Parameters**: Configurable ISS orbital characteristics and GEO satellite positioning
- **Coverage Calculations**: Compute connected time and data transmission capacity based on satellite constellation size
- **Data Metrics**: Calculates total Megabits, Gigabits, and Gigabytes transmitted per ISS orbit
- **Code Rate Modeling**: Separates net data rate from gross transmitted data rate for error correction overhead

### Visualization
- **Bar Graph**: Comparative analysis of data transmission capacity across different satellite configurations (1, 2, or 3 GEO relay satellites)
- **Animated Simulation**: Real-time visualization of ISS trajectory and dynamic communication links with GEO satellites
- **Presentation Graphs**: Link margin, free space path loss, SNR, and packet error rate curves

## Dependencies

```
numpy>=1.20.0
matplotlib>=3.3.0
```

## Installation

1. Clone or download the repository:
```bash
cd engr113simulation
```

2. Install required dependencies:
```bash
pip install numpy matplotlib
```

## Usage

### Current Implementation

Run the calculation report:
```bash
python calculations/calculation_harness.py
```

Run the data visualization and handoff animation:
```bash
python visualization/data_visualization.py
```

Run the presentation graphs:
```bash
python visualization/ppt_graphs.py
```

These scripts will:
1. Calculate data transmission for 1, 2, and 3 satellite configurations
2. Display connected time and data throughput statistics
3. Show percent increase comparisons between configurations
4. Print grouped link budget, SNR, receiver threshold, BER, PER, and throughput calculations
5. Display graphs for transmission capacity, link margin, path loss, SNR, and PER
6. Show an animated visualization of the ISS orbit and satellite communication links

## Configuration Parameters

All simulation parameters are centralized in `config.py`, including:
- **Orbital Parameters**: ISS and GEO satellite altitudes, orbital period, data rate, and coverage percentages
- **Physical Constants**: Speed of light, receiver noise temperature, communication frequency (Ku-band), and bandwidth
- **Coding Parameters**: Net data rate, code rate, gross transmitted data rate, bits per symbol, baud rate, packet size, and occupied bandwidth
- **Transmitter/Receiver Specs**: Antenna gains, transmit power, and receiver power threshold
- **System Losses**: Implementation margins, feeder loss, pointing loss, and receiver noise figures
- **Amplifier Characteristics**: LNA and mixer noise figures and gains

Modify these values to simulate different system configurations, frequency bands, or receiver designs.

### Code Rate Implementation
The model now separates the useful data rate from the gross transmitted data rate by applying the code rate. `DATA_RATE` is the net information rate, while `R_GROSS` is the physical channel rate needed after forward error correction overhead is included.

$$ R_{gross} = \frac{R_{data}}{R_{code}} $$

The baud rate is calculated from the gross rate and the configured bits-per-symbol value.

$$ R_s = \frac{R_{gross}}{\log_2(N_{bps})} $$

The occupied bandwidth uses the baud rate and roll-off factor currently configured in `config.py`.

$$ B_{occupied} = R_s + \alpha $$

Future implementations will propogate this update to BER calculations.

## snr.py
This module handles the component level calculations of the signal chain.

### Conversions
Contains conversion functions to transfer between linear and dB units according to the logarithmic scale.

### dbToLinear
Converts a value in decibels to linear scale.

$$ x_{linear} = 10^{\frac{x_{dB}}{10}} $$

### linearToDb
Converts a linear value to decibels.

$$ x_{dB} = 10\log_{10}(x_{linear}) $$

### spectralEfficiency
Calculates the effective bits per symbol after coding is applied. The code uses packet sizing to estimate the modulation information content and then applies the code rate.

$$ \eta = \log_2(N_{packet})R_{code} $$

### noisePower
Calculates the noise floor using the Boltzmann constant, system temperature, and bandwidth.

$$ P_N = kTB $$

### noiseFigureReciever
Uses the Friis formula to determine the total system noise factor based on the LNA and mixer.  

Only the Bandpass filter, the LNA, and mixer are considered, as they are the dominant contributors to the overall noise figure of the system. The other components are assumed to have negligible noise figures for this analysis, but will be added in later implementations.

$$ F_{total} = F_1 + \frac{F_2-1}{G_1} + \frac{F_3-1}{G_1 G_2} + \frac{F_4-1}{G_1 G_2 G_3} + \cdots + \frac{F_n - 1}{G_1 G_2 \cdots G_{n-1}} $$

### signalToNoiseRatio
The signal to noise ratio is the comparison of the strength of a desired signal to the level of background noise. A higher SNR indicates a clearer signal, while a lower SNR means the noise is more prominent.

$$ SNR = \frac{P_{signal}}{P_{noise}} $$

### receiverThreshold
Uses Shannon-Hartley theorem to determine the minimum power required to support target data rate and bandwidth, adding on constants to produce a realistic figure. The required SNR uses the gross data rate and code rate so that error correction overhead is included in the link requirement.

$$ SNR_{required} = 2^{\frac{R_{gross}}{BR_{code}}} - 1 $$

$$ P_{threshold,dBW} = P_{N,dBW} + NF_{receiver} + SNR_{required,dB} + G_{Shannon} + M_{implementation} $$

## link_budget.py
This module manages the physical balance of the signal. It determines how much raw power reaches the receiver after traveling through space.

### freeSpacePathLoss
Impliments the Friis transmission equation to calculate signal attenuation over distance.

$$ L_{path} = 20\log_{10}(\frac{4\pi df}{c}) $$

### linkBudget
Aggregates transmitter power, antenna gains, and miscellaneous system losses to find the final received power.

$$ Link Budget = P_t + G_t + G_r - L_{freespace} - L_{misc} $$

### linkMargin
Calculates buffer between receiver power and minimum required threshold

$$ M_{link} = P_{received} - P_{threshold} $$

## ber.py
This module contains the data based calculations for the system.

### snrToBit
Normalizes SNR into energy per bit to noise density ratio using spectral efficiency.

$$ \frac{E_b}{N_0}_{dB} = SNR_{dB} - 10\log_{10}(\eta) $$

### snrToSymbol
Normalizes SNR into energy per symbol to noise density ratio using spectral efficiency, bandwidth, and baud rate.

$$ \frac{E_s}{N_0}_{dB} = SNR_{dB} - 10\log_{10}\left(\frac{\eta B}{R_s}\right) $$

### bitErrorRate
Estimates bit error rate from normalized SNR, with a small error margin to keep the BER from becoming exactly zero.

$$ BER = 0.5e^{-\frac{(E_b/N_0)_{linear}}{10}} + \epsilon $$

### packetErrorRate
Calculates packet error rate from bit error rate and packet size, assuming independent bit errors.

$$ PER = 1 - (1 - BER)^{N_{packet}} $$

### packetTransmissionTime
Calculates the time required to transmit one packet at the gross channel data rate.

$$ t_{packet} = \frac{N_{packet}}{R_{gross}} $$

### packetsPerSecond
Calculates how many packets can be transmitted per second using the gross channel data rate.

$$ PPS = \frac{R_{gross}}{N_{packet}} $$

## calculation_harness.py
This module prints a grouped report of the current system constants and all major calculated values. It starts with constants chosen from system needs, then groups calculated outputs by RF link budget, receiver noise, capacity and link margin, error rates, data throughput, and time in view.

### print_section
Prints a section title and underline to keep the calculation report grouped consistently.

## visualization
The visualization modules generate plots and animations for project presentation.

### data_visualization.py
Creates the data transmission comparison graph and ISS-to-GEO handoff animation. The animation update function moves the ISS through the orbit, determines the closest GEO relay satellite, and shows handoff overlap links.

### ppt_graphs.py
Creates presentation graphs for link margin, path loss, SNR, and packet error rate curves.

## AI Usage Statement

README and TODO initially generated with VSCode based claude, heavily modified to fit project. Code hand written with VSCode autofill at most.

# Authors
Ankit Bhajjan
Maxwell Costantino
