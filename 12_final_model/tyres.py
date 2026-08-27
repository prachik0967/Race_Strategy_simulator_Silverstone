from config import TYRES


def calculate_tyre_penalty(
    compound,
    tyre_age
):
    # Calculate tyre compound and degradation lap-time penalty

    if compound not in TYRES:
        raise ValueError(
            f"Unknown tyre compound: {compound}"
        )

    if tyre_age < 0:
        raise ValueError(
            "Tyre age cannot be negative."
        )

    tyre = TYRES[compound]

    degradation = (
        tyre["linear_deg"] * tyre_age
        + tyre["quadratic_deg"] * tyre_age**2
    )

    return (
        tyre["pace_offset"]
        + degradation
    )
