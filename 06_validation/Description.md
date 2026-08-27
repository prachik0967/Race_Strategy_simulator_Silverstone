# Overview

Before I start optimising race strategy, the model I created must be checked to ensure that it behaves logically and in the way I intended.
Therefore, the purpose of this section is to verify that the model produces physically sensible trends and does not generate invalid outputs.

The validation checks include:

- Fuel mass decreases through the race.
- Fuel mass never becomes negative.
- Tyre degradation increases with tyre age.
- Soft tyres begin to degrade faster than Medium and Hard tyres.
- Hard tyres degrade more slowly than Soft tyres.
- Fresh tyres reset to age zero after a pit stop.
- Lap time responds correctly to changes in fuel load and tyre condition.
- Total race time is equal to the sum of lap times and pit-stop losses.

# Validation Approach

The model will be checked using:

1. Numerical tests
2. Automated assertions
3. Visual plots
4. Comparison of expected model behaviour

The aim is not to prove that this simplified model perfectly reproduces a real Formula 1 car.
The aim is to confirm that the model is internally consistent and behaves in a way that is suitable so strategy optimisation can be conducted.
