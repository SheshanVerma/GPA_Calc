# Python Program to calculate the avergae of the total exams and credits

# Enter number of exam student write
number_of_exams = int(input("How many exam you had? :"))

# Enter total number of credit each exam acquire
total_credit = int(input("What is your total number of credit score? :"))

# lets the average be 0
average = 0
for exam in range(number_of_exams):
    score = int(input("Enter Exams scores :"))
    exam_credits = int(input("Enter each exams credits :"))
    average += score * exam_credits / total_credit
print("Therefore your average is :", average)

if average >= 90:
    print("Congratulations your grade is A+ which is Excellent")
elif 90 > average >= 80:
    print("Congratulations your grade is A which is amazing")
elif 80 > average >= 70:
    print("Congratulations your grade is B which is good")
elif 70 > average >= 60:
    print("Congratulations your grade is C you can do better")
elif 60 > average >= 50:
    print("Congratulations your grade is D and you need to work hard")
else:
    print("Sorry you failed!")







