name:str="ana"
grades:list[int]=[7,8,8,7]
mes:float=0
tot:float=0
tot_grades=grades[0]+grades[1]+grades[2]+grades[3]
mes_grades=tot_grades/len(grades)
print(tot_grades)
print(mes_grades)
if(mes_grades<=4):
    print("Ju nuk e perfitoni bursen")
elif(mes_grades >= 7 and (mes_grades <= 9)):
    print("ju perfitoni 50% burse falas")
else:
    print("Ju e perfitoni falas te gjithe bursen")
