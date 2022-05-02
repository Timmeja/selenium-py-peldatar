# Szökőév?
# Készíts függvényt, amelyik adott évszámról eldönti, hogy az szökőév-e. Szökőév minden negyedik, nem szökőév minden századik,
# mégis az minden 400-adik. (2000-ben ezért volt szökőév.) A függvény visszatérési értéke legyen logikai típusú!
# Tipp( % maradekos osztas operátor) Írj programot, amelyik a felhasználótól évszámokat kér,
# és mindegyikre kiírja, hogy szökőév-e! Használd az előbb megírt függvényt! Például: ?
# 2005 Nem szökőév. ? 2000 Szökőév. ? 1980 Szökőév. ? 1900 Nem szökőév.

user_input = int(input('Kérek egy évszámot!: '))
if user_input % 400 == 0:
    print(user_input)
    print(True)
    print('A megadott év szökőév')
elif user_input % 100 == 0:
    print(user_input)
    print(False)
    print('A megadott év nem szökőév')
elif user_input % 4 == 0:
    print(user_input)
    print(True)
    print('A megadott év szökőév')
else:
    print(user_input)
    print(False)
    print('A megadott év nem szökőév')
