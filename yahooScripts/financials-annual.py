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
options.binary_location = path1+"\\yahooScripts\\GoogleChromePortable\\App\\Chrome-bin\\chrome.exe"

driver = webdriver.Chrome(executable_path=chromepath, chrome_options=options)
arg1 = sys.argv[2]
arg2 = arg1.split("-annual",1)[0]
with open(path1+"\\settings\\setting.txt") as json_file:
    
		data = json.load(json_file) 
		Yahoo_output_path = (data['Yahoo_output_path'])
for w in range(0,len(code)):
	link = "https://finance.yahoo.com/quote/"+code[w]+"/"+arg2
	links.append(link)
	print("inside for loop")
	
def func(link):
	ts = time.strftime('%Y-%m-%d %H-%M-%S', time.gmtime())
	print("inside function")
	url = link
	
	driver.get(url)
	print("driver got url")
	time.sleep(3)
	mylist = []
	mynumbers = []
	header = []
	soup = BeautifulSoup(driver.page_source,"html.parser")
	print("bs got the site")
	requests.packages.urllib3.disable_warnings()



	#this is for row beginning for composite

	divparent = soup.find_all('div', attrs = {'class':'D(tbhg)'})
	div1 = divparent[0].findAll('span')
	for head in range(0,len(div1)):
		header.append(div1[head].text)
		
	header.insert(0,"Universal Site Symbol")
	header.insert(1,"Site Symbol")
	header.insert(2,"Timestamp")
	
	fname = Yahoo_output_path
	if not os.path.exists(fname):
		os.makedirs(fname)
	opFile = fname+"\\"+code[i]+"_"+"Yahoo"+"_"+sys.argv[2]+"_"+ts+".csv"
	myFile = open(opFile, 'w',newline = '')
	with myFile:
		writer = csv.writer(myFile)
		writer.writerows([header])
	#------------------------------------------------------------------------
	divparent = soup.find_all('div', attrs = {'class':'D(tbrg)'})
	div = divparent[0].find_all('span', attrs = {'class':'Va(m)'})
	for side in range(0,len(div)):
		mylist.append(div[side].text)
	#------------------------------------------------------------------------
		
	divparent = soup.find_all('div', attrs = {'class':'D(tbrg)'})
	div = divparent[0].find_all('div', attrs = {'data-test':'fin-col'})
	for num in range(0,len(div)):
		mynumbers.append(div[num].text)

	composite_list = [mynumbers[x:x+5] for x in range(0, len(mynumbers),5)]	

	for k in range(0,len(composite_list)):
			composite_list[k].insert(0,code[i])
			composite_list[k].insert(1,code[i])
			composite_list[k].insert(2,time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime()))
			composite_list[k].insert(3,mylist[k])
			
	fname = Yahoo_output_path
	if not os.path.exists(fname):
		os.makedirs(fname)
	opFile = fname+"\\"+code[i]+"_"+"Yahoo"+"_"+sys.argv[2]+"_"+ts+".csv"
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