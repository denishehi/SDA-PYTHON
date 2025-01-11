print("hello world!")
restaurant_name:str="Meksikani"
product_price:float=4.5
product_name:str="burrito"
preparation_time:float=5.2
is_gluten_free:bool=True
#staf_members:list="menaxheri"
has_card_paymant:bool=True
print(restaurant_name)
print(product_price)
print(preparation_time)
print(is_gluten_free)
print(has_card_paymant)
if not has_card_paymant:
    print("nuk mund te paguani me karte")
else:
    print("po ne pranojme pagesa me karte")
if is_gluten_free:
    print("po kemi produkte pa gluten")
else:
    print("nuk kemi produkte pa gluten")