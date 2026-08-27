# Overview

This simulator can calculate the total race time for a manually selected strategy.
In this next stage I want the simulator to be able to automate the search for the fastest strategy.
The optimisation process will evaluate different:

- Starting tyre compounds
- Second tyre compounds
- Pit-stop laps

For each valid strategy, the simulator calculates total race time.
The strategy with the lowest total race time is selected as the optimum.

# One-Stop Strategy Search Space

A one-stop strategy is defined by:

- First tyre compound
- Second tyre compound
- Pit-stop lap

Strategies using the same compound before and after the pit stop are excluded.
Pit stops are restricted to sensible race laps rather than allowing a stop immediately after the start or at the end of the race.

# Optimisation Method

- I used a brute-force search.
- Every valid combination of tyre compounds and pit-stop lap is simulated.
- The total race time for each strategy is stored.
- The strategy with the lowest simulated race time is then identified.

Brute-force optimisation is suitable because the strategies available is relatively small.

# Output

The optimiser will report:

- Fastest strategy
- Starting compound
- Second compound
- Optimal pit lap
- Minimum simulated race time
- Ranked alternative strategies

The stored optimisation data will later be used for visualisation and strategy comparison.
