# Circuit parameters

circuit_name = "Silverstone Grand Prix Circuit"
circuit_length = 5.891       # km
race_laps = 52
race_distance = 306.198      # km
base_lap_time = 88.0         # seconds


# Fuel parameters: the consumption and time penalty are constant values

starting_fuel = 105.0        # kg at the start of the race
fuel_per_lap = 1.9           # kg consumed per completed lap
fuel_time_penalty = 0.035    # seconds added per kg of fuel carried (aka time lost)


# Extra time lost per stop relative to the car continuing on track
# Represents the total pit-stop time loss, not just stationary time

pit_stop_loss = 19.9         # seconds

# Tyre parameters
# Nested dictionary: each compound has its own pace and degradation values
# pace_offset var is the fresh tyre time difference relative to the soft tyres (seconds)
# linear_deg var is the coefficient multiplying tyre age (s/lap of tyre age)
# quadratic_deg var is the coefficient multiplying tyre age squared (s/lap²)

# TYRES is a nested dictionary containing 3 other dictionaries: soft, medium, hard
TYRES = {

    "soft": {
        "pace_offset": 0.00, # Reference compound: fastest when fresh
        "linear_deg": 0.025,
        "quadratic_deg": 0.0015 # Largest quadratic degradation coefficient of the tyres
    },

    "medium": {
        "pace_offset": 0.45, # 0.45 s slower than fresh softs
        "linear_deg": 0.018,
        "quadratic_deg": 0.0009
    },

    "hard": {
        "pace_offset": 0.90, # 0.90 s slower than fresh softs
        "linear_deg": 0.012,
        "quadratic_deg": 0.0005 # Smallest quadratic degradation coefficient
    }
}

# Display selected inputs
print("Silverstone Modelling Parameters")
print() # Print a blank line to improve readability

print(f"Circuit: {circuit_name}")
print(f"Race laps: {race_laps}")
print(f"Base lap time: {base_lap_time} s")
print(f"Starting fuel: {starting_fuel} kg")
print(f"Fuel consumption: {fuel_per_lap} kg/lap")
print(f"Pit-stop loss: {pit_stop_loss} s")
