def calculate_total(scores):
    """Return the sum of all subject scores."""
    return sum(scores.values())


def calculate_average(scores):
    """Return the average score, or zero if no scores exist."""
    if not scores:
        return 0
    return calculate_total(scores) / len(scores)


def assign_grade(average):
    """Assign a grade using the project's grading scale."""
    if average >= 70:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 50:
        return "C"
    elif average >= 45:
        return "D"
    else:
        return "F"


def get_position_text(position):
    """Return a readable position such as 1st, 2nd or 3rd."""
    if 10 <= position % 100 <= 20:
        ending = "th"
    else:
        ending = {1: "st", 2: "nd", 3: "rd"}.get(position % 10, "th")
    return str(position) + ending
