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


def simulate_one_stop_strategy(
    first_compound,
    second_compound,
    pit_lap
):

    stint_1_time = simulate_stint(
        1,
        pit_lap,
        first_compound
    )

    stint_2_time = simulate_stint(
        pit_lap + 1,
        race_laps,
        second_compound
    )

    total_time = (
        stint_1_time
        + pit_stop_loss
        + stint_2_time
    )

    return total_time

def optimise_one_stop():

    compounds = [
        "soft",
        "medium",
        "hard"
    ]

    best_time = float("inf")
    best_strategy = None

    results = []

    for first_compound in compounds:

        for second_compound in compounds:

            # Require a compound change
            if first_compound == second_compound:
                continue

            # Avoid unrealistic extremely early or extremely late stops
            for pit_lap in range(
                5,
                race_laps - 4
            ):

                race_time = (
                    simulate_one_stop_strategy(
                        first_compound,
                        second_compound,
                        pit_lap
                    )
                )

                result = {
                    "first_compound":
                        first_compound,

                    "second_compound":
                        second_compound,

                    "pit_lap":
                        pit_lap,

                    "race_time":
                        race_time
                }

                results.append(result)

                if race_time < best_time:

                    best_time = race_time

                    best_strategy = result

    return best_strategy, results

best_strategy, results = (
    optimise_one_stop()
)

print()
print(" One stop optimisation result")


print(
    f"Starting Compound: "
    f"{best_strategy['first_compound'].capitalize()}"
)

print(
    f"Second Compound: "
    f"{best_strategy['second_compound'].capitalize()}"
)

print(
    f"Pit Lap: "
    f"{best_strategy['pit_lap']}"
)

print(
    f"Race Time: "
    f"{best_strategy['race_time']:.3f} seconds"
)

sorted_results = sorted(
    results,
    key=lambda x: x["race_time"]
)

print()
print("Top 10 strategy")


for position, result in enumerate(
    sorted_results[:10],
    start=1
):

    print(
        f"{position:2d}. "
        f"{result['first_compound'].capitalize()}"
        f" -> "
        f"{result['second_compound'].capitalize()} | "
        f"Pit Lap {result['pit_lap']:2d} | "
        f"{result['race_time']:.3f} s"
    )
