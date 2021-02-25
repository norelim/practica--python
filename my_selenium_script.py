#Asignación simple
from selenium.webdriver import Chrome
driver = Chrome()

from selenium.webdriver import Chrome

with Chrome() as driver:
#your code inside this indent
	driver.get("https://www.google.com/")
	driver.find_element_by_id("input")
print(driver.page_source)
Chrome(executable_path='/path/to/chromedriver')


#<input id="input" type="search" autocomplete="off" spellcheck="false" aria-live="polite" placeholder="Buscar en Google o escribir una URL">
