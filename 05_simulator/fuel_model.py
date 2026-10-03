# Fixed fuel assumptions
starting_fuel = 105.0        # Initial fuel load (kg)
fuel_per_lap = 1.9           # Constant fuel consumption (kg/lap)
fuel_time_deficit = 0.035    # Additional lap time per kg carried (s/kg)

# Calculate the fuel mass at the start of a given race lap

def calculate_fuel_mass(lap):
    # Lap numbering starts at 1
    # At the start of lap N, only N - 1 laps have been completed
    fuel_mass = (
        starting_fuel - (lap - 1) * fuel_per_lap
    )
    
    # return the calculated mass, with a lower limit of zero
    # This prevents negative values but still does not check fuel sufficiency
    return max(fuel_mass, 0) # this return command returns the largest of its arguments e.g max(8,0) returns 8

# Calculate the lap-time penalty caused by the current fuel mass

def calculate_fuel_penalty(lap):
    fuel_mass = calculate_fuel_mass(lap)
    # Reuse the fuel mass function for the requested race lap

    fuel_penalty = (
        fuel_mass * fuel_time_deficit
    # Convert fuel mass into additional lap time: kg × s/kg = s
    )

    return fuel_penalty


# Example checks

print("Fuel model check")

print(
    f"Lap 1 fuel: "
    f"{calculate_fuel_mass(1):.1f} kg"
)

print(
    f"Lap 26 fuel: "
    f"{calculate_fuel_mass(26):.1f} kg"
)

print(
    f"Lap 52 fuel: "
    f"{calculate_fuel_mass(52):.1f} kg"
)
