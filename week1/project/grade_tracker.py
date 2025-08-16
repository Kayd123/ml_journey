import pandas as pd
df = pd.read_csv("data/data.csv")
print(f"Rows: {df.shape[0]}, Columns:{df.shape[1]}")
print (df.head())
student_avg = df.groupby("Name")["Marks"].mean()
print(student_avg)
def get_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"
for student, avg in student_avg.items():
    grade = get_grade(avg)
    print(f"Student: {student} — Average: {avg:.0f}% — Grade: {grade}")
