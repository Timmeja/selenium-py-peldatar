# Írj programot, ami kiírja a kisbetűket, és melléjük a karakter kódjukat!
# A kiírás több oszlopos legyen, és legfeljebb 10 soros.

import abc

oszlop1 = []
oszlop2 = []
oszlop3 = []

for i in range(97, 123, 1):
    char_num = chr(i) + ' ' + str(i)
    if (i - 97) <= 9:
        oszlop1.append(char_num)
    elif (i - 97) <= 19:
        oszlop2.append(char_num)
    else:
        oszlop3.append(char_num)
for i in range(0, 9, 1):
    if i <= 5:
        oszlopok = oszlop1[i] + ' ' + oszlop2[i] + ' ' + oszlop3[i]
    else:
        oszlopok = oszlop1[i] + ' ' + oszlop2[i]

    print(oszlopok)





