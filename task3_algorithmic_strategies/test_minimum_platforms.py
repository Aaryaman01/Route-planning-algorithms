from task3_algorithmic_strategies.minimum_platforms import (
    minimum_platforms
)


arrivals = [900, 940, 950, 1100, 1500, 1800]
departures = [910, 1200, 1120, 1130, 1900, 2000]

result = minimum_platforms(
    arrivals,
    departures
)

print("Minimum platforms:", result)