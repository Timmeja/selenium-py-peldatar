# Készíts egy Python alkalmazást ami selenium-ot használ.
# Nyisson meg egy Chrome böngészöt és töltsön be egy tetszőleges weblapot az Internetről.
# A megoldást egy start.py nevű fileban kell beadnod.

from selenium import webdriver
PATH = 'C:\Windows\chromedriver.exe'
browser = webdriver.Chrome(PATH)
URL = 'https://progmasters.hu/'
browser.get(URL)