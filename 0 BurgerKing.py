print("____________________________________________________________________")
print("Welcome to Burger King")
print(" ")
print("Please check out are menu")
print(" ")
print("Item Names:\nAloo tikki burger    Price: 30\nChicken burger       Price: 40\nDouble cheese burger Price: 60\nHamburger            Price: 90")
print(" ")
print("Drinks:\nPepsi                Price: 35\nCoca cola            Price: 35")
Choice1=input("What you want to eat today:")
Choice2=input("What you want to drink:")
print("*********************************")
item1="Aloo tikki burger"
item2="Chicken burger"
item3="Double cheese burger"
item4="Hamburger"
drink1="Pepsi"
drink2="Coca cola"
item1price=30
item2price=40
item3price=60
item4price=90
drink1price=35
drink2price=35
combo1=item1price+drink1price
combo2=item2price+drink1price
combo3=item3price+drink1price
combo4=item4price+drink1price
combo5=item1price+drink2price
combo6=item2price+drink2price
combo7=item3price+drink2price
combo8=item4price+drink2price
food1tax=item1price/100*15
food2tax=item2price/100*15
food3tax=item3price/100*15
food4tax=item4price/100*15
drink1tax=drink1price/100*15
drink2tax=drink2price/100*15
finalprice1=item1price+food1tax
finalprice2=item2price+food2tax
finalprice3=item3price+food3tax
finalprice4=item4price+food4tax
finalprice5=drink1price+drink1tax
finalprice6=drink2price+drink2tax
combo1tax=combo1/100*15
combo2tax=combo2/100*15
combo3tax=combo3/100*15
combo4tax=combo4/100*15
combo5tax=combo5/100*15
combo6tax=combo6/100*15
combo7tax=combo7/100*15
combo8tax=combo8/100*15
final1=combo1+combo1tax
final2=combo2+combo2tax
final3=combo3+combo3tax
final4=combo4+combo4tax
final5=combo5+combo5tax
final6=combo6+combo6tax
final7=combo7+combo7tax
final8=combo8+combo8tax
if Choice1==item1 and Choice2==drink1:
    print("Your total bill after applying 15% GST:",final1)
elif Choice1==item2 and Choice2==drink1:
    print("Your total bill after applying 15% GST:",final2)
elif Choice1==item3 and Choice2==drink1:
    print("Your total bill after applying 15% GST:",final2)
elif Choice1==item4 and Choice2==drink1:
    print("Your total bill after applying 15% GST:",final4)
elif Choice1==item1 and Choice2==drink2:
    print("Your total bill after applying 15% GST:",final5)
elif Choice1==item2 and Choice2==drink2:
    print("Your total bill after applying 15% GST:",final6)
elif Choice1==item3 and Choice2==drink2:
    print("Your total bill after applying 15% GST:",final7)
elif Choice1==item4 and Choice2==drink2:
    print("Your total bill after applying 15% GST:",final8)
elif Choice1==item1:
    print("Your total bill after applying 15% GST:",finalprice1)
elif Choice1==item2:
    print("Your total bill after applying 15% GST:",finalprice2)
elif Choice1==item3:
    print("Your total bill after applying 15% GST:",finalprice3)
elif Choice1==item4:
    print("Your total bill after applying 15% GST:",finalprice4)
elif Choice2==drink1:
    print("Your total bill after applying 15% GST:",finalprice5)
elif Choice2==drink2:
    print("Your total bill after applying 15% GST:",finalprice6)
print("*********************************")
print("HAPPY EATING!")
print("____________________________________________________________________")


