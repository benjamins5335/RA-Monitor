import requests
from bs4 import BeautifulSoup as bs
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

# atc link: type=addBasket&ticketId=479660&shippingTypeId=8&quantity=1&eventId=1495307&currencyId=1&referrer=https%3A%2F%2Fra.co%2Fevents%2F1495307&isEmbedTickets=true
webhook = "https://discordapp.com/api/webhooks/646488319148163073/asoW2-tyA3JzAvdOgGRlE8hfnr0_p-AKZ0_PpyVhC9s1JRQtlAAeQWb7GYKsBbq_4VCv"
delay = 10000

def run(eventCode):
    url = "https://ra.co/events/" + eventCode
    
    print("Using Home IP")
    browser = webdriver.Chrome("drivers/chromedriver")
    # browser = webdriver.Chrome("../chromedriver")
    
    browser.get(url)
    

    while True:
        try:
            
            frame = WebDriverWait(browser, delay/1000).until(
            
            EC.frame_to_be_available_and_switch_to_it((By.ID, '#tickets-iframe-m')))
                
            buyButton = WebDriverWait(browser, delay/1000).until(
                EC.element_to_be_clickable((By.CLASS_NAME, 'onsale')))
            
            print("&&&&&&&&&&& IN STOCK &&&&&&&&&&&")
            
            requests.post(webhook, json={
                "username": "Tickets Available",
                "embeds": [
                    {
                        "color": "65535",
                        "fields": [
                            {
                                "name": "Link",
                                "value": url
                            }
                        ]
                    }
                ]
            })
            
            time.sleep(20)
            
        except Exception:
            print("not in stock. retrying...")
            browser.refresh()

    



if __name__ == "__main__":
    print("Sparks: 1492035")
    print("Hector Oaks: 1386829")
    print("Ben UFO: 1495342")
    eventCode = input("Enter event code: ")
    # eventCode = "1492035"
    run(eventCode)