## Overview

The race strategy simulator is intentionally simplified.

Its purpose is to investigate the effect of tyre degradation, fuel load and pit-stop timing on race strategy, rather than reproduce a complete Formula 1 race model.

The limitations below define where the current model may differ from real race behaviour.

---

## Tyre Model Limitations

The tyre degradation coefficients are assumed rather than derived from proprietary Formula 1 telemetry.

The model uses a simplified quadratic degradation relationship.

Real tyre performance may also depend on:

- Tyre temperature
- Track temperature
- Track surface condition
- Driving style
- Car setup
- Tyre pressure
- Thermal degradation
- Graining
- Blistering

These effects are not currently included.

---

## Fuel Model Limitations

Fuel consumption is assumed to be constant for every lap.

The effect of fuel mass on lap time is assumed to be linear.

In reality, fuel consumption and lap-time sensitivity may vary with:

- Driving style
- Engine mode
- Traffic
- Safety Car periods
- Track position
- Energy recovery strategy

These effects are not currently modelled.

---

## Pit-Stop Limitations

Pit-stop time loss is treated as a fixed value.

The model does not currently include:

- Variable stationary pit-stop time
- Pit-lane traffic
- Unsafe release delays
- Slow wheel changes
- Pit-entry variation
- Pit-exit traffic

As a result, every simulated pit stop has the same time penalty.

---

## Race Environment Limitations

The deterministic model does not include:

- Weather
- Rain
- Wind
- Track temperature changes
- Safety Car
- Virtual Safety Car
- Red flags
- Track evolution
- Yellow flags

These factors can have a major effect on real race strategy.

---

## Traffic and Overtaking Limitations

The model assumes each car can achieve its calculated lap time without interference.

It does not include:

- Traffic
- Dirty air
- Overtaking difficulty
- DRS
- Defensive driving
- Time lost behind slower cars

This means the simulator does not currently model track position.

---

## Driver Limitations

The deterministic model assumes perfect and repeatable driver performance.

The Monte Carlo model introduces random lap-time variation, but this is still a simplified representation.

The model does not include:

- Driver-specific pace
- Driver fatigue
- Mistakes
- Lock-ups
- Different tyre-management ability
- Different qualifying and race pace

---

## Vehicle Model Limitations

The simulator does not include detailed vehicle dynamics.

It does not currently model:

- Aerodynamic performance
- Suspension behaviour
- Tyre load sensitivity
- Brake temperatures
- Power-unit performance
- ERS deployment
- Mechanical failures
- Vehicle setup

The vehicle is represented through simplified lap-time relationships rather than a full physics model.

---

## Data Limitations

The model does not use proprietary Formula 1 telemetry.

Some model parameters are assumed or simplified.

As a result, the simulator should not be interpreted as an exact predictor of real Formula 1 race strategy.

Instead, it should be treated as a computational engineering model for studying strategy trade-offs.

---

## Computational Limitations

The optimisation currently uses brute-force search.

This is suitable for the current problem because the number of possible strategies is relatively small.

However, if more variables are introduced, such as:

- Weather
- Safety Car timing
- Track position
- Multiple drivers
- Variable tyre conditions

the search space could increase significantly.

More advanced optimisation methods may then become appropriate.
