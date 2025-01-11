# Komente dhe printime

# Ky është një koment  (#)
#ky eshte nje printim i nje texti te thjeshte ne ekran (print)
print("Përshëndetje!")

#Variablat / Datatypes: https://www.w3schools.com/python/python_datatypes.asp
print("==================== VARIABLAT / DataTypes (str / chr / float / int / bool / list[type]) ====================")
#   int -> integer (numer i plote)
#   float -> (nr me presje)
#   str -> string -> (bashkesi karakteresh)
#   chr -> character -> (1 simbol i vetem)
#   bool -> Boolean -> (vlere logjike) -> True ose False
#   list -> (varg/grupim vlerash te nje tipi te caktuar)

product_name: str = "Pizza"
person_gender : chr(1) = "M"
product_price: float = 2.6
person_age: int = 27
is_free_product: bool = True
products : list[str] = ["Rizoto", "Pasta", "Patato"]

print(f"Produkti: {product_name}, Cmimi: {product_price}, gender: {person_gender}, age: {person_age}, is_free: {is_free_product}")
print("products:", products)

# leximi nga tastiera (input) : https://www.w3schools.com/python/ref_func_input.asp
print("==================== INPUT ====================")
name: str = input("Si quheni? ")
print(f"Miresevini {name}!")

print("==================== OPERATORET ARITMETIKE (+ - * ** / // %) ====================")
# Veprime aritmetike  (+ - * ** / // %)
x: int = 5
y: int = 2

# = perdoret per vleredhenie, kalkulimi qe ndodh ne te djathte, do ti ruhet variablit ne te majte...
sum: int = x + y
diff: int = x - y
pro: int = x*y
pje: float = x / y
exp: int = x ** 3
plo: int = x // y
mbetja: float = x % y

print(f"x: {x}, y: {y}, Shuma: {sum}, Diferenca: {diff}, Prodhimi: {pro}, Pjesëtimi: {pje}, plotpjesëtimi: {plo}, mbetja: {mbetja}, exp: {exp}")

#Konvertimi / Casting i vlerave
print("KONVERTIMI / Casting i vlerave")
age_text: str = "23" # ky duke numer, por eshte string (sepse eshte ne thonjeza) si i tille nuk gezon vetite e numrave...
age_num = int(age_text) # meqe duam t'ia rrisim moshen me 1, atehere duhet qe ne fillim ta konvertojme kete string ne numer
age_num += 1 # tani qe stringu eshte konvertuar ne numer, mund te bejme cfaredo lloje veprimi aritmetik, e rrisim moshen me 1
print(f"mosha u be: {age_num}") #mosha ne kete moment u be 24
# Krahasimet
print("==================== OPERATORET E KRAHASIMIT (>, <, >=, <=, ==, !=) ====================")
print(f"x: {x}, y: {y}")
if x == y:
    print("x dhe y janë të barabartë")
if x > y:
    print("x eshte me i madh y")
if x < y:
    print("x eshte me i vogel y")
if x != y:
    print("x dhe y janë të ndryshëm")

print("==================== OPERATORET E DECISIONS (if / elif / else) ====================")
# KUSHTET  (if / elif / else)
print(f"x: {x}, y: {y}")
if x > y:
    print("x është më i madh se y")
elif x == y:
    print (" x eshte i barabarte me y")
else: #ketu mund te ishte kushti (x < y) por nuk e specifikojme, sepse meqe jane 3 kushte ne total, 2 te parat i speficikuam, i treti ndodh ne else.
    print("x nuk është më i madh se y")


print("==================== OPERATORET LOGJIKE bool (and / or / not) ====================")
# LIDHJET LOGJIKE (and / or / not)
has_money: bool = True
has_card: bool = False
print(f"has_money: {has_money}, has_card: {has_card}")

if has_money:
    print("ka para cash")

if not has_card:
    print("nuk ka Card")

if has_money or has_card:
    print("Ne kemi nje menyre pagese...")

if has_money and not has_card:
    print("Paguaj me vetem me para")

#LOOPS:
print("==================== LOOPS (FOR / WHILE) ====================")
#FOR - Loop Example
for i in range (1, 10):
    print(f"hello {i}")


#WHILE - Loop Example
is_playing: bool = True

while is_playing:
    print("Jam duke luajtur...")
    answer = input("deshiron te luash perseri? (po/jo)")
    if (answer != "po"):
        is_playing = False

#FUNCTIONS:
print("==================== FUNCTIONS (Deklarimi (Emri (qellimi i funksionaliteti) / Parametrat(input) ) / Procesi (Logjika) / Rezultati(Output) / Aktivizimi ) ====================")
def add(a: int, b: int):
    return a + b

# Calling the function and storing the result
x = 2
y = 3
print(f"x: {x}, y: {y}")
result = add(x, y)
print("The sum is:", result)

x = 5
y = 8
print(f"x: {x}, y: {y}")
result = add(x, y)
print("The sum is:", result)

#LIBRARIES / Modules (using existing functions)
print("LIBRARIES / Modules (using existing functions)")
import random

lucky_number: int
print("marrim nje vlere te rastesishme duke perdorur funksionin e gatshem 'randint()' i cili eshte pjese e modulit 'random'")
lucky_number = random.randint(1,10)
print(f"My lucky number is {lucky_number}")

# STRINGS
print("==================== STRINGS (str / chr / index / methods) ====================")
# ky eshte nje variabel string
# stringu identifikohet nga indexi, i cili fillon nga 0
welcome: str = "Hello World"
# ketu afishojme gjithe stringun
print(f"Stringu eshte: {welcome}")

#ketu afishojme karakterin e pare
print(f"karakteri i pare, ne indexin 0, ndodhet shkronja: {welcome[0]}")

#ketu afishojme karakterin e dyte
print(f"karakteri i dyte, ne indexin 1, ndodhet shkronja: {welcome[1]}")

#ketu afishojme karakterin e fundit
print(f"karakteri i fundit, ne indexin length-1, ndodhet shkronja: {welcome[len(welcome)-1]}")

# ketu gjejme kodin e nje karakteri: https://www.ascii-code.com/
# ord eshte nje funksion qe na tregon kodin  e nje karakteri specifik
print(f"Kodi i karakterit {welcome[0]} eshte: {ord(welcome[0])}")

# chr() eshte nje funksion qe na tregon karakterin korrenspondues sipas kodeve ascii (1-255)
print("karakteri korrenspondues i kodit 97 eshte: ", chr(97))

#String Methods: https://www.w3schools.com/python/python_ref_string.asp
print(f"Stringu ka {len(welcome)} karaktere")
print(f"Stringu me shkronja te vogla eshte: {welcome.lower()}")
print(f"Stringu me shkronja te medha eshte: {welcome.upper()}")
print(f"Zevendesimi i fjales 'World' me fjalen 'Bote' : {welcome.replace('World', 'Bote')}")

print("Trajtimi i cdo karakteri te string-ut ne menyre dinamike nepermjet perdorimit te cikleve/loops")
for i in range (len(welcome)):
    print(f"index: {i}, karakter: {welcome[i]}")

# LISTS:
print("==================== LISTS Types (str / nr / chr / float / bool ) / Indexing / Methods ====================")

names : list[str] = ["Genti", "Goni", "Tomi", "Ana"]
ages: list[int] = [25, 26, 30, 45]
are_single: list[bool] = [True, False, True, True]
grades: list[float] = [6.7, 9.6, 7.5, 10.0]

print(f"list of strings: names: ", names)
print(f"list of integers: ages: ", ages)
print(f"list of floats: notat: ", grades)
print(f"list of booleans: are_single: ", are_single)

index: int = 0
print(f"Te dhenat e personit te pare ndodhen ne index: {index}")
print(f" {names[index]} eshte {ages[index]} vjec, statusi single: {are_single[index]}, nota: {grades[index]}")

if are_single[index]:
    print(f" {names[index]} eshte single")
else:
    print(f" {names[index]} nuk eshte single")

#LIST METHODS: https://www.w3schools.com/python/python_ref_list.asp
#Rendisim vlerat e listes nga ne rendin rrites A-Z / 0-9
names.sort()
print("Emrat e renditur ne rendit rrites jane: ", names)

#Rendisim vlerat e listes nga ne rendin zbrites Z-A / 9-0
grades.sort(reverse=True)
print("Moshat e renditura ne rendin zbrites jane: ", grades)

print(f"Lista e emrave ka {len(names)} elemente")

print("Fshijme emrin 'Ana' nga lista e emrave")
names.remove("Ana")
print(f"Lista e re e emrave eshte: ", names)
print(f"Lista e emrave ka {len(names)} elemente")

print("Printimi i gjithe elementeve te listes se emrave duke perdor ciklet/loops")
for i in range (len(names)):
    print(f"index: {i}, item: {names[i]}")