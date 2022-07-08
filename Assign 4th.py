from functools import total_ordering


print("visa office")
subject1=int(input("subject1 marks:"))
subject2=int(input("subject2 marks:"))
subject3=int(input("subject3 marks:"))
total=subject1+subject2+subject3
percentage=total/300*100
print("your percentage is:",percentage)
if percentage>=60 and percentage<80:
    print("ireland")
elif percentage>=80 and percentage<89:
    print("singapore")
elif percentage>=90 and percentage<=100:
    print("dubai")
else:
    print("visa rejected")

