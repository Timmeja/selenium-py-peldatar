# Készíts egy Python alkalmazást ami selenium-ot használ.
# Indítsd el lokálisan a selenium-py-peldatar alkalmazást.
# A program töltse be a példatárból az http://localhost:9999/another_form.html oldalt.
# A program segítségével olvassd be a csv tartalmat.
# A feladatod, hogy az oldalon található formanyomtatvány segítségével feltöltsd a táblázatot.
# Használd a Python CSV könyvtárát. A feltöltött táblázatot ellenőrizheted ha a probramod letölti
# a táblázat alatti gomb segítségével az aktuális tartalmat. Hasonlítsd össze python kódból a kapott
# file-t, hogy identikus-e az eredetivel.
# A megoldást egy csvfeltoltes.py nevű fileban kell beadnod.
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import csv

browser = webdriver.Chrome(ChromeDriverManager().install())
URL = 'http://localhost:9999/another_form.html'
browser.get(URL)
browser.maximize_window()


def get_input_field(id):
    element = browser.find_element_by_id(id)

    return element


send_btn = browser.find_element_by_id('submit')
with open('table_in.csv', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    # fullname = []
    # email:= []
    # dob:
    for row in csvreader:
        # print(row)
        get_input_field('fullname').send_keys(row[0])
        get_input_field('email').send_keys(row[1])
        get_input_field('dob').send_keys(row[2])
        get_input_field('phone').send_keys(row[3].strip())
        send_btn.click()
        time.sleep(1)
        get_input_field('fullname').clear()
        get_input_field('email').clear()
        get_input_field('dob').clear()
        get_input_field('phone').clear()

download_btn = browser.find_element_by_xpath('//button')
download_btn.click()

with open('C:/Users/Timmeja/Downloads/table (1).csv', 'r', encoding='UTF-8') as assert_file:
    text_content = assert_file.readlines()
    text_content_assert = []
    for i in text_content:
        text_content_assert.append(i)
    print(text_content_assert)
with open('table_in.csv', 'r', encoding='utf-8') as csvfile:
    csvreader = csvfile.readlines()
    print(csvreader)
# try:
    assert text_content_assert == csvreader
#     print('Az adatmentés sikeres!')
# except AssertionError:
#     print('Az adatmentés sikertelen')


