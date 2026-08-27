from config import (
    race_laps,
    pit_stop_loss
)

from race import simulate_stint


def simulate_one_stop_strategy(
    compound_1,
    compound_2,
    pit_lap
):
    # Simulate a one-stop race strategy.
  

    if pit_lap <= 0 or pit_lap >= race_laps:
        raise ValueError(
            "Pit lap must be within the race."
        )

    if compound_1 == compound_2:
        raise ValueError(
            "One-stop strategy must use "
            "two different compounds."
        )

    stint_1_time, stint_1_data = (
        simulate_stint(
            1,
            pit_lap,
            compound_1
        )
    )

    stint_2_time, stint_2_data = (
        simulate_stint(
            pit_lap + 1,
            Race_laps,
            compound_2
        )
    )

    total_time = (
        stint_1_time
        + stint_2_time
        + pit_stop_loss
    )

    race_data = (
        stint_1_data
        + stint_2_data
    )

    return total_time, race_data


def simulate_two_stop_strategy(
    compound_1,
    compound_2,
    compound_3,
    pit_1,
    pit_2
):
   
  
  # Simulate a two-stop race strategy.


    if pit_1 <= 0:
        raise ValueError(
            "First pit lap is invalid."
        )

    if pit_2 >= RACE_LAPS:
        raise ValueError(
            "Second pit lap is invalid."
        )

    if pit_2 <= pit_1:
        raise ValueError(
            "Second pit stop must occur "
            "after the first."
        )

    compounds = {
        compound_1,
        compound_2,
        compound_3
    }

    if len(compounds) < 2:
        raise ValueError(
            "At least two tyre compounds "
            "must be used."
        )

    stint_1_time, stint_1_data = (
        simulate_stint(
            1,
            pit_1,
            compound_1
        )
    )

    stint_2_time, stint_2_data = (
        simulate_stint(
            pit_1 + 1,
            pit_2,
            compound_2
        )
    )

    stint_3_time, stint_3_data = (
        simulate_stint(
            pit_2 + 1,
            race_laps,
            compound_3
        )
    )

    total_time = (
        stint_1_time
        + stint_2_time
        + stint_3_time
        + 2 * pit_stop_loss
    )

    race_data = (
        stint_1_data
        + stint_2_data
        + stint_3_data
    )

    return total_time, race_data
