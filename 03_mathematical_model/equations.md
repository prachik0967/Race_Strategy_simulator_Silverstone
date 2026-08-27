# Fuel Mass

m_f(n) = m_start - (n - 1)m_lap

# Fuel Lap-Time Penalty

Δt_fuel = k_f × m_f

# Tyre Degradation

Δt_tyre = C + aA + bA²

# Lap Time

t_lap = t_base + Δt_fuel + Δt_tyre

&

t_lap = t_base + k_f m_f + C + aA + bA²

# Stint Time

T_stint = Σ t_lap

# Total Race Time

T_race = Σ t_lap + Σ T_pit
