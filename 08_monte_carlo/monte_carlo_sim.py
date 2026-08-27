import random
import statistics
import matplotlib.pyplot as plt

race_laps = 52

base_lap_time = 88.0

starting_fuel = 105.0
fuel_per_lap = 1.9
fuel_time_penalty = 0.035

pit_stop_loss = 19.9

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

    return (
        deterministic_time
        + random_variation
    )

def simulate_stochastic_one_stop(
    first_compound,
    second_compound,
    pit_lap
):

    total_time = 0

    tyre_age = 0

    for lap in range(
        1,
        pit_lap + 1
    ):

        total_time += (
            calculate_stochastic_lap_time(
                lap,
                first_compound,
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
                second_compound,
                tyre_age
            )
        )

        tyre_age += 1

    return total_time

def run_monte_carlo(
    first_compound,
    second_compound,
    pit_lap,
    simulations=10000
):

    race_times = []

    for _ in range(simulations):

        race_time = (
            simulate_stochastic_one_stop(
                first_compound,
                second_compound,
                pit_lap
            )
        )

        race_times.append(
            race_time
        )

    return race_times

race_times = run_monte_carlo(
    "medium",
    "hard",
    20,
    simulations=10000
)

mean_time = statistics.mean(
    race_times
)

standard_deviation = (
    statistics.stdev(
        race_times
    )
)

minimum_time = min(
    race_times
)

maximum_time = max(
    race_times
)

print()
print("Monte carlo results")


print(
    "Strategy: Medium -> Hard"
)

print(
    "Pit Lap: 20"
)

print(
    f"Simulations: "
    f"{len(race_times)}"
)

print()

print(
    f"Mean Race Time: "
    f"{mean_time:.3f} s"
)

print(
    f"Standard Deviation: "
    f"{standard_deviation:.3f} s"
)

print(
    f"Fastest Simulation: "
    f"{minimum_time:.3f} s"
)

print(
    f"Slowest Simulation: "
    f"{maximum_time:.3f} s"
)

plt.hist(
    race_times,
    bins=40
)

plt.xlabel(
    "Total Race Time (s)"
)

plt.ylabel(
    "Frequency"
)

plt.title(
    "Monte Carlo Race-Time Distribution"
)

plt.grid()

plt.show()
