# Circuit parameters

circuit_name = "Silverstone Grand Prix Circuit"
circuit_length = 5.891       # km
race_laps = 52
race_distance = 306.198      # km
base_lap_time = 88.0         # seconds


# Fuel parameters

starting_fuel = 105.0        # kg
fuel_per_lap = 1.9           # kg per lap
fuel_time_penalty = 0.035    # seconds per kg

# Pit-stop parameters

pit_stop_loss = 19.9         # seconds

# Tyre parameters

TYRES = {

    "soft": {
        "pace_offset": 0.00,
        "linear_deg": 0.025,
        "quadratic_deg": 0.0015
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

print("Silverstone Modelling Parameters")
print("-----------------------------")

print(f"Circuit: {circuit_name}")
print(f"Race laps: {race_laps}")
print(f"Base lap time: {base_lap_time} s")
print(f"Starting fuel: {starting_fuel} kg")
print(f"Fuel consumption: {fuel_per_lap} kg/lap")
print(f"Pit-stop loss: {pit_stop_loss} s")
