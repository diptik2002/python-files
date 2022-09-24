
print(" SHAKE_MAKER ")
print("")
print("Welcome To SHAKE_MAKER")
print("Shakes :-\n Choco Shake     Price :- 150/-\n Kitkat Shake    Price :- 100/-\n Oreo Shake      Price:- 100/-")
print("Toppings :-\n Chocolates      Price :- 50/- \n Kitkat          Price :- 60/-\n Oreo            Price :- 80/-")
Shake=input("What you wanna drink today :-")
Toppings=input("If you wanna add some toppings :-")
print(" ")
shake1="Choco Shake"
shake2="Kitkat Shake"
shake3="Oreo Shake"
top1="Chocolates"
top2="Kitkat"
top3="Oreo"
#Shake price
Sprice1=150
Sprice2=100
Sprice3=100
#Toppings Price
top1price=50
top2price=60
top3price=80
#Cgst on Single Shakes
cgst1=Sprice1/100*5
cgst2=Sprice2/100*5
cgst3=Sprice3/100*5
#Sgst on Single Shakes
sgst1=Sprice1/100*5
sgst2=Sprice2/100*5
sgst3=Sprice3/100*5
#Total Taxes On Single Shake
Stax1=cgst1+sgst1
Stax2=cgst2+sgst2
Stax3=cgst3+sgst3
#Single Shake Final Price
Singlefinal1=Sprice1+Stax1
Singlefinal2=Sprice2+Stax2
Singlefinal3=Sprice3+Stax3
#Shake1 Combos
Combo1=Sprice1+top1price
Combo2=Sprice1+top2price
Combo3=Sprice1+top3price
#Shake2 Combos
Combo4=Sprice2+top1price
Combo5=Sprice2+top2price
Combo6=Sprice2+top3price
#Shake3 Combos
Combo7=Sprice3+top1price
Combo8=Sprice3+top2price
Combo9=Sprice3+top3price
#Cgst on Shakes Combo
ccgst1=Combo1/100*5
ccgst2=Combo2/100*5
ccgst3=Combo3/100*5
ccgst4=Combo4/100*5
ccgst5=Combo5/100*5
ccgst6=Combo6/100*5
ccgst7=Combo7/100*5
ccgst8=Combo8/100*5
ccgst9=Combo9/100*5
#Sgst on Shakes Combo
ssgst1=Combo1/100*5
ssgst2=Combo2/100*5
ssgst3=Combo3/100*5
ssgst4=Combo4/100*5
ssgst5=Combo5/100*5
ssgst6=Combo6/100*5
ssgst7=Combo7/100*5
ssgst8=Combo8/100*5
ssgst9=Combo9/100*5
#Total Taxes on Shakes Combo
Combotax1=ccgst1+ssgst1
Combotax2=ccgst2+ssgst2
Combotax3=ccgst3+ssgst3
Combotax4=ccgst4+ssgst4
Combotax5=ccgst5+ssgst5
Combotax6=ccgst6+ssgst6
Combotax7=ccgst7+ssgst7
Combotax8=ccgst8+ssgst8
Combotax9=ccgst9+ssgst9
#Combo Shakes Final Price
Combofinal1=Combo1+Combotax1
Combofinal2=Combo2+Combotax2
Combofinal3=Combo3+Combotax3
Combofinal4=Combo4+Combotax4
Combofinal5=Combo5+Combotax5
Combofinal6=Combo6+Combotax6
Combofinal7=Combo7+Combotax7
Combofinal8=Combo8+Combotax8
Combofinal9=Combo9+Combotax9
if Shake==shake1 and Toppings==top1:
    print("*************************************")
    print(" ")
    print("Your selected shake :-",shake1)
    print("Your selected toppings :-",top1)  
    print("cgst 5% :-",ccgst1)
    print("sgst 5% :-",ssgst1)
    print("Total tax :-",Combotax1)
    print("Total payable price :-",Combofinal1)
    print(" ")
    print("*************************************")
elif Shake==shake1 and Toppings==top2:
    print("*************************************")
    print(" ")
    print("Your selected shake :-",shake1)
    print("Your selected toppings :-",top2)  
    print("cgst 5% :-",ccgst2)
    print("sgst 5% :-",ssgst2)
    print("Total tax :-",Combotax2)
    print("Total payable price :-",Combofinal2)
    print(" ")
    print("*************************************")
elif Shake==shake1 and Toppings==top3:
    print("*************************************")
    print(" ")
    print("Your selected shake :-",shake1)
    print("Your selected toppings :-",top3)  
    print("cgst 5% :-",ccgst3)
    print("sgst 5% :-",ssgst3)
    print("Total tax :-",Combotax3)
    print("Total payable price :-",Combofinal3)
    print(" ")
    print("*************************************")
elif Shake==shake2 and Toppings==top1:
    print("*************************************")
    print(" ")
    print("Your selected shake :-",shake2)
    print("Your selected toppings :-",top1)  
    print("cgst 5% :-",ccgst4)
    print("sgst 5% :-",ssgst4)
    print("Total tax :-",Combotax4)
    print("Total payable price :-",Combofinal4)
    print(" ")
    print("*************************************")
elif Shake==shake2 and Toppings==top2:
    print("*************************************")
    print(" ")
    print("Your selected shake :-",shake2)
    print("Your selected toppings :-",top2)  
    print("cgst 5% :-",ccgst5)
    print("sgst 5% :-",ssgst5)
    print("Total tax :-",Combotax5)
    print("Total payable price :-",Combofinal5)
    print(" ")
    print("*************************************")
elif Shake==shake2 and Toppings==top3:
    print("*************************************")
    print(" ")
    print("Your selected shake :-",shake2)
    print("Your selected toppings :-",top3)  
    print("cgst 5% :-",ccgst6)
    print("sgst 5% :-",ssgst6)
    print("Total tax :-",Combotax6)
    print("Total payable price :-",Combofinal6)
    print(" ")
    print("*************************************")
elif Shake==shake3 and Toppings==top1:
    print("*************************************")
    print(" ")
    print("Your selected shake :-",shake3)
    print("Your selected toppings :-",top1)  
    print("cgst 5% :-",ccgst7)
    print("sgst 5% :-",ssgst7)
    print("Total tax :-",Combotax7)
    print("Total payable price :-",Combofinal7)
    print(" ")
    print("*************************************")
elif Shake==shake3 and Toppings==top2:
    print("*************************************")
    print(" ")
    print("Your selected shake :-",shake3)
    print("Your selected toppings :-",top2)  
    print("cgst 5% :-",ccgst8)
    print("sgst 5% :-",ssgst8)
    print("Total tax :-",Combotax8)
    print("Total payable price :-",Combofinal8)
    print(" ")
    print("*************************************")
elif Shake==shake3 and Toppings==top3:
    print("*************************************")
    print(" ")
    print("Your selected shake :-",shake3)
    print("Your selected toppings :-",top3)  
    print("cgst 5% :-",ccgst9)
    print("sgst 5% :-",ssgst9)
    print("Total tax :-",Combotax9)
    print("Total payable price :-",Combofinal9)
    print(" ")
    print("*************************************")
elif Shake==shake1:
    print("*************************************")
    print(" ")
    print("Your shake :-",shake1)
    print("cgst 5% :-",cgst1)
    print("sgst 5% :-",sgst1)
    print("Total tax :-",Stax1)
    print("Total payable amount :-",Singlefinal1)
    print(" ")
    print("*************************************")
elif Shake==shake2:
    print("*************************************")
    print(" ")
    print("Your shake :-",shake2)
    print("cgst 5% :-",cgst2)
    print("sgst 5% :-",sgst2)
    print("Total tax :-",Stax2)
    print("Total payable amount :-",Singlefinal2)
    print(" ")
    print("*************************************")
elif Shake==shake3:
    print("*************************************")
    print(" ")
    print("Your shake :-",shake3)
    print("cgst 5% :-",cgst3)
    print("sgst 5% :-",sgst3)
    print("Total tax :-",Stax3)
    print("Total payable amount :-",Singlefinal3)
    print("*************************************")
    print(" ")
else:
    print("Thank you for coming...!!!!!")
a=input()


    
    









