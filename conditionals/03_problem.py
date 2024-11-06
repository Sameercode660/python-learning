# 3. Grade calculator: Assign a letter grade based on student's score: A(90-100), B(80-89), C(70-79), D(60-69), F(below 60)

score = 101

if score >= 90 and score <= 100:
    print("Grade: A")

elif score < 90 and score >= 80:
    print("Grade: B")

elif score < 80 and score >= 70:
    print("Grade: C")

elif score < 70 and score >= 60:
    print("Grade: D")

elif score < 60:
    print("Grade: F")

else:
    print("Invalid Grade")
