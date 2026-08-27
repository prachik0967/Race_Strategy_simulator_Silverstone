#one-stop race simulator

race_laps = 52
base_lap_time = 88.0

starting_fuel = 105.0
fuel_per_lap = 1.9
fuel_time_penalty = 0.035

pit_stop_loss = 19.9


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
        starting_fuel - (lap - 1) * fuel_per_lap,0
    )


def calculate_lap_time(
    lap,
    compound,
    tyre_age
):

    fuel_penalty = (
        calculate_fuel_mass(lap) * fuel_time_penalty
    )

    tyre = TYRES[compound]

    tyre_penalty = (
        tyre["pace_offset"]
        + tyre["linear_deg"] * tyre_age
        + tyre["quadratic_deg"] * tyre_age**2
    )

    return (
        base_lap_time + fuel_penalty + tyre_penalty
    )


def simulate_stint(
    start_lap,
    end_lap,
    compound
):

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
            "lap_time": lap_time
        })

        total_time += lap_time
        tyre_age += 1

    return total_time, lap_data


def simulate_one_stop_strategy(
    first_compound,
    second_compound,
    pit_lap
):

    stint_1_time, stint_1_data = (
        simulate_stint(
            1,
            pit_lap,
            first_compound
        )
    )

    stint_2_time, stint_2_data = (
        simulate_stint(
            pit_lap + 1,
            race_laps,
            second_compound
        )
    )

    total_time = (
        stint_1_time
        + pit_stop_loss
        + stint_2_time
    )

    race_data = (
        stint_1_data
        + stint_2_data
    )

    return total_time, race_data


def format_time(seconds):

    minutes = int(seconds // 60)

    remaining_seconds = (
        seconds % 60
    )

    return (
        f"{minutes}:"
        f"{remaining_seconds:06.3f}"
    )


# Example race strategy

race_time, race_data = (
    simulate_one_stop_strategy(
        "medium",
        "hard",
        20
    )
)



print("Silverstone race simulator")

print()
print("Strategy:")
print("Medium -> Hard")
print("Pit at end of Lap 20")

print()
print(
    f"Total Race Time: "
    f"{format_time(race_time)}"
)
