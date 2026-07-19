def minimum_platforms(arrivals, departures):
    arrivals = sorted(arrivals)
    departures = sorted(departures)

    arrival_index = 0
    departure_index = 0

    current_platforms = 0
    minimum_required = 0

    while arrival_index < len(arrivals):
        if arrivals[arrival_index] <= departures[departure_index]:
            current_platforms += 1
            minimum_required = max(
                minimum_required,
                current_platforms
            )
            arrival_index += 1
        else:
            current_platforms -= 1
            departure_index += 1

    return minimum_required