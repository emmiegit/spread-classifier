def normalize_spread(stats):
    total = sum(stats)
    count = len(stats)
    return [(stat / total) * count for stat in stats]

IDEAL_SPREADS = [
    ("flat", )
]


def calculate_error(spread1, spread2):
    errors = [abs(stat1 - stat2) for stat1, stat2 in zip(spread1, spread2)]
    return sum(errors), errors


def calculate_confidence(total_error, count):
    return (2 * count - total_error) / (2 * count)

def compare_spreads(spread):
    results = []
    for name, ideal_spread in IDEAL_SPREADS:
        total_error, error = calculate_error(spread, ideal_spread)
        confidence = calculate_confidence(spread, len(spread))
        results.push((name, total_error, error, confidence))

    results.sort(key=lambda x: x[1])
    for name, total_error, error, confidence in results:
        print(f"{name} {total_error:.2f} {confidence:.2f}")
    print(f"Best match: {name} {confidence * 100:.1f}")
