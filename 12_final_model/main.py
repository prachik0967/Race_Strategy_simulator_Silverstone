# silverstone race sim main program

from config import (
    circuit_name,
    circuit_length,
    race_laps,
    race_distance
)

from optimiser import (
    optimise_one_stop,
    optimise_two_stop,
    compare_stop_strategies
)

from monte_carlo import (
    run_monte_carlo_one_stop,
    calculate_statistics
)


# helper function
# Convert seconds into minutes:seconds

def format_time(seconds):
    
    minutes = int(
        seconds // 60
    )

    remaining_seconds = (
        seconds % 60
    )

    return (
        f"{minutes}:"
        f"{remaining_seconds:06.3f}"
    )


# circuit information

print()
print(" Silverstone race strategy simulator")
print("==========================================")
print()
print(
    f"Circuit: {circuit_name}"
)

print(
    f"Circuit Length: "
    f"{circuit_length} km"
)

print(
    f"Race Laps: "
    f"{race_laps}"
)

print(
    f"Race Distance: "
    f"{race_distance} km"
)


# one stop optimisation

best_one_stop, one_stop_results = (
    optimise_one_stop()
)

print()
print(" Best one stop strategy")
print("------------------------------------------")

print(
    f"Strategy: "
    f"{best_one_stop['compound_1'].capitalize()}"
    f" -> "
    f"{best_one_stop['compound_2'].capitalize()}"
)

print(
    f"Pit Lap: "
    f"{best_one_stop['pit_lap']}"
)

print(
    f"Race Time: "
    f"{format_time(best_one_stop['race_time'])}"
)


# two stop optimisation

best_two_stop, two_stop_results = (
    optimise_two_stop()
)

print()
print("Best two-stop strategy")
print("------------------------------------------")

print(
    f"Strategy: "
    f"{best_two_stop['compound_1'].capitalize()}"
    f" -> "
    f"{best_two_stop['compound_2'].capitalize()}"
    f" -> "
    f"{best_two_stop['compound_3'].capitalize()}"
)

print(
    f"Pit Laps: "
    f"{best_two_stop['pit_1']} and "
    f"{best_two_stop['pit_2']}"
)

print(
    f"Race Time: "
    f"{format_time(best_two_stop['race_time'])}"
)


# overall comparisono

comparison = (
    compare_stop_strategies()
)

overall_best = (
    comparison["overall_best"]
)

print()
print(" overall deterministic result")
print("------------------------------------------")

print(
    f"Fastest Strategy Type: "
    f"{overall_best['strategy_type'].capitalize()}"
)

print(
    f"Advantage: "
    f"{overall_best['advantage']:.3f} seconds"
)


# monte carlo analysis
# For now, Monte Carlo analysis is performed on the optimal one-stop strategy.

print()
print("Monte carlo analysis")
print("------------------------------------------")

print(
    "Running 10,000 simulations."
)


race_times = (
    run_monte_carlo_one_stop(
        best_one_stop["compound_1"],
        best_one_stop["compound_2"],
        best_one_stop["pit_lap"],
        simulations=10000
    )
)


statistics = (
    calculate_statistics(
        race_times
    )
)


print()

print(
    f"Strategy: "
    f"{best_one_stop['compound_1'].capitalize()}"
    f" -> "
    f"{best_one_stop['compound_2'].capitalize()}"
)

print(
    f"Pit Lap: "
    f"{best_one_stop['pit_lap']}"
)

print(
    f"Mean Race Time: "
    f"{format_time(statistics['mean'])}"
)

print(
    f"Standard Deviation: "
    f"{statistics['standard_deviation']:.3f} s"
)

print(
    f"Fastest Simulation: "
    f"{format_time(statistics['minimum'])}"
)

print(
    f"Slowest Simulation: "
    f"{format_time(statistics['maximum'])}"
)


# end

print()
print(" SIMULATION COMPLETED!!")
print()
