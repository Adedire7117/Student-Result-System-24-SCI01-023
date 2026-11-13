from datetime import date


class Student:
    """Stores one student's personal details and subject scores."""

    def __init__(self, student_id, full_name, student_class, gender, date_of_birth,
                 scores=None, result_date=None):
        self.student_id = student_id
        self.full_name = full_name
        self.student_class = student_class
        self.gender = gender
        self.date_of_birth = date_of_birth
        self.scores = scores if scores is not None else {}
        self.result_date = result_date

    def add_or_update_score(self, subject, score):
        """Save a score and record the date it was entered."""
        self.scores[subject] = float(score)
        self.result_date = date.today().isoformat()

    def total_score(self):
        return sum(self.scores.values())

    def average_score(self):
        if len(self.scores) == 0:
            return 0
        return self.total_score() / len(self.scores)

    def grade(self):
        average = self.average_score()
        if average >= 70:
            return "A"
        elif average >= 60:
            return "B"
        elif average >= 50:
            return "C"
        elif average >= 45:
            return "D"
        return "F"

    def to_dictionary(self):
        """Convert the object into a dictionary so JSON can store it."""
        return {
            "student_id": self.student_id,
            "full_name": self.full_name,
            "student_class": self.student_class,
            "gender": self.gender,
            "date_of_birth": self.date_of_birth,
            "scores": self.scores,
            "result_date": self.result_date
        }

    @classmethod
    def from_dictionary(cls, details):
        """Create a Student object from a dictionary loaded from JSON."""
        return cls(
            details["student_id"],
            details["full_name"],
            details["student_class"],
            details["gender"],
            details["date_of_birth"],
            details.get("scores", {}),
            details.get("result_date")
        )
