race_laps = 52

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


def calculate_lap_time(
    lap,
    compound,
    tyre_age
):

    fuel_penalty = (
        calculate_fuel_mass(lap)* fuel_time_penalty
    )

    tyre_penalty = (
        calculate_tyre_penalty(
            compound,
            tyre_age
        )
    )

    return (
        base_lap_time+ fuel_penalty + tyre_penalty
    )



def test_fuel_never_negative():

    for lap in range(
        1,
        race_laps + 1
    ):

        assert calculate_fuel_mass(lap) >= 0

    print("PASS: Fuel mass never becomes negative")


def test_fuel_decreases():

    previous_fuel = calculate_fuel_mass(1)

    for lap in range(
        2,
        race_laps + 1
    ):

        current_fuel = calculate_fuel_mass(lap)

        assert current_fuel <= previous_fuel

        previous_fuel = current_fuel

    print("PASS: Fuel mass decreases through the race")


def test_tyre_degradation_increases():

    for compound in TYRES:

        previous_penalty = (
            calculate_tyre_penalty(
                compound,0
            )
        )

        for tyre_age in range(
            1,
            31
        ):

            current_penalty = (
                calculate_tyre_penalty(
                    compound,
                    tyre_age
                )
            )

            assert (
                current_penalty >= previous_penalty
            )

            previous_penalty = current_penalty

    print("PASS: Tyre penalty increases with tyre age")


def test_fresh_tyre_order():

    soft = calculate_tyre_penalty(
        "soft", 0
    )

    medium = calculate_tyre_penalty(
        "medium",0
    )

    hard = calculate_tyre_penalty(
        "hard",0
    )

    assert soft < medium < hard

    print(
        "PASS: Fresh tyre pace order is "
        "Soft > Medium > Hard"
    )


def test_fuel_effect():

    lap_1_time = calculate_lap_time(
        1,
        "soft",0
    )

    lap_40_time = calculate_lap_time(
        40,
        "soft", 0
    )

    assert lap_40_time < lap_1_time

    print(
        "PASS: Lower fuel load produces "
        "a faster lap with fresh tyres"
    )


# run the tests

print()
print("Model Validation")

test_fuel_never_negative()
test_fuel_decreases()
test_tyre_degradation_increases()
test_fresh_tyre_order()
test_fuel_effect()
