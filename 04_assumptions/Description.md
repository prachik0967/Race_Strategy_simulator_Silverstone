I want this simulator to combine real data from the Silverstone circuit with simplified modelling assumptions.
These assumptions are necessary because tyre degradation data and detailed vehicle parameters are not publicly available for me to access.
The purpose of the model is therefore not to reproduce an exact F1 race, but to create a simplified engineering simulation that allows different race strategies to be compared consistently.

# Real Circuit Data

The model uses these Silverstone race parameters:

- Circuit length: 5.891 km
- Race laps: 52
- Race distance: 306.198 km

# Base Lap-Time Assumption

My model uses a baseline lap time of:

88.0 seconds

This represents a simplified reference lap time for a car using fresh Soft tyres and with no fuel-related lap-time deficit.
This value is a modelling reference and is not intended to represent an exact real-world race lap.

# Fuel Assumptions

The model assumes that:

- Starting fuel mass: 105 kg
- Fuel consumption: 1.9 kg per lap
- Fuel lap-time sensitivity: 0.035 seconds per kg

Fuel consumption is assumed to remain constant throughout the race.

The effect of fuel mass on lap time is assumed to be linear.

## Pit-Stop Assumption

The model assumes a fixed pit-stop time loss of:

19.9 seconds

This represents the total time lost relative to remaining on track.
The initial model assumes that this loss is identical for every pit stop.

# Tyre Assumptions

Three tyre compounds are modelled:

- Soft
- Medium
- Hard

Each compound has:

- A fresh-tyre pace offset
- A linear degradation coefficient
- A quadratic degradation coefficient

The initial assumed parameters are:

| Compound | Pace Offset (s) | Linear Degradation | Quadratic Degradation |
|----------|-----------------|--------------------|-----------------------|
| Soft | 0.00 | 0.025 | 0.0015 |
| Medium | 0.45 | 0.018 | 0.0009 |
| Hard | 0.90 | 0.012 | 0.0005 |

The Soft tyre is assumed to provide the greatest initial performance but degrade more rapidly.
The Hard tyre is assumed to provide the lowest initial performance but degrade more slowly.

# Simplifying Assumptions

The model assumes:

- Constant fuel consumption per lap
- Constant pit-stop loss
- No tyre temperature effects
- No tyre warm-up phase
- No track evolution
- No traffic effects
- No overtaking effects
- No weather changes
- No Safety Car or Virtual Safety Car
- No driver errors
- No mechanical failures

These assumptions allow the core relationship between tyre degradation, fuel load and pit-stop strategy to be studied before any additional complexity is introduced.
