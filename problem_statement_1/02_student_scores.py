from pathlib import Path

import requests
# pyrefly: ignore [missing-import]
import matplotlib.pyplot as plt


API_URL = "https://jsonplaceholder.typicode.com/users"

# Resolve output path relative to script location
BASE_DIR = Path(__file__).resolve().parent
OUTPUT_IMAGE = BASE_DIR / "student_scores.png"


def fetch_student_data():
    response = requests.get(API_URL, timeout=10)

    if response.status_code != 200:
        print("Failed to fetch student data from API")
        return []

    data = response.json()

    students = []

    for index, student in enumerate(data[:8]):
        name = student.get("name", f"Student {index + 1}")

        # Assumption:
        # The selected API provides user/student names but does not
        # provide test scores. Scores are assigned for demonstration.
        score = 60 + (index * 5)

        students.append({
            "name": name,
            "score": score
        })

    return students


def calculate_average(students):
    if not students:
        return 0

    total_score = sum(student["score"] for student in students)

    average = total_score / len(students)

    return average


def display_scores(students, average):
    print("\nStudent Test Scores:")
    print("-" * 40)

    for student in students:
        print(f"{student['name']}: {student['score']}")

    print("-" * 40)
    print(f"Average Score: {average:.2f}")


def create_chart(students, average):
    names = [student["name"] for student in students]
    scores = [student["score"] for student in students]

    plt.figure(figsize=(10, 6))

    plt.bar(names, scores)

    plt.axhline(
        average,
        linestyle="--",
        label=f"Average: {average:.2f}"
    )

    plt.title("Student Test Scores")
    plt.xlabel("Students")
    plt.ylabel("Score")

    plt.xticks(rotation=30, ha='right')

    plt.legend()
    plt.tight_layout()

    plt.savefig(OUTPUT_IMAGE)
    print(f"\nChart saved to: {OUTPUT_IMAGE}")

    # Only show interactively if a GUI backend is available
    try:
        if plt.get_backend().lower() != "agg":
            plt.show()
        else:
            plt.close()
    except Exception:
        plt.close()


def main():
    students = fetch_student_data()

    if not students:
        print("No student data fetched.")
        return

    average = calculate_average(students)

    display_scores(students, average)

    create_chart(students, average)


if __name__ == "__main__":
    main()
