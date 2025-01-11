#Duhet korrelimi midis fjales pizza dhe cmimit perkates



def find_maxINDEX(list):
    priceHIGH_index = list.index(max(cmimet))
    return priceHIGH_index

def find_lowINDEX(list):
    priceLOW_index = list.index(min(cmimet))
    return priceLOW_index


menu : list[str] = []
cmimet : list[int] = [100, 200, 300]
menu.append("pizza")
menu.append("spaghetti")
menu.append("fish")


print(menu)

# menu.remove("spaghetti")
# print("Since spaghetti is index 1 we remove it.")
# print(menu)
#
# if "spaghetti" in menu:
#     print("There is spaghetti in the menu ")
#
# else:
#     print("There is no spaghetti in the menu ")

print(cmimet)


#cili ka cmimin me te larte

priceHIGH_index = find_maxINDEX(cmimet)

menu.pop(priceHIGH_index)
cmimet.pop(priceHIGH_index)


priceLOW_index = find_lowINDEX(cmimet)
priceHIGH_index = cmimet.index(max(cmimet))

print(menu)
print(cmimet)
print(f"{menu[priceHIGH_index]} ka cmimin me te larte")
print(f"{menu[priceLOW_index]} ka cmimin me te ulet")








