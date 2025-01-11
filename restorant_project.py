# Ne fillim te kodit deklarojme variablat e nevojshme me type-t perkatese dhe me vlerat ne varesi te biznesit qe behet fjale
#Te dhenat e Biznesit
restaurant_name : str = "Il gusto italiano"
type_bussines : str = "Restaurant"
product_price: float = 4.6
staff_number : int = 12
table_number : int = 30
has_card_payment : bool = True
has_shisha_included : bool = False
products_list: list[str] = ["Pizza", "Spagetti", "Rizotto"]
# products_prices: list[float] = [5.6, 8.9, 5.4]
restaurant_balance: float = 800
has_beers: bool = True
has_energy_drinks: bool = False

# Te dhenat e klientit
client_cash_balance: float = 10.2
client_card_balance: float = 5
client_bag: list [str] = [] #per momentin do jete bosh, dhe do mbushet kur klienti te porosise produkte

# afishojme te dhenat e variablave, per te pare nese i kane marre vlerat sic duhet.
print(f"emri i restorantit:  {restaurant_name}")
print("tipi i biznesit: " + type_bussines)
print(f"restoranti ka {staff_number} punonjes")
print(f"restoranti ka {table_number} tavolina")


#bejme disa testime te kushteve...
if (has_card_payment):
    print ('Po, kemi pagese me karte')
else:
    print ('Jo, nuk kemi pagese me karte')

if (has_shisha_included):
    print ('Po, kemi shisha')
else:
    print ('Jo, fatkeqsisht nuk kemi shisha')

if (not has_shisha_included):
    print("po, nuk ka shisha")


if (has_beers or has_energy_drinks):
    print("kemi birra ose pije energjike")
else:
    print("Me vjen keq por nuk kemi pije per ty...")

if (has_beers and has_energy_drinks):
    print("Po kemi edhe birra dhe pije energjike")
else:
    print("Me vjen keq nuk i kemi te dyja pijet")


#MEPOSHTE FILLON LOGJIKA E BIZNESIT:
print("===============================================================================================================")
print(f"Miresevini ne:  {restaurant_name} {type_bussines}")

#Printo produktet e MENU-se biznesit
print("Menuja e produkteve:")
print (products_list)

# Lexojme emrin  e produktit nga perdoruesi dhe vleren e tij e ruajme tek variabli "ordered_product"
ordered_product = input("Porosit nje produkt duke shkruar emrin e tij: ")
print("ju porositet produktin: " + ordered_product)

# Kontrollojme, nese produkti qe perdoruresi ka porositur, nuk ndodhet ne listen e menuse qe ne ofrojme, atehere do te mbyllim programin!
if (ordered_product not in products_list):
    print("me vjen keq por nuk e kemi kete produkt, te lutem zgjidh nje produkt nga menuja!")
    exit(0) # exit eshte per te nderprere exekutimin e kodit me poshte, persa kohe ne nuk e e kemi kete produkt ne menu.


#Ne fillim afishojme  balancat e restorantit, dhe klientit, gjithashtu dhe canten e klientit, per te pare se ne cfare gjendje jemi
print(f"balanca e vjeter e restorantit eshte: {restaurant_balance}")
print(f"balanca e vjeter e klientit eshte: cash: {client_cash_balance}, card: {client_card_balance}")
print (client_bag)


# Pyesim klientin se cfare menyre pagese ka deshire te perdore per transaksionin:
ans = input("Si do e beni pagesen? (cash / card)")

#kontrollojme pergjigjen e klientit:
#nese klienti kerkon pagese me cash, ath do ja zbresim leket nga balanca cash
if (ans == "cash"):
    print("proceed with cash")
    if (client_cash_balance >= product_price):
            print("proceed with payment")
            client_cash_balance = client_cash_balance - product_price
            restaurant_balance = restaurant_balance + product_price
            client_bag.append(ordered_product) # shto produktin e porositur ne canten e klientit
    else:
        print ("Me vjen keq por nuk keni para mjaftueshem!")

#nese kleinti kerkon pagese me card, ath do ja zbresim leket nga balanca card
elif (ans == "card"):
    print("proceed with card")
    if (has_card_payment):
         if (client_card_balance >= product_price):
            print("proceed with payment")
            client_balance = client_card_balance - product_price
            restaurant_balance = restaurant_balance + product_price
            client_bag.append(ordered_product)# shto produktin e porositur ne canten e klientit
         else:
             print("Ju lutem kontrolloni limitin e kartes tuaj!")
    else:
        print("Ne nuk ofrojme pagesa me card!")


# nese klienti ka shkruar ndonje metode pagese qe nuk e kemi ose qka shkruar metoden gabim, atehere i themi qe nuk e ofrojme kete metode pagese dhe dalim nga programi
else:
    print("nuk e ofrojme kete lloje metode pagese...")
    exit(0)

#afishojme balancat e reja te biznesit / klientit per te pare sesi ka afektuar transaksioni.
print(f"balanca e re e restorantit eshte: {restaurant_balance}")
print(f"balanca e vjeter e klientit eshte: cash: {client_cash_balance}, card: {client_card_balance}")
print("canta e klientit permban:")
print(client_bag)

print(f"Faleminderit qe zgjodhet {restaurant_name} {type_bussines}")
#Te dhenat e Biznesit
restaurant_name : str = "Il gusto italiano"
type_bussines : str = "Restaurant"
product_price: float = 4.6
staff_number : int = 12
table_number : int = 30
has_card_payment : bool = True
has_shisha_included : bool = False
has_gluten_free:bool=True
has_lactose_free:bool=False
products_list: list[str] = ["Pizza", "Spagetti", "Rizotto","Lasagna","Calzone"]
# products_prices: list[float] = [5.6, 8.9, 5.4]
restaurant_balance: float = 800
has_beers: bool = True
has_energy_drinks: bool = False

# Te dhenat e klientit
client_cash_balance: float = 10.2
client_card_balance: float = 5
client_bag: list [str] = [] #per momentin do jete bosh, dhe do mbushet kur klienti te porosise produkte

# afishojme te dhenat e variablave, per te pare nese i kane marre vlerat sic duhet.
print(f"emri i restorantit:  {restaurant_name}")
print("tipi i biznesit: " + type_bussines)
print(f"restoranti ka {staff_number} punonjes")
print(f"restoranti ka {table_number} tavolina")


#bejme disa testime te kushteve...
if (has_card_payment):
    print ('Po, kemi pagese me karte')
else:
    print ('Jo, nuk kemi pagese me karte')

if (has_shisha_included):
    print ('Po, kemi shisha')
else:
    print ('Jo, fatkeqsisht nuk kemi shisha')

if (not has_shisha_included):
    print("po, nuk ka shisha")
if(has_gluten_free):
    print('Po, kemi ushqime pa gluten')
else:
    print('jo fatkqesisht nuk kemi')
if(not has_lactose_free):
    print('po,nuk kemi ushqime pa lactose')
else:
    print('jo,kemi ushqime pa lactose')


if (has_beers or has_energy_drinks):
    print("kemi birra ose pije energjike")
else:
    print("Me vjen keq por nuk kemi pije per ty...")

if (has_beers and has_energy_drinks):
    print("Po kemi edhe birra dhe pije energjike")
else:
    print("Me vjen keq nuk i kemi te dyja pijet")


#MEPOSHTE FILLON LOGJIKA E BIZNESIT:
print("===============================================================================================================")
print(f"Miresevini ne:  {restaurant_name} {type_bussines}")

#Printo produktet e MENU-se biznesit
print("Menuja e produkteve:")
print (products_list)

# Lexojme emrin  e produktit nga perdoruesi dhe vleren e tij e ruajme tek variabli "ordered_product"
ordered_product = input("Porosit nje produkt duke shkruar emrin e tij: ")
print("ju porositet produktin: " + ordered_product)

# Kontrollojme, nese produkti qe perdoruresi ka porositur, nuk ndodhet ne listen e menuse qe ne ofrojme, atehere do te mbyllim programin!
if (ordered_product not in products_list):
    print("me vjen keq por nuk e kemi kete produkt, te lutem zgjidh nje produkt nga menuja!")
    exit(0) # exit eshte per te nderprere exekutimin e kodit me poshte, persa kohe ne nuk e e kemi kete produkt ne menu.


#Ne fillim afishojme  balancat e restorantit, dhe klientit, gjithashtu dhe canten e klientit, per te pare se ne cfare gjendje jemi
print(f"balanca e vjeter e restorantit eshte: {restaurant_balance}")
print(f"balanca e vjeter e klientit eshte: cash: {client_cash_balance}, card: {client_card_balance}")
print (client_bag)


# Pyesim klientin se cfare menyre pagese ka deshire te perdore per transaksionin:
ans = input("Si do e beni pagesen? (cash / card)")

#kontrollojme pergjigjen e klientit:
#nese klienti kerkon pagese me cash, ath do ja zbresim leket nga balanca cash
if (ans == "cash"):
    print("proceed with cash")
    if (client_cash_balance >= product_price):
            print("proceed with payment")
            client_cash_balance = client_cash_balance - product_price
            restaurant_balance = restaurant_balance + product_price
            client_bag.append(ordered_product) # shto produktin e porositur ne canten e klientit
    else:
        print ("Me vjen keq por nuk keni para mjaftueshem!")

#nese kleinti kerkon pagese me card, ath do ja zbresim leket nga balanca card
elif (ans == "card"):
    print("proceed with card")
    if (has_card_payment):
         if (client_card_balance >= product_price):
            print("proceed with payment")
            client_balance = client_card_balance - product_price
            restaurant_balance = restaurant_balance + product_price
            client_bag.append(ordered_product)# shto produktin e porositur ne canten e klientit
         else:
             print("Ju lutem kontrolloni limitin e kartes tuaj!")
    else:
        print("Ne nuk ofrojme pagesa me card!")


# nese klienti ka shkruar ndonje metode pagese qe nuk e kemi ose qka shkruar metoden gabim, atehere i themi qe nuk e ofrojme kete metode pagese dhe dalim nga programi
else:
    print("nuk e ofrojme kete lloje metode pagese...")
    exit(0)

#afishojme balancat e reja te biznesit / klientit per te pare sesi ka afektuar transaksioni.
print(f"balanca e re e restorantit eshte: {restaurant_balance}")
print(f"balanca e vjeter e klientit eshte: cash: {client_cash_balance}, card: {client_card_balance}")
print("canta e klientit permban:")
print(client_bag)

print(f"Faleminderit qe zgjodhet {restaurant_name} {type_bussines}")
