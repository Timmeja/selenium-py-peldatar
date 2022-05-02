# Készíts egy Python alkalmazást ami selenium-ot használ. Indítsd el lokálisan a selenium-py-peldatar alkalmazást.
# A program töltse be a példatárból az http://localhost:9999/kitchensink.html oldalt.
# Gyakorlás képpen keress ki elemekt a képernyőről az alábbi kritériumoknak megfelelően:
# ID alapján
# NAME alapján
# XPath kifejezéssel Minden megtalált elemnek irassd ki a text értékét, vagy egy attribútum értékét.

from selenium import webdriver

PATH = 'C:\Windows\chromedriver.exe'
browser = webdriver.Chrome(PATH)
URL = 'http://localhost:9999/kitchensink.html'
browser.get(URL)

radio_btn_example = browser.find_element_by_xpath('//*[@id="radio-btn-example"]/fieldset/label[3]')
print(radio_btn_example.text)
class_select_example = browser.find_element_by_xpath('//*[@id="carselect"]/option[2]')
print(class_select_example.text)
open_window = browser.find_element_by_id('openwindow')
print(open_window.get_attribute('type'))
course_name = browser.find_element_by_xpath('//*[@id="product"]/tbody/tr[2]/td[2]')
print(course_name.text)

browser.quit()


