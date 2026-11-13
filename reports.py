from pathlib import Path
from results import get_position_text


def student_report(student):
    """Build a text report card for one student."""
    lines = [
        "=" * 55,
        "                 STUDENT REPORT CARD",
        "=" * 55,
        f"Student ID:       {student.student_id}",
        f"Full Name:        {student.full_name}",
        f"Class/Form:       {student.student_class}",
        f"Gender:           {student.gender}",
        f"Date of Birth:    {student.date_of_birth}",
        "-" * 55,
        "SUBJECT RESULTS",
        "-" * 55
    ]

    if student.scores:
        for subject, score in sorted(student.scores.items()):
            lines.append(f"{subject:<30} {score:>7.2f}")
    else:
        lines.append("No scores have been entered.")

    lines.extend([
        "-" * 55,
        f"Number of Subjects: {len(student.scores)}",
        f"Total Score:        {student.total_score():.2f}",
        f"Average Score:      {student.average_score():.2f}",
        f"Grade:              {student.grade() if student.scores else 'N/A'}",
        f"Result Entered:     {student.result_date or 'Not entered'}",
        "=" * 55
    ])
    return "\n".join(lines)


def class_report(students):
    """Build a summary of all students and their results."""
    lines = [
        "=" * 78,
        "                         CLASS RESULT SUMMARY",
        "=" * 78,
        f"{'ID':<12} {'NAME':<25} {'TOTAL':>9} {'AVERAGE':>10} {'GRADE':>8}",
        "-" * 78
    ]

    ranked = sorted(students, key=lambda item: item.average_score(), reverse=True)
    for student in ranked:
        grade = student.grade() if student.scores else "N/A"
        lines.append(
            f"{student.student_id:<12} {student.full_name[:24]:<25} "
            f"{student.total_score():>9.2f} {student.average_score():>10.2f} {grade:>8}"
        )

    averages = [student.average_score() for student in students if student.scores]
    if averages:
        lines.extend([
            "-" * 78,
            f"Students with results: {len(averages)}",
            f"Highest average:       {max(averages):.2f}",
            f"Lowest average:        {min(averages):.2f}",
            f"Class average:         {sum(averages) / len(averages):.2f}"
        ])
    else:
        lines.append("No student results are available yet.")

    lines.append("=" * 78)
    return "\n".join(lines)


def save_text_report(content, filename):
    """Save a report inside the project's reports folder."""
    report_folder = Path(__file__).parent / "reports"
    report_folder.mkdir(exist_ok=True)
    file_path = report_folder / filename

    with file_path.open("w", encoding="utf-8") as file:
        file.write(content)

    return file_path
