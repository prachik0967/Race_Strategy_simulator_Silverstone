#reference lap time before adding nay tyre or fuel penalties
base_lap_time = 88.0

starting_fuel = 105.0 #fuel at the start of the race (kg)
fuel_per_lap = 1.9 #assumed constant fuel consumption (kg/lap
fuel_time_penalty = 0.035 #additional lap time per kg of fuel (s/kg)


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
        # this condition ensures that there is never a negative mass
        # on lap one no laps have been committed so lap - 1 is used
    )


def calculate_lap_time(
    lap,
    compound,
    tyre_age
):

    fuel_mass = calculate_fuel_mass(lap)

    #convert the remaining fuel mass into a lap time penalty
    fuel_penalty = (
        fuel_mass * fuel_time_penalty
    )

    # Retrieve the right coefficients for the compound thst is going to be used
    tyre = TYRES[compound]

    
    # Combine the compound's initial pace deficit with the wear var
    # The squared term makes degradation accelerate as tyres age
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

    # Assume a fresh set of tyres at the beginning of every stint
    total_time = 0
    tyre_age = 0

    # Store individual lap results for later analysis or plotting
    lap_data = []

    # range excludes its upper bound, so +1 includes end_lap
    for lap in range(
        start_lap,
        end_lap + 1
    ):

        lap_time = calculate_lap_time(
            lap,
            compound,
            tyre_age
        )

        # Record the conditions used to calculate this lap
        lap_data.append({
            "lap": lap,
            "compound": compound,
            "tyre_age": tyre_age,
            "fuel_mass":
                calculate_fuel_mass(lap),
            "lap_time": lap_time
        })

        # Increase age AFTER calculating the lap
        total_time += lap_time
        tyre_age += 1
        # the first lap uses age 0, the second uses age 1, etc

    # Return both the overall result and the data for the lap completed
    return total_time, lap_data


# Example stint
# Simulate race laps 1–20 on a fresh set of medium tyres
# Unpack the two returned values into separate variables.

stint_time, stint_data = simulate_stint(
    1,
    20,
    "medium"
)

# An f-string inserts the result; :.3f displays three decimal places
print(
    f"20-lap Medium stint time: "
    f"{stint_time:.3f} seconds"
)
