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
path1 = sys.argv[3]
def remove_values_from_list(the_list, val):
   return [value for value in the_list if value != val]
#--------------------------------------------------------------------------------
chromepath = path1+"\\settings\\chromedriver\\chromedriver.exe"
options = Options()
options.add_argument("--headless")
options.add_argument('--disable-gpu')
options.add_argument('--log-level=3')
options.add_argument('--lang=en')
options.binary_location = path1+"\\tdScripts\\GoogleChromePortable\\App\\Chrome-bin\\chrome.exe"

driver = webdriver.Chrome(executable_path=chromepath, chrome_options=options)
with open(path1+"\\settings\\setting.txt") as json_file:
    
		data = json.load(json_file) 
		TD_output_path = (data['TD_output_path'])
for w in range(0,len(code)):
	link = "https://research.tdameritrade.com/grid/public/research/stocks/"+sys.argv[2]+"?symbol="+code[w]
	links.append(link)
	print("inside for loop")
	
def func(link):
	ts = time.strftime('%Y-%m-%d %H-%M-%S', time.gmtime())
	
	print("inside function")
	url = link
	
	driver.get(url)
	
	print("driver got url")
	soup = BeautifulSoup(driver.page_source,"html.parser")

	print("bs got the site")

	requests.packages.urllib3.disable_warnings()
	
	try:
		divparent = soup.find_all('div', attrs = {'class':'module-header'})
	except:
		print("no div!")
		return
	
	try:
		div = divparent[0].find('h2')
	except:
		print("no div")
		return
	industryname = div.text.split("the ")[1]

	mylist = []
	header = []
	industrycode = []
	
	header.append("Universal Site Symbol")
	header.append("Site Symbol")
	header.append("Timestamp")
	header.append("Industry Name")
	header.append("Industry Peers")
	fname = TD_output_path
	if not os.path.exists(fname):
		os.makedirs(fname)
	opFile = fname+"\\"+code[i]+"_"+"TD"+"_"+sys.argv[2]+"_"+ts+".csv"
	myFile = open(opFile, 'w',newline = '')
	with myFile:
		writer = csv.writer(myFile)
		writer.writerows([header])
	
	
	mylist.append(code[i])
	mylist.append(code[i])
	mylist.append(time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime()))
	mylist.append(industryname)
	try:
		divparent = soup.find_all('table', attrs = {'class':'ui-table'})
	except:
		print("no table")
		return
	div1 = divparent[0].findAll('span')
	mylist.append(div1[0].text)
	
	fname = TD_output_path
	if not os.path.exists(fname):
		os.makedirs(fname)
	opFile = fname+"\\"+code[i]+"_"+"TD"+"_"+sys.argv[2]+"_"+ts+".csv"
	myFile = open(opFile, 'a',newline = '',encoding='utf-8')
	with myFile:
		writer = csv.writer(myFile)
		writer.writerows([mylist])
		mylist.pop()
		
	div = divparent[0].find('thead')
	data = div.findAll('a')
	for m in range(0,len(data)):
		mylist.append(data[m].text)
		fname = TD_output_path
		if not os.path.exists(fname):
			os.makedirs(fname)
		opFile = fname+"\\"+code[i]+"_"+"TD"+"_"+sys.argv[2]+"_"+ts+".csv"
		myFile = open(opFile, 'a',newline = '',encoding='utf-8')
		with myFile:
			writer = csv.writer(myFile)
			writer.writerows([mylist])
			mylist.pop()
			
			
for i in range(0,len(links)):
	print("doing for ",i)		
	url = links[i]
	func(url)
	print("sleeping for 5 seconds")
	time.sleep(5)		
print("done ^_^")