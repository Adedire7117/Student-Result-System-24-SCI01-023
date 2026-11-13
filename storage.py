import json
from pathlib import Path
from student import Student

DATA_FILE = Path(__file__).parent / "data" / "students.json"


def load_students():
    """Load saved students. Return an empty list if the file is missing."""
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)

    if not DATA_FILE.exists():
        DATA_FILE.write_text("[]", encoding="utf-8")
        return []

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            saved_data = json.load(file)

        return [Student.from_dictionary(item) for item in saved_data]

    except json.JSONDecodeError:
        print("Warning: students.json contains invalid JSON. Starting with no records.")
        return []
    except (KeyError, TypeError) as error:
        print("Warning: a student record could not be loaded:", error)
        return []


def save_students(students):
    """Save all Student objects to the JSON data file."""
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    saved_data = [student.to_dictionary() for student in students]

    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(saved_data, file, indent=4)

