# ISS Link Budget and Data Transmission Simulator

A comprehensive simulation tool for analyzing ISS (International Space Station) communication capabilities through GEO (Geostationary Orbit) relay satellites. This project combines data transmission analysis with signal propagation modeling to evaluate link budgets and system performance.

## Project Overview

This project models the communication link between the ISS and ground control centers via GEO relay satellites. The current implementation calculates data transmission rates and visualizes coverage patterns. The extended link budget tool will simulate realistic signal degradation and propagation characteristics.

## Current Features

### Data Transmission Analysis
- **Orbital Parameters**: Configurable ISS orbital characteristics and GEO satellite positioning
- **Coverage Calculations**: Compute connected time and data transmission capacity based on satellite constellation size
- **Data Metrics**: Calculates total Megabits, Gigabits, and Gigabytes transmitted per ISS orbit

### Visualization
- **Bar Graph**: Comparative analysis of data transmission capacity across different satellite configurations (1, 2, or 3 GEO relay satellites)
- **Animated Simulation**: Real-time visualization of ISS trajectory and dynamic communication links with GEO satellites

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

Run the main simulation:
```bash
python engr113.py
```

This will:
1. Calculate data transmission for 1, 2, and 3 satellite configurations
2. Display connected time and data throughput statistics
3. Show percent increase comparisons between configurations
4. Display a bar graph comparing transmission capabilities
5. Show an animated visualization of the ISS orbit and satellite communication links

## Configuration Parameters

All simulation parameters are centralized in `config.py`, including:
- **Orbital Parameters**: ISS and GEO satellite altitudes, orbital period, data rate, and coverage percentages
- **Physical Constants**: Speed of light, receiver noise temperature, communication frequency (Ku-band), and bandwidth
- **Transmitter/Receiver Specs**: Antenna gains, transmit power, and receiver power threshold
- **System Losses**: Implementation margins, feeder loss, pointing loss, and receiver noise figures
- **Amplifier Characteristics**: LNA and mixer noise figures and gains

Modify these values to simulate different system configurations, frequency bands, or receiver designs.


## link_budget.py
This module manages the physical balance of the signal. It determiens how much raw power reaches the receiver after traveling through space.

### freeSpacePathLoss
Impliments the Friis transmission equation to calculate signal attenuation over distance.

$$ L_{path} = 20\log_{10}(\frac{4\pi df}{c}) $$

### linkBudget
Aggregates transmitter power, antenna gains, and miscellaneous system losses to find the final received power.

$$ Link Budget = P_t + G_t + G_r - L_{freespace} - L_{misc} $$

### linkMargin
Calculates buffer between reciever power and minimum required threshold

## snr.py
This module handles the component level calculations of the signal chain.

### Conversions
Contains conversion functions to transfer between linear and dB units.

### noisePower
Calculates the noise floor using the Boltzmann constant, system temperature, and bandwidth.

$$ P_N = kTB $$

### noiseFigureReciever
Uses the Friis formula to determine the total system noise factore based on the LNA and mixer.  Onlt the LNA and mixer are considered, as they are the dominant contributors to the overall noise figure of the system. The other components are assumed to have negligible noise figures for this analysis, but may be added in later implementations.

$$ F_{total} = F_{LNA} + \frac{F_{mixer} - 1}{G_{LNA}} $$

### recieverThreshold
Uses Shannon-Hartley theorem to determine the minimum power required to support target data rate and bandwidth, adding on constants to produce a realistic figure.

$$ SNR_{required} = 2^{\frac{R}{B}} - 1 $$


## AI Usage Statement

README and TODO initially generated with VSCode based claude, heavily modified to fit project. Code hand written with VSCode autofill at most.

# Authors
Ankit Bhajjan
Maxwell Costantino
