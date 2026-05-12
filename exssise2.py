# ===== EXAM RESULT (WITH STUDENT NAME) =====

print("    EXAM RESULT \n")

# Student Name
name = input("enter your Name: ")

# Subject 1
subject1 = input("Enter the Name of subject One : ")
marks1 = float(input("Enter The Subject markis: "))

# Subject 2
subject2 = input("Enter the Name of subject Two: ")
marks2 = float(input("Enter The Subject markis: "))

# Subject 3
subject3 = input("Enter the Name of subject Three: ")
marks3 = float(input("Enter The Subject markis: "))

# Subject 4
subject4 = input("Enter the Name of subject Four: ")
marks4 = float(input("Enter The Subject markis: "))

# Total & Percentage
total = marks1 + marks2 + marks3 + marks4
percentage = total / 4

# GPA
if percentage >= 90:
    gpa = 4.0
elif percentage >= 80:
    gpa = 3.0
elif percentage >= 70:
    gpa = 2.0
elif percentage >= 60:
    gpa = 1.0
else:
    gpa = 0.0

# Output
print("\n RESULT ")
print(f"Magaca Ardayga: {name}\n")

print(f"{subject1}: {marks1}")
print(f"{subject2}: {marks2}")
print(f"{subject3}: {marks3}")
print(f"{subject4}: {marks4}")

print(f"\nTotal: {total}")
print(f"Percentage: {percentage}%")
print(f"GPA: {gpa}")
print("\n wellcome,", name)
print("natiijo wacan mahadsanid!")