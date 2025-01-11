# KETO JANE DEKLARIMET:

original_word: str = "";
new_chars: list[chr(1)] = []
new_word: str = ""

#1. KRIJIMI / DEKLARIMI
#def - definition - percakto/krijo nje funksionalitet
#name: capitalize - merr nje string cfaredo, dhe shkronjat e atij strinu ti kthen ne kappitale.
#2. MARRJA E PARAMETRAVE - word_word - input (cfaredo / ne presim vetem fjale me shkronnja te vogla, jo karaktere te tjera)
def capitalize (old_word):

    #3. PROCESI

    # boshatis listen e karaktereve
    new_chars: list[chr(1)] = []

    word_length : int = len(old_word)
    # print(f"Gjatesia e fjales se dhene eshte: {word_length}")

    # krijojme nje loop, qe iteton/perserit veprimet aq here sa shkonja ka fjala
    for i in range(0, word_length):
        #printojme skronjen e cdo fjale, sipas indexeve
        # print(f"indexi eshte {i}")
        alpha = old_word[i]
        # print(f"shkonja respektive eshte: {alpha}")

        #gjejme kodin e e shkronjes respektive
        code: int = ord(alpha)
        # print(f"kodi i shkronjes se pare eshte: {code}")

        if (code >= 97 and code <= 128):
            #bej kalkulimet e nevojshme, ne menyre qe shkronja e vogel te behet e madhe
            new_code = code - 32 #meqe shkonjat e voglja kane 32 njesi diference me shkronjat e medha sipas kodeve ASCII, ju zbresim vleren 32 per ti kthyer ne te medha

            #printojme kodin e shkronjes se re(te madhe)
            # print(f"kodi i shkronjes se re eshte: {new_code}")

            #gjejme shkronjen respektive te kodit te ri
            alpha: chr = chr(new_code)

            #afishojme shkronjen e re (SHKRONJA E MADHE)
            # print(f"Rikthimi i kodit asccii ne shkronje {aplha}")
        else:
            print(f"karakteri '{alpha}' nuk u ndryshua sepse nuk eshte shkronje")

        #ruaje karakterin e vjete/ri tek lista, nuk ka rendesi nese ndryshoi apo jo.
        new_chars.append(alpha)
        # print(f"shkonjat e shnderruara deri tani jane {new_chars}")

    new_word = "".join(new_chars)
    # print(f"Fjala e re e formuar eshte: {new_word}")


    #4. OUTPUT
    return new_word


# LOGJIKA E KODIT - FILLON KETU

original_word = "laptop123"

print(f"Input - original Word: {original_word}")

# PERDORIMI I FUNKSIONIT
# emri (capitalize)
# INPUT - word - jepni nje fjale cfare nepermjet variablit original_word
# OUPUT - new_word - > vlera e re do ruhet tek variable new_word
new_word = capitalize(original_word)
print(f"Fjala e re eshte: {new_word}")