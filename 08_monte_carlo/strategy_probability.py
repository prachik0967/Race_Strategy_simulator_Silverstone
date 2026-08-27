import random
import statistics


race_laps = 52

base_lap_time = 88.0

starting_fuel = 105.0
fuel_per_lap = 1.9
fuel_time_penalty = 0.035

pit_stop_loss = 19.9

driver_variability = 0.20


simulations = 10000


strategy_a_times = run_monte_carlo(
    "medium",
    "hard",
    20,
    simulations
)

strategy_b_times = run_monte_carlo(
    "soft",
    "hard",
    16,
    simulations
)

strategy_a_wins = 0
strategy_b_wins = 0

for time_a, time_b in zip(
    strategy_a_times,
    strategy_b_times
):

    if time_a < time_b:

        strategy_a_wins += 1

    elif time_b < time_a:

        strategy_b_wins += 1

  probability_a = (
    strategy_a_wins
    / simulations
)

probability_b = (
    strategy_b_wins
    / simulations
)

print()
print("strategy probability")

print()

print(
    f"Medium -> Hard win probability: "
    f"{probability_a:.1%}"
)

print(
    f"Soft -> Hard win probability: "
    f"{probability_b:.1%}"
)
