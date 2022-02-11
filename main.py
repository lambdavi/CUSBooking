from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, ElementNotInteractableException
import datetime
delay=10

# Parameters to set
NAME=""
SURNAME=""
EMAIL=""
PATH_TO_WEBDRIVER=""

def next_weekday(d, weekday):
    days_ahead = weekday - d.weekday()
    if days_ahead <= 0: # Target day already happened this week
        days_ahead += 7
    return d + datetime.timedelta(days_ahead)

def get_weekday():
    return datetime.datetime.today().weekday()

if __name__ == "__main__":
    today = get_weekday()
    if today != 2 and today != 5:
        print("Oggi non e' giorno di prenotazioni")
        exit(1)
    else:
        print("Oggi e' giorno di prenotazioni")
        webdriver = webdriver.Chrome(PATH_TO_WEBDRIVER)
        sleep(2)
        webdriver.get('https://www.custorino.it/easy-sport/')
        webdriver.execute_script("window.scrollBy(0,700);")
        try:
            free_fitness = WebDriverWait(webdriver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/main/div/div/div/section[3]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div[2]/div[1]')))
            free_fitness.click()        
        except TimeoutException:
            print("Loading took too much time!")
        try:
            sala_pesi = WebDriverWait(webdriver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/main/div/div/div/section[3]/div/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[1]/div[2]/div[2]/div/div[1]')))
            sala_pesi.click()       
        except TimeoutException:
            print("Loading took too much time!")
        
        # Seleziono il giorno
        d = datetime.datetime.today()
        if today == 4:
            next_monday = next_weekday(d, 0) # 0 = Monday, 1=Tuesday, 2=Wednesday...
            print(next_monday.day)
            next_day_to_book = next_monday.day
            next_hour_to_book = "17:00 - 18:30"
        else:
            next_monday = next_weekday(d, 3) # 0 = Monday, 1=Tuesday, 2=Wednesday...
            print(next_monday.day)
            next_day_to_book = next_monday.day
            next_hour_to_book = "18:30 - 20:00"

        webdriver.execute_script("window.scrollBy(0,700);")
        try:
            sleep(3)
            nextD = WebDriverWait(webdriver, delay).until(EC.presence_of_element_located((By.XPATH, f"//*[contains(text(),'{next_day_to_book}')]")))
            nextD = webdriver.find_elements_by_xpath(f"//*[contains(text(),'{next_day_to_book}')]")
            # Naive algorithm to find day in the calendar
            # TODO: find better algorithm
            for opt in nextD:
                try:
                    opt.click()
                    break
                except ElementNotInteractableException:
                    pass
        except TimeoutException:
            print("Loading took too much time!")
        try:
            sleep(1)
            nextH = WebDriverWait(webdriver, delay).until(EC.presence_of_element_located((By.XPATH, f"//*[contains(text(),'{next_hour_to_book}')]")))
            nextH.click()
        except TimeoutException:
            print("Loading took too much time!")
        # Clicca continua
        try:
            continua = WebDriverWait(webdriver, delay).until(EC.presence_of_element_located((By.ID, "am-continue-button")))
            continua.click()
        except TimeoutException:
            print("Loading took too much time!")
        
        webdriver.execute_script("window.scrollBy(0,400);")
        try:
            sleep(2)
            name_input = WebDriverWait(webdriver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/main/div/div/div/section[3]/div/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[2]/div[3]/div[2]/div[3]/div[1]/form/div[1]/div[3]/div/div/div/input')))
            name_input.send_keys(NAME)
            surname_input = webdriver.find_element_by_xpath('/html/body/div[1]/main/div/div/div/section[3]/div/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[2]/div[3]/div[2]/div[3]/div[1]/form/div[1]/div[4]/div/div/div/input')
            surname_input.send_keys(SURNAME)
            email_input = webdriver.find_element_by_xpath('/html/body/div[1]/main/div/div/div/section[3]/div/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[2]/div[3]/div[2]/div[3]/div[1]/form/div[1]/div[5]/div/div/div/input')
            email_input.send_keys(EMAIL)
        except TimeoutException:
            print("Loading took too much time!")
        
        try:
            confirm = WebDriverWait(webdriver, delay).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'Conferma')]")))
            #confirm.click()
            print("CONFERMA!")
        except TimeoutException:
            print("Loading took too much time!")
    exit(0)
