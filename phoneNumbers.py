import requests
from bs4 import BeautifulSoup
import re
import numpy as np


#pages is the num of pages deep we want to search for numbers

def scrape(pages):
    numbers = []

    for i in range(1,pages+1):
        url = "https://britishnumbers.com/uk-mobile-numbers/?sort=priceasc&page=" + str(i)
        html_content = requests.get(url).text

        soup = BeautifulSoup(html_content, "html.parser")
        scraper = soup.find_all("h4", attrs={'class': 'card-title'})    #where the numbers are stored


        data = [i.get_text() for i in scraper]  #get the actual text within the html we have located
        data = [i.strip() for i in data]    #clean data

        for i in data:
            numbers.append(i)
        
    return numbers


#check for 4 consecutive numbers, can be extended to however many you want.
def consecNum(num):
    for i in range(len(num) - 3):
        if num[i] == num[i+1] and num[i+1] == num[i+2] and num[i+2] == num[i+3]:
            return True
    return False



#Here we scrape the first 10 pages of numbers
scraped_numbers = scrape(10)

for i in scraped_numbers:
    if consecNum(i):
        print(i)