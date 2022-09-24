print( "              DMart")
print("----------------------------------------")
print("      AVENUE SUPERRMARTS LTD")
print("----------------------------------------")
print("   CIN :- L61900MH2000PLC126473")
print("     GSTIN :- 24AACCA8432H1ZW ")
print("     FSSAI NO :-10715026000439 ")
print("----------------------------------------")
print("            DMART MOTERA ")
print("    City Gold Multiplex Compund ")
print(" Motera Stadium Road ,Sabarmati1, Motera ")
print("          Ahmedabad - 380005")
print("__________Phone : 078-30938500__________")
print("")
sum = 0
while (True):
	userInput = input("Enter the price of item or press q to quit :")
	if (userInput!='q'):
		sum = sum + int(userInput)
		print(f"Order total so far: {sum}")
	else:
		print(f"Your Bill total is {sum}.\nThanks for shopping with us")
		break

