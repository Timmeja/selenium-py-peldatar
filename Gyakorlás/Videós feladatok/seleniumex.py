# Készíts egy Python alkalmazást ami selenium-ot használ.
# Nyisson meg egy Chrome böngészöt és töltsön be egy tetszőleges weblapot az Internetről.
# Az oldalon probáld megtalálni a <div id="nemletezik"></div> mezőt.
# A lényeg, hogy hibát dogjon a driver.find_by_id függvény hívás.

# Feladatot, hogy kezed le ezt a hibát és írj ki valami emberileg olvasható üzenetet.
# Extra feladatként készíts egy saját függvényt, ami
# bármilyen find_by_id lokátor hívásnál lekezeli a nemlétező elem tipusú hibát.
# A megoldáshoz használj python try except struktúrát.
import time

from selenium import webdriver


PATH = 'C:\Windows\chromedriver.exe'
browser = webdriver.Chrome(PATH)
URL = 'https://python.org/'
browser.get(URL)

#not_to_be = browser.find_element_by_id('nemletezik')


def to_be_or_not(id):
    try:
        assert browser.find_element_by_id(id)
    except:
        print('Az elem nincs jelen az oldalon!')

to_be_or_not('nemletezik')
browser.quit()