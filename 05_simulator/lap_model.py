# Reference time with fresh soft tyres and zero modelled fuel penalty
base_lap_time = 88.0

# Fuel assumptions: consumption and time penalty are constant
starting_fuel = 105.0 # kg at the start of the race
fuel_per_lap = 1.9 # kg consumed per completed lap
fuel_time_penalty = 0.035 # seconds added per kg of fuel carried

# Extra time lost per stop relative to continuing on track
# Represents the total pit-stop time loss, not just stationary time
pit_stop_loss = 19.9         # seconds

# Nested dictionary
# Compound-specific coefficients for the tyre model
TYRES = {

    "soft": {
        "pace_offset": 0.00,
        "linear_deg": 0.025, # s per lap of tyre age
        "quadratic_deg": 0.0015 # s per lap of tyre age squared
    },

    "medium": {
        "pace_offset": 0.45,
        "linear_deg": 0.018,
        "quadratic_deg": 0.0009
    },

    "hard": {
        "pace_offset": 0.90,
        "linear_deg": 0.012,
        "quadratic_deg": 0.0005
    }
}


def calculate_fuel_mass(lap):
# At the start of race lap N, N - 1 laps have been completed
    fuel_mass = (
        starting_fuel - (lap - 1) * fuel_per_lap
    )
     # Prevent negative mass
     # however this does not check whether the race is feasible
    return max(fuel_mass, 0)


def calculate_fuel_penalty(lap):
# Calculate fuel mass and convert it into additional lap time (seconds)
    return (
        calculate_fuel_mass(lap) * fuel_time_penalty
    )


def calculate_tyre_penalty(compound,tyre_age):
# Select the coefficient dictionary for the requested compound
    tyre = TYRES[compound]

    # Add the fresh compound offset and age related degradation (seconds)
    return (
        tyre["pace_offset"] + tyre["linear_deg"] * tyre_age + tyre["quadratic_deg"] * tyre_age**2
    )


def calculate_lap_time(lap,compound, tyre_age):

    # Fuel depends on overall race progress
    fuel_penalty = (
        calculate_fuel_penalty(lap)
    )
    
# Tyre performance depends on compound and age of the current set
    tyre_penalty = (
        calculate_tyre_penalty(compound,tyre_age)
    )

    
# Combine the reference time with independent fuel and tyre effects
    lap_time = (
        base_lap_time + fuel_penalty + tyre_penalty
    )
    
  # Return the predicted time in seconds
    return lap_time


# Example calculation: first race lap on soft tyres

lap_time = calculate_lap_time(
    lap=1,
    compound="soft",
    tyre_age=0
)

#displayed up to 3 sigfig
print(
    f"Lap 1 predicted time: "
    f"{lap_time:.3f} seconds"
)
