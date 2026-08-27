# Overview

The simulator produces the same race time every time for a given strategy.
Real races contain uncertainty.

Lap times vary due to factors such as:

- Small driver performance variations
- Minor differences in tyre behaviour
- Track conditions
- Small operational inconsistencies

To represent this uncertainty, a Monte Carlo simulation is introduced.

# Stochastic Lap-Time Model

The deterministic lap-time model is:

t_lap = t_base + Δt_fuel + Δt_tyre

The stochastic model becomes:

t_actual = t_deterministic + ε

where:

ε ~ N(0, σ)

and:

- ε is a random lap-time variation
- σ is the standard deviation of the variation

# Monte Carlo Method

For each race strategy:

1. Simulate a complete race.
2. Add random variation to each lap.
3. Record the resulting race time.
4. Repeat the race many times.
5. Analyse the distribution of race times.

This allows the expected performance and uncertainty of different race strategies to be compared.

# Outputs

The Monte Carlo model will calculate:

- Mean race time
- Standard deviation of race time
- Distribution of race times
- Probability that one strategy outperforms another

The deterministic optimiser identifies the theoretically fastest strategy.

The Monte Carlo model then evaluates how robust that strategy is when uncertainty is introduced.
