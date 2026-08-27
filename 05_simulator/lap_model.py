base_lap_time = 88.0

starting_fuel = 105.0
fuel_per_lap = 1.9
fuel_time_per_penalty = 0.035


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

    fuel_mass = (
        starting_fuel - (lap - 1) * fuel_per_lap
    )
    return max(fuel_mass, 0)


def calculate_fuel_penalty(lap):

    return (
        calculate_fuel_mass(lap) * fuel_time_per_penalty
    )


def calculate_tyre_penalty(
    compound,
    tyre_age
):

    tyre = TYRES[compound]

    return (
        tyre["pace_offset"]
        + tyre["linear_deg"] * tyre_age
        + tyre["quadratic_deg"] * tyre_age**2
    )


def calculate_lap_time(
    lap,
    compound,
    tyre_age
):

    fuel_penalty = (
        calculate_fuel_penalty(lap)
    )

    tyre_penalty = (
        calculate_tyre_penalty(
            compound,
            tyre_age
        )
    )

    lap_time = (
        base_lap_time + fuel_penalty + tyre_penalty
    )

    return lap_time


# Example calculation

lap_time = calculate_lap_time(
    lap=1,
    compound="soft",
    tyre_age=0
)

print(
    f"Lap 1 predicted time: "
    f"{lap_time:.3f} seconds"
)
