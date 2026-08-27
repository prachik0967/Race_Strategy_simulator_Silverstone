import random

base_lap_time = 88.0

starting_fuel = 105.0
fuel_per_lap = 1.9
fuel_time_penalty = 0.035

driver_variability = 0.20


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


def calculate_fuel_mass(lap):

    return max(
        starting_fuel
        - (lap - 1) * fuel_per_lap,
        0
    )


def calculate_deterministic_lap_time(
    lap,
    compound,
    tyre_age
):

    fuel_penalty = (
        calculate_fuel_mass(lap)
        * fuel_time_penalty
    )

    tyre = TYRES[compound]

    tyre_penalty = (
        tyre["pace_offset"]
        + tyre["linear_deg"] * tyre_age
        + tyre["quadratic_deg"] * tyre_age**2
    )

    return (
        base_lap_time
        + fuel_penalty
        + tyre_penalty
    )


def calculate_stochastic_lap_time(
    lap,
    compound,
    tyre_age
):

    deterministic_time = (
        calculate_deterministic_lap_time(
            lap,
            compound,
            tyre_age
        )
    )

    random_variation = random.gauss(
        0,
        driver_variability
    )

    stochastic_time = (
        deterministic_time
        + random_variation
    )

    return stochastic_time


# Example comparison

deterministic = (
    calculate_deterministic_lap_time(
        10,
        "medium",
        9
    )
)

stochastic = (
    calculate_stochastic_lap_time(
        10,
        "medium",
        9
    )
)

print()
print("Stochastic lap time model")
print("--------------------")

print(
    f"Deterministic lap time: "
    f"{deterministic:.3f} s"
)

print(
    f"Stochastic lap time: "
    f"{stochastic:.3f} s"
)
