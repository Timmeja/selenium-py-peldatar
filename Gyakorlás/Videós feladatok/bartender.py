# Kérd be a felhasználó életkorát, és kérdezd meg, mit iszik. Kétféle italt ismerünk:
# sör és kóla. Ha a felhasználó kiskorú, és sört kér, akkor közöld vele, hogy sajnos nem adhatsz neki.
# Ha a felhasználó 60 feletti, és kólát kér, akkor közöld vele, hogy a koffein megemelheti a vérnyomását.
# Ha ismeretlen italt adott meg, akkor írd ki, hogy csak sört és kólát tudunk adni.
# Minden más esetben szolgáld ki. (Írd ki pl. "Parancsoljon, a söre." vagy "Parancsoljon,a kólája.")

user_age = int(input('Felhasználó életkora: '))
drink = input('Mit iszik? ')

if user_age < 18 and drink == 'sör':
    print('Kiskorút sajnos nem szolgálhatok ki alkohollal!')
elif user_age > 60 and drink == 'kóla':
    print('A koffein megemelheti a vérnyomását!')
elif drink != 'sör' and drink != 'kóla':
    print('Sajnos csak sört és kólát tudunk adni!')
else:
    print(f'Parancsoljon a {drink}!')
