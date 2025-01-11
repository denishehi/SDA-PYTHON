import random
#Ketu bejme deklarimin dhe konfigurimet (inicializimin/vleredhenien) e variablave qe do na duhen per mbarevajtjen e programit (lojes)
#ne menyre qe:
# Nese duam qe ta bejme me 5 attempts, mjafton qe te ndryshojme vleren e variablit "MAX_ATTEMPTS=5", pa prekur logjiken e programit
#Nese duam qe numri te jete nga 1-20, mjafton qe te ndryshojme konfigurimin e variablit "MAX_NUMBERS=20", pa prekur logjiken e programit
is_playing: bool = True
MAX_NUMBERS: int = 15
MAX_ATTEMPTS: int = 3
price:int=5000
attempts: int
lucky_number: int
guessed_number: int
answer: str

# ky eshte LOOP i pare, (i jashtem) do te perseritet persa kohe qe lojtari do te kete deshire, i cili do te varet nga variabli "is_playing"
while is_playing:
    # percdo loje te re, marrim nje numer random te ri, dhe konfigurojme variablat me vlerat fillestare
    lucky_number: int = random.randint(1,MAX_NUMBERS)
    was_found = False
    attempts = MAX_ATTEMPTS

    print(f"Guess a number (1-{MAX_NUMBERS}) brenda {MAX_ATTEMPTS} mundesive")

    # ky eshte LOOP i i dyte, (i brendshem) do te perseritet max 3 here, ose do te nderpritet nese lojtari e gjen para heres se 3
    while attempts > 0:
        #percdo round, i japim mundesine lojtarit te gjeje numrin e fatit
        answer = input(f"Guess a number (attempts: {attempts}): ")
        # meqe numri i futur nga tastiera eshte i tipit string, ne duhet ta convertojme ate ne fillim ne tipin int, me pas do ta perdorim si numer
        guessed_number = int(answer)

        # nese do keni ndonje error, mund te beni uncomment keto 2 rrjeshta per te pare vlerat e 2 variablave ne kohe reale
        # print(f"guessed_number: {guessed_number} / type: {type(guessed_number)}")
        # print(f"lucky_number: {lucky_number} / type: {type(lucky_number)}")

        if guessed_number == lucky_number:
            was_found = True
            break #meqe lojtari e gjeti numrin para qe ti zerohen te gjitha mundesite, dalim nga LOOP
        else:
            # ne momentin qe lojtari provoi nje numer, atehere sapo i humbi nje mundesi...
            attempts -= 1
            # nese lojtarit i ka ngelur edhe ndonje mundesi, atehere do ta ndihmojme per roundin e radhes
            if attempts > 0:
                print("Provo perseri!")
                if lucky_number > guessed_number:
                    direction = "lart"
                else:
                    direction = "poshte"
                print(f"Hint: kerko me {direction}")
    if was_found:
        print("Bravo ti fitove llotarine!!")
    else:
        print("Sapo humbe!")
    print(f"Guessed number was: {lucky_number}")

    answer = input("Deshiron te luash perseri? (yes / no): ")

    if answer != "yes":
        is_playing = False

print("Loja mbaroi, bye!")