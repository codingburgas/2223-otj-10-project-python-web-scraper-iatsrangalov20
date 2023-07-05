import os
clear = lambda: os.system('cls')

import requests
import re
from bs4 import BeautifulSoup

def scrape_website():
    while True:
        category = input("What do you want to search for: ")

        if category == "processor":
            processor = input("Enter processor: ")

            URL = "https://desktop.bg/grigs-all"
            page = requests.get(URL)
            soup = BeautifulSoup(page.content, 'html.parser')

            pcs = soup.find_all(string=re.compile("\({}".format(processor)))
            prices = soup.body.find_all("span", class_="price")
            price = 0
            index = 1

            for pc in pcs:
                print(str(index)+ ". " + pc + " -", prices[price].text.strip())
                price+=1
                index+=1

            if input("Press Enter to search again...") == "":
                clear()
            else:
                break
                
        elif category == "headphones":
            headphones = input("Enter headphones brand: ")

            URL = "https://desktop.bg/promotions?utf8=%E2%9C%93&search%5Btype_in%5D%5B%5D=headphone&per_page=27&search%5Bs%5D=promo_asc"
            page = requests.get(URL)
            soup = BeautifulSoup(page.content, 'html.parser')

            headphones = soup.find_all(string=re.compile("^{}".format(headphones)))
            prices = soup.body.find_all("span", class_="price")
            price = 0
            
            sold_all = soup.find_all('li', class_="sold-count")
            sold = 0
            index = 1

            for h in headphones:
                print(str(index)+ ". " + h + " -", prices[price].text.strip(), "-", sold_all[sold].text.strip())
                index+=1
                sold+=1
                price+=1

            if input("Press Enter to search again...") == "":
                clear()
            else:
                break
                
scrape_website()