from config import (
    base_lap_time,
    starting_fuel,
    fuel_per_lap,
    fuel_time_penalty
)

from tyres import calculate_tyre_penalty


def calculate_fuel_mass(lap):
    # Calculate fuel mass at the start of a race lap.

    if lap < 1:
        raise ValueError(
            "Lap number must be at least 1."
        )

    fuel_mass = (
        starting_fuel
        - (lap - 1) * fuel_per_lap
    )

    return max(
        fuel_mass,
        0
    )


def calculate_fuel_penalty(lap):
    # Calculate lap-time penalty due to fuel mass.

    return (
        calculate_fuel_mass(lap)
        * fuel_time_penalty
    )


def calculate_lap_time(
    lap,
    compound,
    tyre_age
):

    # Calculate deterministic lap time.
 

    return (
        base_lap_time
        + calculate_fuel_penalty(lap)
        + calculate_tyre_penalty(
            compound,
            tyre_age
        )
    )


def simulate_stint(
    start_lap,
    end_lap,
    compound
):
    # Simulate a complete tyre stint.

    total_time = 0
    tyre_age = 0
    lap_data = []

    for lap in range(
        start_lap,
        end_lap + 1
    ):

        lap_time = calculate_lap_time(
            lap,
            compound,
            tyre_age
        )

        lap_data.append({
            "lap": lap,
            "compound": compound,
            "tyre_age": tyre_age,
            "fuel_mass":
                calculate_fuel_mass(lap),
            "lap_time":
                lap_time
        })

        total_time += lap_time
        tyre_age += 1

    return total_time, lap_data
