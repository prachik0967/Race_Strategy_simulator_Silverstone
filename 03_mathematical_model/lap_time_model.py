# Basic lap time mathematiacl model

def calculate_lap_time(
    base_lap_time,
    fuel_mass,
    fuel_time_penalty,
    tyre_pace_offset,
    tyre_age,
    linear_degradation,
    quadratic_degradation
):

# Calculate predicted lap time using the mathematical model

    fuel_penalty = (
        fuel_mass * fuel_time_penalty
    )

    tyre_penalty = (
        tyre_pace_offset
        + linear_degradation * tyre_age
        + quadratic_degradation * tyre_age**2
    )

    lap_time = (
        base_lap_time
        + fuel_penalty
        + tyre_penalty
    )

    return lap_time


# Example calculation

example_lap_time = calculate_lap_time(
    base_lap_time=88.0,
    fuel_mass=105.0,
    fuel_time_penalty=0.035,
    tyre_pace_offset=0.0,
    tyre_age=0,
    linear_degradation=0.025,
    quadratic_degradation=0.0015
)

print(
    f"Example predicted lap time: "
    f"{example_lap_time:.3f} seconds"
)

# Predicted lap time output: 91.675 seconds
