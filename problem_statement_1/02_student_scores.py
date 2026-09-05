# pyrefly: ignore [missing-import]

import requests
# pyrefly: ignore [missing-import]
import matplotlib.pyplot as plt

API_URL = "https://jsonplaceholder.typicode.com/users"


def fetch_student_scores():
    response=requests.get(API_URL, timeout=10)


    if response.status_code!=200:
        print("Failed to fetch student data")
        return []



    data=response.json()
    students=[]


    for index, student in enumerate(data[:8]):
        name=student.get("name", f"Student{index+1}")

        score=60 + (index*5 %41)
        students.append({
            "name": name,
            "score": score
        })
    return students


def calculate_average(students):
    if not students:
        return 0

    total=sum(student['score'] for student in students)

    return total/len(students)



def display_chart(students, average_score):
    names=[student['name'] for student in students]
    score=[student['score'] for student in students]


    plt.figure(figsize=(10,6))

    plt.bar(names, score)


    plt.axhline(
        average_score, linestyle="--",
        label=f"Average: {average_score:.2f}"
    )
    plt.xlabel("Students")
    plt.ylabel("Test Score")
    plt.title("Student Test Scores")

    plt.xticks(rotation=30)

    plt.legend()
    plt.tight_layout()

    plt.savefig("student_scores.png")

    plt.show()




def main():
    students=fetch_student_scores()

    if not students:
        return


    average_score=calculate_average(students)

    print("Student Scores")
    for student in students:
        print(f"{student['name']}: {student['score']}")

    print(f"\nAverage Score: {average_score:.2f}")
    display_chart(students, average_score)

if __name__ == "__main__":
    main()

