print("car showroom")
car_name=input("enter your car name:")
car1="duster"
car2="city"
car3="bmw"
price1=500000
price2=540000
price3=900000
tax1=price1*10/100
tax2=price2*8/100
tax3=price3*15/100
finalprice1=price1+tax1
finalprice2=price2+tax2
finalprice3=price3+tax3
if car_name==car1:
    print("10% road tax:",finalprice1)
elif car_name==car2:
    print("8% road tax:",finalprice2)
elif car_name==car3:
    print("15% road tax:",finalprice3)
else:
    print("Thank You")
            

