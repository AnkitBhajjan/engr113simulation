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

In `engr113.py`, modify the following parameters to adjust the simulation:

```python
DATA_RATE = 600          # Mbps - downlink data rate
ORBIT_TIME = 90 * 60     # seconds - ISS orbital period
EARTH_RADIUS = 1         # units - Earth radius (relative)
ISS_RADIUS = 1.3         # units - ISS orbital altitude (relative)
GEO_RADIUS = 2.2         # units - GEO orbital altitude (relative)
```

Coverage dictionary defines satellite constellation coverage percentages:
```python
coverage = {
    1: 0.35,  # 1 satellite covers 35%
    2: 0.70,  # 2 satellites cover 70%
    3: 0.99   # 3 satellites cover 99%
}
```

## Future Development

The link budget tool will extend this project with:
- Path loss calculations using NumPy arrays for vectorized operations
- Atmospheric and environmental effects modeling
- Antenna gain patterns and radiation diagrams
- Comprehensive link margin analysis
- Performance prediction under various conditions

## AI Usage Statement

# Authors
Ankit Bhajjan
Maxwell Costantino
