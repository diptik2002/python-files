print("scholarship program")
print("")
subject1=int(input("marks1:"))
subject2=int(input("marks2:"))
subject3=int(input("marks3:"))
print("")
total=subject1+subject2+subject3
print("")
percentage=total/300*100
if percentage>=60 and percentage<70:
    print("5000 rs. scholarship")
elif percentage>=70 and percentage<80:
    print("10000rs. scholarship")
elif percentage>=80 and percentage<90:
    print("20000rs. scholarship")
elif percentage>=90 and percentage <=100:
    print("30000rs. scholarship")             
else:
    print("tata bye bye")
