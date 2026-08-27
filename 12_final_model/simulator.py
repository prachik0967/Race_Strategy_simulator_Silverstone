
# Circuit

circuit_name = "Silverstone Grand Prix Circuit"

circuit_length = 5.891       # km
race_laps = 52
race_distance = 306.198      # km


# Base pace


base_lap_time = 88.0         # seconds


# fuel model

starting_fuel = 105.0        # kg
fuel_per_lap = 1.9           # kg/lap
fuel_time_penalty = 0.035    # seconds/kg


# pit stop

pit_stop_loss = 19.9         # seconds



# Monte Carlo


driver_variability = 0.20    # seconds standard deviation


# Tyre compounds

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
