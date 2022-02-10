from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import datetime

# Parameters to set
NAME=""
SURNAME=""
EMAIL=""

def get_weekday():
    return datetime.datetime.today().weekday()

if __name__ == "__main__":
    today = get_weekday()
    if today != 2 and today != 5:
        print("Oggi non e' giorno di prenotazioni")
    else:
        print("Oggi e' giorno di prenotazioni")
        webdriver = webdriver.Chrome('/home/davide/mydev/CUSBooking/chromedriver')
        sleep(2)
        webdriver.get('https://www.custorino.it/easy-sport/')
        sleep(3)
        webdriver.execute_script("window.scrollBy(0,700);")
        sleep(1)
        free_fitness = webdriver.find_element_by_xpath(
        '/html/body/div[1]/main/div/div/div/section[3]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div[2]/div[1]')
        free_fitness.click()
        sleep(2) 
        sala_pesi = webdriver.find_element_by_xpath(
        '/html/body/div[1]/main/div/div/div/section[3]/div/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[1]/div[2]/div[2]/div/div[1]')
        sala_pesi.click()
        sleep(3)
        # Seleziono il giorno
        webdriver.execute_script("window.scrollBy(0,700);")
        sleep(1)
        next_day_to_book = "14"
        nextD = webdriver.find_elements_by_xpath(f"//*[contains(text(),'{next_day_to_book}')]")
        nextD[1].click()
        sleep(1)
        # Seleziono l'ora
        next_hour_to_book = "17:00 - 18:30"
        nextH = webdriver.find_element_by_xpath(f"//*[contains(text(),'{next_hour_to_book}')]")
        #print(nextH.get_attribute('innerHTML'))
        nextH.click()
        sleep(1)
        # Clicca continua
        continua = webdriver.find_element_by_id("am-continue-button")
        continua.click()
        sleep(3)
        webdriver.execute_script("window.scrollBy(0,400);")
        sleep(1)
        name_input = webdriver.find_element_by_xpath('/html/body/div[1]/main/div/div/div/section[3]/div/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[2]/div[3]/div[2]/div[3]/div[1]/form/div[1]/div[3]/div/div/div/input')
        name_input.send_keys(NAME)
        surname_input = webdriver.find_element_by_xpath('/html/body/div[1]/main/div/div/div/section[3]/div/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[2]/div[3]/div[2]/div[3]/div[1]/form/div[1]/div[4]/div/div/div/input')
        surname_input.send_keys(SURNAME)
        email_input = webdriver.find_element_by_xpath('/html/body/div[1]/main/div/div/div/section[3]/div/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[2]/div[3]/div[2]/div[3]/div[1]/form/div[1]/div[5]/div/div/div/input')
        email_input.send_keys(EMAIL)
        sleep(2)
        confirm = webdriver.find_element_by_xpath("//*[contains(text(),'Conferma')]")
        #confirm.click()
