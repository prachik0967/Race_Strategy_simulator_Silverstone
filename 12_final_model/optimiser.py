from config import race_laps
from strategy import (
    simulate_one_stop_strategy,
    simulate_two_stop_strategy
)


COMPOUNDS = [
    "soft",
    "medium",
    "hard"
]


# one stop optimisation

def optimise_one_stop():
    # Search all valid one-stop strategies and return the fastest result.
 
    best_time = float("inf")
    best_strategy = None

    results = []

    for compound_1 in COMPOUNDS:

        for compound_2 in COMPOUNDS:

            if compound_1 == compound_2:
                continue

            for pit_lap in range(
                5,
                race_laps - 4
            ):

                race_time, _ = (
                    simulate_one_stop_strategy(
                        compound_1,
                        compound_2,
                        pit_lap
                    )
                )

                result = {
                    "compound_1": compound_1,
                    "compound_2": compound_2,
                    "pit_lap": pit_lap,
                    "race_time": race_time
                }

                results.append(
                    result
                )

                if race_time < best_time:

                    best_time = race_time
                    best_strategy = result

    return best_strategy, results


# two stop optimisation

def optimise_two_stop():
    # Search all valid two-stop strategies and return the fastest result.

    best_time = float("inf")
    best_strategy = None

    results = []

    for compound_1 in COMPOUNDS:

        for compound_2 in COMPOUNDS:

            for compound_3 in COMPOUNDS:

                # At least two different compounds must be used

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

                        race_time, _ = (
                            simulate_two_stop_strategy(
                                compound_1,
                                compound_2,
                                compound_3,
                                pit_1,
                                pit_2
                            )
                        )

                        result = {
                            "compound_1":
                                compound_1,

                            "compound_2":
                                compound_2,

                            "compound_3":
                                compound_3,

                            "pit_1":
                                pit_1,

                            "pit_2":
                                pit_2,

                            "race_time":
                                race_time
                        }

                        results.append(
                            result
                        )

                        if race_time < best_time:

                            best_time = race_time
                            best_strategy = result

    return best_strategy, results


# overall comparison

def compare_stop_strategies():
    
    # Compare the optimal one-stop and two-stop strategies


    best_one_stop, one_stop_results = (
        optimise_one_stop()
    )

    best_two_stop, two_stop_results = (
        optimise_two_stop()
    )

    if (
        best_one_stop["race_time"]
        < best_two_stop["race_time"]
    ):

        overall_best = {
            "strategy_type": "one-stop",
            "strategy": best_one_stop,
            "advantage": (
                best_two_stop["race_time"]
                - best_one_stop["race_time"]
            )
        }

    else:

        overall_best = {
            "strategy_type": "two-stop",
            "strategy": best_two_stop,
            "advantage": (
                best_one_stop["race_time"]
                - best_two_stop["race_time"]
            )
        }

    return {
        "best_one_stop": best_one_stop,
        "best_two_stop": best_two_stop,
        "overall_best": overall_best,
        "one_stop_results": one_stop_results,
        "two_stop_results": two_stop_results
    }
