
mes: float = 0
total: float = 0

#  Calculate the total of 5 numbers
for i in range(1, 6):
    nr = float(input("give your number:")) # we should not allow the user to enter alpha chaars
    total = total + nr


# Find the average of the total
mes = total / 5

#Print the calculated average
print (f"Mesatarja e 5 numrave te dhene eshte: {mes}")