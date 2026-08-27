# one stop vs two stop comparison

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


# Core model

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

        total_time += calculate_lap_time(
            lap,
            compound,
            tyre_age
        )

        tyre_age += 1

    return total_time

# one stop simulation

def simulate_one_stop_strategy(
    compound_1,
    compound_2,
    pit_lap
):

    stint_1 = simulate_stint(
        1,
        pit_lap,
        compound_1
    )

    stint_2 = simulate_stint(
        pit_lap + 1,
        race_laps,
        compound_2
    )

    return (
        stint_1
        + stint_2
        + pit_stop_loss
    )

# two stop simulation

def simulate_two_stop_strategy(
    compound_1,
    compound_2,
    compound_3,
    pit_1,
    pit_2
):

    stint_1 = simulate_stint(
        1,
        pit_1,
        compound_1
    )

    stint_2 = simulate_stint(
        pit_1 + 1,
        pit_2,
        compound_2
    )

    stint_3 = simulate_stint(
        pit_2 + 1,
        RACE_LAPS,
        compound_3
    )

    return (
        stint_1
        + stint_2
        + stint_3
        + 2 * pit_stop_loss
    )

# one stop optimiser

def optimise_one_stop():

    compounds = [
        "soft",
        "medium",
        "hard"
    ]

    best_time = float("inf")
    best_strategy = None

    for compound_1 in compounds:

        for compound_2 in compounds:

            if compound_1 == compound_2:
                continue

            for pit_lap in range(
                5,
                race_laps - 4
            ):

                race_time = (
                    simulate_one_stop_strategy(
                        compound_1,
                        compound_2,
                        pit_lap
                    )
                )

                if race_time < best_time:

                    best_time = race_time

                    best_strategy = {
                        "compound_1": compound_1,
                        "compound_2": compound_2,
                        "pit_lap": pit_lap,
                        "race_time": race_time
                    }

    return best_strategy


# two stop optimiser

def optimise_two_stop():

    compounds = [
        "soft",
        "medium",
        "hard"
    ]

    best_time = float("inf")
    best_strategy = None

    for compound_1 in compounds:

        for compound_2 in compounds:

            for compound_3 in compounds:

                unique_compounds = {
                    compound_1,
                    compound_2,
                    compound_3
                }

                if len(unique_compounds) < 2:
                    continue

                for pit_1 in range(
                    5,
                    race_laps - 10
                ):

                    for pit_2 in range(
                        pit_1 + 5,
                        race_laps - 4
                    ):

                        race_time = (
                            simulate_two_stop_strategy(
                                compound_1,
                                compound_2,
                                compound_3,
                                pit_1,
                                pit_2
                            )
                        )

                        if race_time < best_time:

                            best_time = race_time

                            best_strategy = {
                                "compound_1": compound_1,
                                "compound_2": compound_2,
                                "compound_3": compound_3,
                                "pit_1": pit_1,
                                "pit_2": pit_2,
                                "race_time": race_time
                            }

    return best_strategy

# run both optimisers

best_one_stop = optimise_one_stop()

best_two_stop = optimise_two_stop()


# display results
print()
print("one stops vs two stop")

print()
print("Best One-Stop Strategy")

print(
    f"{best_one_stop['compound_1'].capitalize()}"
    f" -> "
    f"{best_one_stop['compound_2'].capitalize()}"
)

print(
    f"Pit Lap: "
    f"{best_one_stop['pit_lap']}"
)

print(
    f"Race Time: "
    f"{best_one_stop['race_time']:.3f} s"
)


print()
print("Best Two-Stop Strategy")

print(
    f"{best_two_stop['compound_1'].capitalize()}"
    f" -> "
    f"{best_two_stop['compound_2'].capitalize()}"
    f" -> "
    f"{best_two_stop['compound_3'].capitalize()}"
)

print(
    f"Pit Laps: "
    f"{best_two_stop['pit_1']} and "
    f"{best_two_stop['pit_2']}"
)

print(
    f"Race Time: "
    f"{best_two_stop['race_time']:.3f} s"
)


# determine overall best strategy

if (
    best_one_stop["race_time"]
    < best_two_stop["race_time"]
):

    advantage = (
        best_two_stop["race_time"]
        - best_one_stop["race_time"]
    )

    print()
    print("Overal result")
    print("One-stop strategy is faster.")

    print(
        f"Advantage: "
        f"{advantage:.3f} seconds"
    )

else:

    advantage = (
        best_one_stop["race_time"]
        - best_two_stop["race_time"]
    )

    print()
    print("overall result")
    print("Two-stop strategy is faster.")

    print(
        f"Advantage: "
        f"{advantage:.3f} seconds"
    )
