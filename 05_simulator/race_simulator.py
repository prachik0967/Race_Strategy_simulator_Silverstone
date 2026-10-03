#one-stop race simulator

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


def calculate_lap_time(lap,compound, tyre_age):

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


def simulate_stint( start_lap, end_lap,compound):

    total_time = 0
    tyre_age = 0 # Assume that each stint starts on a fresh set

    lap_data = []

    # range excludes its upper limit, so +1 includes end_lap
    for lap in range(start_lap, end_lap + 1 ):

        lap_time = calculate_lap_time(
            lap,
            compound,
            tyre_age
        )

        # Store one dictionary per lap for later inspection and plotting. This is all the datat from that one lap
        # the result of this is a list of dictionaries. one record per lap
        lap_data.append({
            "lap": lap,
            "compound": compound,
            "tyre_age": tyre_age,
            "fuel_mass":calculate_fuel_mass(lap),
            "lap_time": lap_time
            # these vars are created fresh each time
        })

        total_time += lap_time 
        # += is an augmented addition operator that adds a value to a variable and assign the result back to that same variable
        # The loop calculates each lap in turn
        
        tyre_age += 1 # Increase age after calculating the current lap
        # The order matters - I have to calculate and record the lap before increasing tyre age. The first lap therefore uses age 0, the second age 1

    # Return both the stint duration and its individual lap records
    return total_time, lap_data


def simulate_one_stop_strategy(first_compound,second_compound, pit_lap):

    # pit_lap belongs to the first stint: stop at the end of this lap
    stint_1_time, stint_1_data = (
        simulate_stint(
            1,
            pit_lap,
            first_compound
        )
    )

    # Start the next lap on fresh tyres - race lap numbering continues
    stint_2_time, stint_2_data = (
        simulate_stint(
            pit_lap + 1,
            race_laps,
            second_compound
        )
    )

    # Add the pit stop loss exactly once, outside the lap calculations - consider independant
    total_time = (
        stint_1_time
        + pit_stop_loss
        + stint_2_time
    )

    # Join the two lists in race order
    race_data = (
        stint_1_data
        + stint_2_data
    )

    return total_time, race_data

#IMPORTANT: the pit-stop loss appears in race_time, but isn’t included in any individual race_data lap time

# Separate total seconds into whole minutes and leftover seconds
def format_time(seconds):

    minutes = int(seconds // 60)

    remaining_seconds = (
        seconds % 60
    )

    # Display seconds with leading zeros and three decimal places
    return (
        f"{minutes}:"
        f"{remaining_seconds:06.3f}"
    )


# Example race strategy
# Evaluate one chosen strategy; this does not search for the fastest strategy

race_time, race_data = (
    simulate_one_stop_strategy(
        "medium",
        "hard",
        20
    )
)



print("Silverstone race simulator")

print()
print("Strategy:")
print("Medium -> Hard")
print("Pit at end of Lap 20")

print()
print(
    f"Total Race Time: "
    f"{format_time(race_time)}"
)
