#Creating a Grade classifyer
# input
name = input("Enter Learner Name: ")
mathematics = float(input("Please Enter Mathematics marks: "))
english = float(input("Please Enter English Marks: "))
sciences = float(input("Please Enter Scieneces Marks: "))

#Prcessing calculations
marks_sum = (mathematics + english + sciences)/3
print("\n===============================================Report card================================================")
# output of Marks_sum


# Grades and Descion making
if marks_sum >= 80:
    grade = ("A")
elif marks_sum >= 70:
    grade = ("B")
elif marks_sum >= 60:
    grade = ("C")
elif marks_sum >= 50:
    grade = ("D")
elif marks_sum >= 40:
    grade = ("E")
else:
    grade = ("D")

# Lowest threshhold that needs attentions
if marks_sum >= 50:
    status = ("Passed")
elif marks_sum >= 40: 
    status = ("need to intervine")
else:
    status = ("fail")

#output
print("Learner Name: ", name)
print("The Mark for Mathematics: ", mathematics)
print("The Mark for English: ", english)
print("The mark for sciences: ", sciences)
print("Average: ", marks_sum)
print("Average rounded: ", round(marks_sum, 2))
print("Grade: ", grade)
print("Status:", status)

# Check intervention
print("\n interverntion Report:")
if mathematics < 40:
    print("mathatics needs intervention")
if english < 40:
    print("english needs intervention")
if sciences < 40:
    print("sciences needs intervention")

if mathematics >= 40 and english >= 40 and sciences >= 40:
    print("no intervention needed")
print("========================================================================================================")

