import random
import statistics

from config import (
    race_laps,
    pit_stop_loss,
    driver_variability
)

from race import calculate_lap_time


# stochastic lap time

def calculate_stochastic_lap_time(
    lap,
    compound,
    tyre_age
):

  # Add random lap-time variation to the deterministic lap-time prediction.

    deterministic_time = (
        calculate_lap_time(
            lap,
            compound,
            tyre_age
        )
    )

    random_variation = random.gauss(
        0,
        driver_variability
    )

    return (
        deterministic_time
        + random_variation
    )


# stochastic one stop race

def simulate_stochastic_one_stop(
    compound_1,
    compound_2,
    pit_lap
):
  
  
  # Simulate one complete one-stop race with random lap-time variation.

    total_time = 0

    tyre_age = 0

    for lap in range(
        1,
        pit_lap + 1
    ):

        total_time += (
            calculate_stochastic_lap_time(
                lap,
                compound_1,
                tyre_age
            )
        )

        tyre_age += 1

    total_time += pit_stop_loss

    tyre_age = 0

    for lap in range(
        pit_lap + 1,
        race_laps + 1
    ):

        total_time += (
            calculate_stochastic_lap_time(
                lap,
                compound_2,
                tyre_age
            )
        )

        tyre_age += 1

    return total_time


# monte carlo runner

def run_monte_carlo_one_stop(
    compound_1,
    compound_2,
    pit_lap,
    simulations=10000
):
  
  
  # Repeat a one-stop strategy many times and return the simulated race times.

    race_times = []

    for _ in range(
        simulations
    ):

        race_time = (
            simulate_stochastic_one_stop(
                compound_1,
                compound_2,
                pit_lap
            )
        )

        race_times.append(
            race_time
        )

    return race_times


# summary stats

def calculate_statistics(
    race_times
):
   
  
  # Calculate summary stats for a set of Monte Carlo race times
    return {
        "mean":
            statistics.mean(
                race_times
            ),

        "standard_deviation":
            statistics.stdev(
                race_times
            ),

        "minimum":
            min(
                race_times
            ),

        "maximum":
            max(
                race_times
            )
    }


# Strategy comparison

def compare_strategies(
    strategy_a,
    strategy_b,
    simulations=10000
):
   
  
  # Compare two one-stop strategies using Monte Carlo simulation.

    strategy_a_times = (
        run_monte_carlo_one_stop(
            strategy_a["compound_1"],
            strategy_a["compound_2"],
            strategy_a["pit_lap"],
            simulations
        )
    )

    strategy_b_times = (
        run_monte_carlo_one_stop(
            strategy_b["compound_1"],
            strategy_b["compound_2"],
            strategy_b["pit_lap"],
            simulations
        )
    )

    strategy_a_wins = 0
    strategy_b_wins = 0
    ties = 0

    for time_a, time_b in zip(
        strategy_a_times,
        strategy_b_times
    ):

        if time_a < time_b:
            strategy_a_wins += 1

        elif time_b < time_a:
            strategy_b_wins += 1

        else:
            ties += 1

    return {
        "strategy_a_probability":
            strategy_a_wins
            / simulations,

        "strategy_b_probability":
            strategy_b_wins
            / simulations,

        "tie_probability":
            ties
            / simulations,

        "strategy_a_times":
            strategy_a_times,

        "strategy_b_times":
            strategy_b_times
    }
