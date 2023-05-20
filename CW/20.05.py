from selenium import webdriver
from selenium.webdriver.common.by import By

from time import sleep

browser = webdriver.Chrome()

browser.get('https://clickclickclick.click/')

button = browser.find_element(by= By.CLASS_NAME,
                              value = 'button')
assert button.is_displayed()

for elem in range(10):
    button.click()
    sleep(5)
    
browser.close()

'''
1. Почитать о HTML:
    https://ru.wikipedia.org/wiki/HTML
2. Почитать о XPATH:
    https://ru.wikipedia.org/wiki/XPath
3. Найти на сайте https://ru.wikipedia.org/wiki/XPath при помощи XPATH следующее:
   - текст Xpath
   - вкладка "Ссылки"
   - Вкладка "Править ссылки"
   - кнопка "История"
4. Почитать о Selenium:
    https://www.selenium.dev

'''




