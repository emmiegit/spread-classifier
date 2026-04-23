def normalize_spread(stats):
    total = sum(stats)
    count = len(stats)
    return [(stat / total) * count for stat in stats]


IDEAL_SPREADS = [
    ("flat", [1, 1, 1, 1, 1, 1]),
    ("staircase", normalize_spread([10, 20, 30, 40, 50, 60])),
    ("reverse staircase", normalize_spread([60, 50, 40, 30, 20, 10])),
    # HP 50-80
    # ATK 200
    # DEF 50-80
    # SPA 0
    # SPD 50-80
    # SPE 90-110
    ("ideal atk", normalize_spread([80, 200, 80, 0, 80, 110])),
    ("ideal spa", normalize_spread([80, 0, 80, 200, 80, 110])),
]

# below 90 is "no speed"
# cheez is one defense state is below 50


def calculate_error(spread1, spread2):
    errors = [abs(stat1 - stat2) for stat1, stat2 in zip(spread1, spread2)]
    return sum(errors), errors


def calculate_fit(total_error, count):
    return (2 * count - total_error) / (2 * count)


def compare_spreads(spread):
    results = []
    for name, ideal_spread in IDEAL_SPREADS:
        total_error, error = calculate_error(spread, ideal_spread)
        fit = calculate_fit(spread, len(spread))
        results.push((name, total_error, error, fit))

    results.sort(key=lambda x: x[1])
    return results
