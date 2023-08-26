from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.edge import service
from random import *
import os
os.system("cls") #clear screen from previous sessions
import time
import json # for cookies

cookies_path = 'auth/cookies.json'
local_storage_path = 'auth/local_storage.json'
your_user_agent = "Super_Cool_User_Agent" # Replace with your desired user-agent STRING. You can find your current browser's user-agent by searching "What's my user-agent?" in a search engine

options = webdriver.EdgeOptions()
options.use_chromium = True
options.add_argument("start-maximized")
options.page_load_strategy = 'eager' #do not wait for images to load
options.add_argument("user-agent=" + your_user_agent) 
options.add_experimental_option("detach", True)

s = 20 #time to wait for a single component on the page to appear, in seconds; increase it if you get server-side errors «try again later»

driver = webdriver.Edge(options=options)
action = ActionChains(driver)
wait = WebDriverWait(driver,s)

number_of_messages=4
message = []
for i in range(number_of_messages): #the number of messages in the directory
    text_file = open("messages/linkedin-invitation-"+str(i)+".txt", "r")
    message.append(text_file.read())
    text_file.close()

username = "nakigoetenshi@gmail.com"
password = "Super_Mega_Password"
login_page = "https://www.linkedin.com/login"

weekly_limit=200
weekly_limit -=5 # just for the sake of safety, besides, You want to be able to add some connections by hand!
weekly_counter = 0 #load from file!
text_file = open("linkedin-weekly-counter.txt", "r")
weekly_counter = int(text_file.readline())
text_file.close()

search_link = "https://www.linkedin.com/in/nakigoe-angel/" # replace

def load_data_from_json(path): return json.load(open(path, 'r'))
def save_data_to_json(data, path): json.dump(data, open(path, 'w'))

def add_cookies(cookies): [driver.add_cookie(cookie) for cookie in cookies]
def add_local_storage(local_storage): [driver.execute_script(f"window.localStorage.setItem('{k}', '{v}');") for k, v in local_storage.items()]

def success(): return True if wait.until(EC.presence_of_element_located((By.XPATH, '//div[contains(@class,"global-nav__me")]'))) else False

def navigate_and_check(search_link):
    driver.get(search_link)
    time.sleep(15)
    if success(): # return True if you are loggged in successfully independent of saving new cookies
        save_data_to_json(driver.get_cookies(), cookies_path)
        save_data_to_json({key: driver.execute_script(f"return window.localStorage.getItem('{key}');") for key in driver.execute_script("return Object.keys(window.localStorage);")}, local_storage_path)
        return True
    else: 
        return False
   
def login():
    wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@id="username"]'))).send_keys(username)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@id="password"]'))).send_keys(password)
    action.click(wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Sign in")]')))).perform()
    time.sleep(15)
    
def check_cookies_and_login():
    driver.get(login_page) # you have to open some page first before trying to load cookies!
    time.sleep(3)
    
    if os.path.exists(cookies_path) and os.path.exists(local_storage_path):
        add_cookies(load_data_from_json(cookies_path))
        add_local_storage(load_data_from_json(local_storage_path))
        
        if navigate_and_check(search_link):
            return # it is OK, you are logged in
    
    driver.get(login_page)
    time.sleep(3)
    login()
    navigate_and_check(search_link)
        
def scroll_to_bottom(): 
    reached_page_end= False
    last_height = driver.execute_script("return document.body.scrollHeight")
    
    #expand the skills list:
    while not reached_page_end:
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(2)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if last_height == new_height:
            reached_page_end = True
        else:
            last_height = new_height
            
def connect(name):
    try:
        #add note button:      
        action.click(wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Add a note"]')))).perform()
        
        #store the person's name and attach to the random message to reduce automation detection:
        personalized_message = "Dear " + name + "\n" + message[randint(0,number_of_messages-1)]
        
        cover_letter_text = wait.until(EC.element_to_be_clickable((By.XPATH, '//textarea[@id="custom-message"]')))
        
        cover_letter_text.send_keys(personalized_message) 
        send_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Send now"]')))
        action.move_to_element(send_button).perform()
        time.sleep(0.5)
        action.click(send_button).perform()
        time.sleep(1)
        return 0 #OK, sent
    except TimeoutException:
        return 1           
    except StaleElementReferenceException:
        return 1
    except:
        return 1

def hide_header_and_messenger():    
    hide_header = wait.until(EC.presence_of_element_located((By.XPATH, '//header[@id="global-nav"]')))
    driver.execute_script("arguments[0].style.display = 'none';", hide_header)
    
    hide_top_menu = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'scaffold-layout-toolbar')))
    driver.execute_script("arguments[0].style.display = 'none';", hide_top_menu)
    
    hide_main_messenger = wait.until(EC.presence_of_element_located((By.XPATH, '//aside[@id="msg-overlay"]')))
    driver.execute_script("arguments[0].style.display = 'none';", hide_main_messenger)

def find_connect_buttons_and_people_names_and_perform_connect():
    global weekly_counter
    hide_header_and_messenger()
    scroll_to_bottom()
    time.sleep(1)
    connect_buttons = driver.find_elements(By.XPATH, '//button//span[contains(., "Connect")]')
    for connect_button in connect_buttons:
        person = connect_button.find_element(By.XPATH, './/ancestor::div[@class="entity-result__item"]')
        person_name = person.find_element(By.XPATH, './/span[@aria-hidden="true"]').get_attribute('innerHTML').strip("\n <!---->")
        action.move_to_element(connect_button).perform()
        time.sleep(1)
        driver.execute_script("arguments[0].click();", connect_button)
        time.sleep(1)
        try:
            got_it_button = driver.find_element(By.XPATH, '//button//span[contains(., "Got it")]')
            driver.execute_script("arguments[0].click();", got_it_button)
        except:
            pass
             
        if (weekly_counter<weekly_limit and connect(person_name) == 0): 
            weekly_counter +=1
            with open('linkedin-weekly-counter.txt', 'w') as a:
                a.writelines(str(weekly_counter))
            time.sleep(randint(1, 10)) # to reduce LinkedIn automation detection
        elif(weekly_counter>=weekly_limit): # to reduce LinkedIn automation detection
            os.system("cls") #clear screen from unnecessary logs since the operation has completed successfully
            print("You've reached Your weekly limit of "+ str(weekly_limit) +" connection requests. Stop before LinkedIn blocks You! \n \nSincerely Yours, \nNAKIGOE.ORG\n")
            driver.close()
            driver.quit()
                
def main():
    check_cookies_and_login()
    
    action.click(wait.until(EC.element_to_be_clickable((By.XPATH, '//section[@class="artdeco-card ember-view pv-top-card"]//a[@class="ember-view"]')))).perform()
    time.sleep(15)
    hide_header_and_messenger()
    while True:
        try:
            scroll_to_bottom()
            time.sleep(5)
            test_results_presence = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="entity-result__item"]')))
        except TimeoutException:
            break
        except StaleElementReferenceException:
            break
        if test_results_presence:
            #insert open «Follow» page function call here (if you write it)
                     
            #direct connect with the person's name included:
            find_connect_buttons_and_people_names_and_perform_connect()
        try:
            scroll_to_bottom()
            next_page_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Next"]')))
            action.move_to_element(next_page_button).perform()
            time.sleep(0.5)
            action.click(next_page_button).perform()
        except TimeoutException:
            break
        except StaleElementReferenceException:
            break

    # Close the only tab, will also close the browser.
    driver.close()
    driver.quit()
main()