#UPDATED
import requests
from bs4 import BeautifulSoup
import csv
import sys
import os
import json
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
path1 = os.path.dirname(os.path.abspath(__file__))
from datetime import datetime

def remove_values_from_list(the_list, val):
   return [value for value in the_list if value != val]
   
path1 = "C:\\Users\\hp\\Desktop\\scrapingProject"   
chromepath = path1+"\\settings\\chromedriver\\chromedriver.exe"
geckodriver = "C:\\Users\\hp\\Downloads\\geckodriver-v0.26.0-win64\\geckodriver.exe"
options = Options()
options.add_argument("--headless")
options.add_argument('--disable-gpu')
options.add_argument('--log-level=3')
options.add_argument('--lang=en')
options.add_argument('--window-size=1300,1000')
driver = webdriver.Chrome(executable_path=chromepath, options=options)
# driver = webdriver.Firefox(executable_path = geckodriver, options=options)

url = 'https://www.nasdaq.com/market-activity/stocks/aapl/short-interest'
driver.get(url)

soup = BeautifulSoup(driver.page_source,"html.parser")

print("bs got the site")

requests.packages.urllib3.disable_warnings()

mylist = []
header = []

try:
	divparent = soup.find_all('div', attrs={'class':'short-interest__table-container'})
except:
	print("no list")
	pass
	
	
my_table = divparent[0].find_all('table')
print(my_table[0])