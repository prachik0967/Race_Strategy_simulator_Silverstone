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

# Calculate the lap-time penalty caused by tyre compound and tyre degradation
def calculate_tyre_penalty(
    compound,
    tyre_age
):
    tyre = TYRES[compound]

    # Calculate the time lost through wear.
    # The linear term grows steadily
    # The squared term makes the penalty grow increasingly quickly as the tyres get older
    degradation = (
        tyre["linear_deg"] * tyre_age
        + tyre["quadratic_deg"] * tyre_age**2
    )

    # Add the compound's fresh tyre pace deficit to the wear penalty
    tyre_penalty = (
        tyre["pace_offset"]
        + degradation
    )

    # Return only the tyre contribution, not the complete lap time
    return tyre_penalty


# Example checks

print("Tyre model checks")

print(
    "Fresh Soft:",
    calculate_tyre_penalty("soft", 0)
)

print(
    "15-lap-old Soft:",
    calculate_tyre_penalty("soft", 15)
)

print(
    "Fresh Medium:",
    calculate_tyre_penalty("medium", 0)
)

print(
    "Fresh Hard:",
    calculate_tyre_penalty("hard", 0)
)
