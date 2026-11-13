# Student Result Management System

A beginner-friendly command-line Student Result Management System built with Python.

## Features

- Register students with ID, name, class/form, gender and date of birth.
- View, search, update and delete student records.
- Record scores for five subjects: English Language, Mathematics, Biology, Chemistry and Physics.
- Update an individual subject score.
- Calculate total, average and grade.
- Generate individual report cards.
- Display class results and class statistics.
- Sort students by average score or name.
- Save and load records using a JSON file.
- Save individual and class reports as text files.
- Record the date a student's result was entered.

## Requirements

- Python 3.9 or newer.
- No third-party Python packages are required.

## How to run

1. Extract the `student_result_system` folder.
2. Open the folder in Visual Studio Code.
3. Open the terminal in VS Code.
4. Run:

   ```bash
   python main.py
   ```

   On some Windows installations, use:

   ```bash
   py main.py
   ```

5. Choose an option from the menu.

## Grade scale

| Average | Grade |
|---|---|
| 70–100 | A |
| 60–69.99 | B |
| 50–59.99 | C |
| 45–49.99 | D |
| Below 45 | F |

## Project structure

```text
student_result_system/
├── main.py
├── student.py
├── results.py
├── storage.py
├── reports.py
├── README.md
├── data/
│   └── students.json
└── reports/
    └── (generated text reports appear here)
```

## Data storage

Student information is stored in `data/students.json`. The application loads the file when it starts and saves changes when records are added, updated, or deleted.

## Python concepts demonstrated

- Variables, strings, numbers and type conversion
- `if`, `elif`, `else`, `for` and `while`
- Lists and dictionaries
- Functions with parameters and return values
- Classes and objects
- Sorting with `sorted()`
- File handling with `open()`
- JSON data storage
- Exception handling with `try` and `except`
- Date handling with `datetime`
- Modules and imports

## Important note

This is an educational command-line project. It is designed for local practical demonstration and does not include user accounts, passwords or network access.
