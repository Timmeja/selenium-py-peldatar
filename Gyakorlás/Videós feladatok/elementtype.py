# Készíts egy Python alkalmazást ami selenium-ot használ. Indítsd el lokálisan a selenium-py-peldatar alkalmazást.
# A program töltse be a példatárból az http://localhost:9999/trickyelements.html oldalt.
# Használj id lokátort és keressd ki az elemenekt egyesével.
# A legelső olyan elemre ami button típusú kattints rá és ellenőrizd,
# hogy a helyes szöveg jelenik-e meg az elemek listája alatt.
import time

from selenium import webdriver

PATH = 'C:\Windows\chromedriver.exe'
browser = webdriver.Chrome(PATH)
URL = 'http://localhost:9999/trickyelements.html'
browser.get(URL)

# random_btn = browser.find_element_by_id('randomized')
# difficulty_btn = browser.find_element_by_id('difficulty')
# btn_1 = browser.find_element_by_id('element'+str(1))
# btn_2 = browser.find_element_by_id('element2')
# btn_3 = browser.find_element_by_id('element3')
# btn_4 = browser.find_element_by_id('element4')
# btn_5 = browser.find_element_by_id('element5')


# def btn_click(btn_id):

for i in range(1, 6):
    id = 'element' + str(i)
    btn_id = browser.find_element_by_id(id)
    btn_id.tag_name == 'button' and btn_id.is_enabled()
    btn_id.click()
    time.sleep(1)
    result = browser.find_element_by_id('result')
    if result.text == f'{id} was clicked':
        print(f'{id} result is OK!')
    else:
        print(f'{id} No button!')

time.sleep(2)

print('I am done')
time.sleep(2)
browser.quit()
