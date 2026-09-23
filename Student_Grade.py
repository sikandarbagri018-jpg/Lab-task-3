#Question no 1

subjects = 5
marks = []

# Loop to enter marks for 5 subjects
for i in range(subjects):
    m = float(input(f"Enter marks for subject {i+1} (out of 100): "))
    marks.append(m)

total = sum(marks)
percentage = (total / (subjects * 100)) * 100

# Grade logic
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

result = "Pass" if percentage >= 50 else "Fail"

print("\n--- Result ---")
print("Total Marks:", total)
print("Percentage: {:.2f}%".format(percentage))
print("Grade:", grade)
print("Result:", result)