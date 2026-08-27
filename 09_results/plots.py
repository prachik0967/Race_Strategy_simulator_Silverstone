import matplotlib.pyplot as plt
import random

race_laps = 52

starting_fuel = 105.0
fuel_per_lap = 1.9

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

# plot 1 - fuel mass through the race

def calculate_fuel_mass(lap):

    return max(
        starting_fuel
        - (lap - 1) * fuel_per_lap,
        0
    )


laps = list(
    range(1, race_laps + 1)
)

fuel_values = [
    calculate_fuel_mass(lap)
    for lap in laps
]


plt.figure()

plt.plot(
    laps,
    fuel_values
)

plt.xlabel(
    "Race Lap"
)

plt.ylabel(
    "Fuel Mass (kg)"
)

plt.title(
    "Fuel Mass Throughout the Silverstone Race"
)

plt.grid()

plt.tight_layout()

plt.savefig(
    "fuel_mass.png"
)

plt.show()

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

tyre_ages = list(
    range(0, 31)
)


plt.figure()


for compound in TYRES:

    penalties = [

        calculate_tyre_penalty(
            compound,
            age
        )

        for age in tyre_ages
    ]

    plt.plot(
        tyre_ages,
        penalties,
        label=compound.capitalize()
    )


plt.xlabel(
    "Tyre Age (laps)"
)

plt.ylabel(
    "Lap-Time Penalty (s)"
)

plt.title(
    "Modelled Tyre Degradation"
)

plt.legend()

plt.grid()

plt.tight_layout()

plt.savefig(
    "tyre_degradation.png"
)

plt.show()

base_lap_time = 88.0

fuel_time_penalty = 0.035

pit_stop_loss = 19.9

def calculate_lap_time(
    lap,
    compound,
    tyre_age
):

    fuel_penalty = (
        calculate_fuel_mass(lap)
        * fuel_time_penalty
    )

    tyre_penalty = (
        calculate_tyre_penalty(
            compound,
            tyre_age
        )
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

def simulate_one_stop(
    compound_1,
    compound_2,
    pit_lap
):

    return (
        simulate_stint(
            1,
            pit_lap,
            compound_1
        )
        +
        pit_stop_loss
        +
        simulate_stint(
            pit_lap + 1,
            race_laps,
            compound_2
        )
    )

pit_laps = list(
    range(5, race_laps - 4)
)

race_times = []


for pit_lap in pit_laps:

    race_time = simulate_one_stop(
        "medium",
        "hard",
        pit_lap
    )

    race_times.append(
        race_time
    )

minimum_time = min(
    race_times
)

minimum_index = race_times.index(
    minimum_time
)

optimal_pit_lap = (
    pit_laps[minimum_index]
)

plt.figure()

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
    "Medium to Hard Pit-Window Optimisation"
)

plt.grid()

plt.tight_layout()

plt.savefig(
    "pit_window.png"
)

plt.show()

driver_variabilty = 0.20

def calculate_stochastic_lap_time(
    lap,
    compound,
    tyre_age
):

    deterministic_time = (
        calculate_lap_time(
            lap,
            compound,
            tyre_age
        )
    )

    random_variation = (
        random.gauss(
            0,
            driver_variability
        )
    )

    return (
        deterministic_time
        + random_variation
    )

def simulate_stochastic_race(
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

simulations = 10000

monte_carlo_times = []


for _ in range(
    simulations
):

    race_time = (
        simulate_stochastic_race(
            "medium",
            "hard",
            optimal_pit_lap
        )
    )

    monte_carlo_times.append(
        race_time
    )

plt.figure()

plt.hist(
    monte_carlo_times,
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

plt.tight_layout()

plt.savefig(
    "monte_carlo_distribution.png"
)

plt.show()
