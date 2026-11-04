"""Calculate a letter grade from equally weighted whole-number scores."""


def letter_grade(average):
    for minimum, grade in [(90, "A"), (80, "B"), (70, "C"), (60, "D")]:
        if average >= minimum:
            return grade
    return "F"


def main():
    print("Student Grade Calculator")
    print("Enter one whole-number score (0–100) at a time. Press Enter to finish.")
    scores = []
    while True:
        entry = input("Score: ").strip()
        if not entry:
            break
        try:
            score = int(entry)
        except ValueError:
            print("Please enter a whole number.")
            continue
        if 0 <= score <= 100:
            scores.append(score)
        else:
            print("Scores must be between 0 and 100.")

    if scores:
        average = sum(scores) / len(scores)
        print(f"Average: {average:.2f}/100")
        print(f"Letter grade: {letter_grade(average)}")
    else:
        print("No scores entered.")


if __name__ == "__main__":
    main()
