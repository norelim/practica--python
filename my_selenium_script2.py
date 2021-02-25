from selenium.webdriver import Chrome
#driver = Chrome()

#Como gestor de contexto

with Chrome() as driver:
#your code inside this indent
	driver.get("https://www.google.com/")
print(driver.page_source)
#Chrome(executable_path='/path/to/chromedriver')


#driver.find_element_by_id("element_id")
#CON DATO => driver.find_element(By.ID, "cheese")
#//*[@id="input"] este es el xpath que me traigo de la pagina
xpath = "//*[@id= driver.input]"
searchinput = driver.find_element_by_xpath(xpath)
searchinput.send_keys("Barack Obama age")
searchinput.send_keys(Keys.ENTER)

#//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[1]/input
xpathresult = "//*[@id= xpath.tsf]/div[2]/div[1]/div[1]/div/div[1]"
resultdiv = driver.find_element_by_xpath(xpathresult)
age = resultdiv.text
print("Barack Obama is getting old. Currently, his age is",age)


