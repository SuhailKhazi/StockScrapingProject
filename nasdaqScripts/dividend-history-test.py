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
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
links = []
code = [sys.argv[1]]
def remove_values_from_list(the_list, val):
   return [value for value in the_list if value != val]
#--------------------------------------------------------------------------------
chromepath = r"C:\Users\hp\Desktop\webScrape\chromedriver\chromedriver.exe"
options = Options()
# options.add_argument("--headless")
options.add_argument('--disable-gpu')
options.add_argument('--log-level=3')
options.add_argument('--lang=en')

driver = webdriver.Chrome(executable_path=chromepath, chrome_options=options)

for w in range(0,len(code)):
	link = "https://new.nasdaq.com/market-activity/stocks/"+code[w]+"/"+sys.argv[2]
	links.append(link)
	print("inside for loop")
	
def func(link):
	
	print("inside function")
	url = link
	
	driver.get(url)
	print("driver got url")
	
	soup = BeautifulSoup(driver.page_source,"html.parser")

	print("bs got the site")

	requests.packages.urllib3.disable_warnings()
	
	mylist = []
	header = []
	
	try:
		listdiv = soup.find_all('ul', attrs={'class':'dividend-history__summary'})
	except:
		print("no list")
		return
		
	
	for item in listdiv[0].findAll('li'):
		for data in item.find_all('span', attrs = {'class':'dividend-history__summary-item__label'}):
			header.append(data.text)
			
	for item in listdiv[0].findAll('li'):
		for data in item.find_all('span', attrs = {'class':'dividend-history__summary-item__value'}):
			mylist.append(data.text)
			
	header.insert(0,"Universal Site Symbol")
	header.insert(1,"Site Symbol")
	header.insert(2,"Timestamp")
	fname = r"C:\Users\hp\Desktop\scraping project\output files\Nasdaq\\"+sys.argv[2]
	if not os.path.exists(fname):
		os.makedirs(fname)
	opFile = fname+"\\"+code[i]+".csv"
	myFile = open(opFile, 'w',newline = '')
	with myFile:
		writer = csv.writer(myFile)
		writer.writerows([header])
	
	mylist.insert(0,code[i])
	mylist.insert(1,code[i])
	mylist.insert(2,time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime()))
	
	fname = r"C:\Users\hp\Desktop\scraping project\output files\Nasdaq\\"+sys.argv[2]
	if not os.path.exists(fname):
		os.makedirs(fname)
	opFile = fname+"\\"+code[i]+".csv"
	myFile = open(opFile, 'a',newline = '')
	with myFile:
		writer = csv.writer(myFile)
		writer.writerows([mylist])
		
	#--------------------------------------------------------------------------------
	
	mylist = []
	header = []
	try:
		divparent = soup.find_all('div', attrs={'class':'dividend-history__table-container'})
	except:
		print("no div here")
	try:
		my_table = divparent[0].find('table')
	except:
		print("no table div here!")
		return
	try:
		for row in my_table.findAll('tr'):
			for data in row.findAll('th'):
				mylist.append(data.text)
			for data in row.findAll('td'):
				mylist.append(data.text)
					
	except:
		print("no table here!")
		return
		
		
	header = mylist[:6]
	header.insert(0,"Universal Site Symbol")
	header.insert(1,"Site Symbol")
	header.insert(2,"Timestamp")
	fname = r"C:\Users\hp\Desktop\scraping project\output files\Nasdaq\\"+sys.argv[2]
	if not os.path.exists(fname):
		os.makedirs(fname)
	opFile = fname+"\\"+code[i]+".csv"
	myFile = open(opFile, 'a',newline = '')
	with myFile:
		writer = csv.writer(myFile)
		writer.writerows([header])
		
		
	mylist = mylist[6:]
	composite_list = [mylist[x:x+6] for x in range(0, len(mylist),6)]
	
	for k in range(0,len(composite_list)):
		composite_list[k].insert(0,code[i])
		composite_list[k].insert(1,code[i])
		composite_list[k].insert(2,time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime()))
		
	fname = r"C:\Users\hp\Desktop\scraping project\output files\Nasdaq\\"+sys.argv[2]
	if not os.path.exists(fname):
		os.makedirs(fname)
	opFile = fname+"\\"+code[i]+".csv"
	myFile = open(opFile, 'a',newline = '',encoding='utf-8')
	with myFile:
			writer = csv.writer(myFile)
			for z in range(0,len(composite_list)):
				writer.writerows([composite_list[z]])
				
				
				
for i in range(0,len(links)):
	print("doing for ",i)		
	url = links[i]
	func(url)
	print("sleeping for 5 seconds")
	time.sleep(5)		
print("done ^_^")