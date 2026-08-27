This section implements the first complete race simulation.
The simulator is deterministic, meaning that the same inputs will always produce the same outputs.

The model combines:
- Fuel mass
- Fuel-related lap-time penalty
- Tyre compound
- Tyre degradation
- Lap time
- Stint time
- Pit-stop loss
- Total race time

No random race events are included yet

# Model Structure

TheI am going to be building this simulator in small sections so I can test each section independently:

1. Fuel model
2. Tyre model
3. Lap-time model
4. Stint simulator
5. Race simulator

# Deterministic Lap-Time Equation

The lap-time model is:

t_lap = t_base + Δt_fuel + Δt_tyre

where:

- t_base is the reference lap time
- Δt_fuel is the penalty caused by fuel mass
- Δt_tyre is the penalty caused by tyre compound and tyre degradation

# Purpose

The simulator will provide the foundation for later strategy optimisation.

At this stage, the user provides a tyre strategy and pit-stop timing, and the program will then calculate the resulting total race time.
