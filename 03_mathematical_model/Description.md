Estimating lap time using a simplified  model.
The model assumes that lap time is primarily affected by:

- Base vehicle pace
- Fuel mass
- Tyre compound
- Tyre degradation

The basic lap-time equation is:

**t_lap = t_base + Δt_fuel + Δt_tyre**

where:

- t_lap = predicted lap time
- t_base = baseline lap time
- Δt_fuel = lap-time penalty caused by fuel mass
- Δt_tyre = lap-time penalty caused by tyre compound and degradation

# Fuel Model

Mass of the fuel decreases as the race progresses.
The fuel mass at lap 'n' is modelled as:

m_f(n) = m_start - (n - 1)m_lap

where:

- m_f = current fuel mass
- m_start = starting fuel mass
- m_lap = fuel consumed per lap
- n = race lap

The lap-time deficit caused by the mass of the fuel is assumed to be linear:

Δt_fuel = k_f × m_f

where:

- k_f = fuel sensitivity coefficient
- m_f = current fuel mass

---

# Tyre Model

Three compounds are used to model tyre performance:

- Soft
- Medium
- Hard

Each compound has:

- A fresh tyre pace offset
- A linear degradation coefficient
- A quadratic degradation coefficient

The tyre deficit is calculated using:

Δt_tyre = C + aA + bA²

where:

- C = tyre compound pace offset
- A = tyre age in laps
- a = linear degradation coefficient
- b = quadratic degradation coefficient

The quadratic term is introduced into the equation to allow degradation to increase more rapidly during longer stints.

# Complete Lap-Time Model

t_lap = t_base + k_f * m_f + C + aA + bA²


# Stint Time

A stint is the total time spent on one set of tyres.
The stint time is:

T_stint = Σ t_lap

for every lap completed within that stint.

# Race Time

Total race time is:

T_race = Σ t_lap + Σ T_pit

where:

- T_race = total simulated race time
- T_pit = time lost during pit stops

This is crucial cause this allows different tyre strategies and pit-stop timings to be compared.
