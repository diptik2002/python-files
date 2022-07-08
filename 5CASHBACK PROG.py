print(" ************************ ")
print(" MOON LIGHT STORE ")
product1=float(input("Enter your product1 price:"))
product2=float(input("Enter your product2 price:"))
product3=float(input("Enter your product3 price:"))
print(" Your product1 price is: ",product1)
print(" Your product2 price is: ",product2)
print(" Your product3 price is: ",product3)
total=product1+product2+product3
print("TOTAL PAYABLE PRICE:",total)
if total>=500:
    print(" You got 100RS. cashback ")
elif total==300:
    print(" You got 50RS. cashback ")
else:
    print(" No cashback ")
print(" *** THANK YOU *** ")


