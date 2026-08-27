import matplotlib.pyplot as plt


starting_fuel = 105.0
fuel_per_lap = 1.9
fuel_time_penalty = 0.035

base_lap_time = 88.0

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

# Plot 1: Fuel mass

laps = list(
    range(1, 53)
)

fuel_mass = [
    calculate_fuel_mass(lap)
    for lap in laps
]

plt.plot(
    laps,
    fuel_mass
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

plt.show()


# Plot 2: Tyre degradation


tyre_ages = list(
    range(0, 31)
)

for compound in TYRES:

    penalties = [

        calculate_tyre_penalty(
            compound,
            tyre_age
        )

        for tyre_age
        in tyre_ages
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

plt.show()

# Plot 3: Lap-time evolution


def calculate_lap_time(
    lap,
    compound,
    tyre_age
):

    fuel_penalty = (
        calculate_fuel_mass(lap) * fuel_time_penalty
    )

    tyre_penalty = (
        calculate_tyre_penalty(
            compound,
            tyre_age
        )
    )

    return (
        base_lap_time + fuel_penalty + tyre_penalty
    )


laps = list(
    range(1, 31)
)

for compound in TYRES:

    lap_times = []

    for lap in laps:

        tyre_age = lap - 1

        lap_time = (
            calculate_lap_time(
                lap,
                compound,
                tyre_age
            )
        )

        lap_times.append(
            lap_time
        )

    plt.plot(
        laps,
        lap_times,
        label=compound.capitalize()
    )

plt.xlabel(
    "Race Lap"
)

plt.ylabel(
    "Predicted Lap Time (s)"
)

plt.title(
    "Fuel Burn vs Tyre Degradation"
)

plt.legend()

plt.grid()

plt.show()
