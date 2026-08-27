import matplotlib.pyplot as plt


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
        starting_fuel
        - (lap - 1) * fuel_per_lap,
        0
    )


def calculate_lap_time(
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


def simulate_stint(
    start_lap,
    end_lap,
    compound
):

    total_time = 0
    tyre_age = 0

    for lap in range(
        start_lap,
        end_lap + 1
    ):

        total_time += (
            calculate_lap_time(
                lap,
                compound,
                tyre_age
            )
        )

        tyre_age += 1

    return total_time


def simulate_strategy(
    first_compound,
    second_compound,
    pit_lap
):

    return (
        simulate_stint(
            1,
            pit_lap,
            first_compound
        )
        +
        PIT_STOP_LOSS
        +
        simulate_stint(
            pit_lap + 1,
            race_laps,
            second_compound
        )
    )

pit_laps = list(
    range(5, race_laps - 4)
)

race_times = []

for pit_lap in pit_laps:

    race_time = simulate_strategy(
        "medium",
        "hard",
        pit_lap
    )

    race_times.append(
        race_time
    )

plt.plot(
    pit_laps,
    race_times
)

plt.xlabel(
    "Pit-Stop Lap"
)

plt.ylabel(
    "Total Race Time (s)"
)

plt.title(
    "Medium to Hard Pit-Stop Optimisation"
)

plt.grid()

plt.show()

minimum_time = min(
    race_times
)

minimum_index = (
    race_times.index(
        minimum_time
    )
)

optimal_pit_lap = (
    pit_laps[minimum_index]
)

print(
    f"Optimal Medium -> Hard pit lap: "
    f"{optimal_pit_lap}"
)

print(
    f"Minimum race time: "
    f"{minimum_time:.3f} seconds"
)

plt.plot(
    pit_laps,
    race_times
)

plt.scatter(
    optimal_pit_lap,
    minimum_time
)

plt.xlabel(
    "Pit-Stop Lap"
)

plt.ylabel(
    "Total Race Time (s)"
)

plt.title(
    "Medium to Hard Pit-Stop Optimisation"
)

plt.grid()

plt.show()
