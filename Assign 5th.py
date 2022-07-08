print("shop")
quantity=int(input("price:")) #first of all we are going to add the price.bcz price ke bina aage ka step ni hoga
discount=quantity*10/100 # qus ma kidhu che ke aapde disc. b aapvanu che toh aenu calculation pn krvu padse
total=quantity-discount # hve disc. cut krya pchi su price malse aapda ne ae b lakhvi padse. 
if quantity>=1000: 
    print("you got 10% discount",total) #hve ahiya agar jo price 1000 thi vadhare hase toh 10% malse toh aenu total pan lakhvu padse ne ke finally aatli price thai gai.
else:
    print("no")

#toh aama khali quantity levani hti pchi aene discount aapvanu che bs biju kai j nathi aama
