# Basic lap time mathematical model
# Predict one lap's time from a reference time, fuel loads and tyre condition
# All time values and calculated penalites are in seconds

# def creates a reusable function
def calculate_lap_time(
    base_lap_time, # Reference lap time at zero modelled fuel penalty and zero tyre offset/degradation (s)
    fuel_mass, # Fuel carried on the lap (kg)
    fuel_time_penalty, # Extra lap time per kilogram of fuel (s/kg)
    tyre_pace_offset, # Fresh tyre pace difference from the reference (s)
    tyre_age, # Laps already completed on this set of tyres
    linear_degradation, # Linear tyre age coefficient (s/lap of tyre age)
    quadratic_degradation # Quadratic coefficient (s/lap of tyre age squared)
):

# Calculate predicted lap time using the mathematical model
# Assume each additional kilogram of fuel adds the same time penalty
    
    fuel_penalty = (
        fuel_mass * fuel_time_penalty
    )

# Combine the compound's initial pace with age related degradation
# **2 squares the tyre age, allowing degradation to accelerate with age (qaudratic term used)
    tyre_penalty = (
        tyre_pace_offset
        + linear_degradation * tyre_age
        + quadratic_degradation * tyre_age**2
    )
    
# Assume that the fuel and tyre effects can be added independently (no correaltion)
    lap_time = (
        base_lap_time
        + fuel_penalty
        + tyre_penalty
    )

# Send the calculated value back to the code/var that called the function
    return lap_time


# Example inputs to demonstrate the function
# Their validity needs to be justified separately using data

example_lap_time = calculate_lap_time(
    base_lap_time=88.0,
    fuel_mass=105.0,
    fuel_time_penalty=0.035,
    tyre_pace_offset=0.0,
    tyre_age=0,
    linear_degradation=0.025,
    quadratic_degradation=0.0015
)

# Display the result rounded to three decimal places
print(
    f"Example predicted lap time: "
    f"{example_lap_time:.3f} seconds"
)

# Predicted lap time output: 91.675 seconds
