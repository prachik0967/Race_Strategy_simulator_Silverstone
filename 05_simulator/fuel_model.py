starting_fuel = 105.0        # kg
fuel_per_lap = 1.9           # kg per lap
fuel_time_deficit = 0.035    # seconds per kg

# Calculate the fuel mass at the start of a given race lap

def calculate_fuel_mass(lap):
    fuel_mass = (
        starting_fuel - (lap - 1) * fuel_per_lap
    )

    return max(fuel_mass, 0)

# Calculate the lap-time penalty caused by the current fuel mass

def calculate_fuel_penalty(lap):
    fuel_mass = calculate_fuel_mass(lap)

    fuel_penalty = (
        fuel_mass * fuel_time_deficit
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
