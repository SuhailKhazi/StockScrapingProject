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
options.binary_location = path1+"\\reutersScripts\\GoogleChromePortable\\App\\Chrome-bin\\chrome.exe"

driver = webdriver.Chrome(executable_path=chromepath, options=options)

with open(path1+"\\settings\\setting.txt") as json_file:
    
		data = json.load(json_file) 
		Reuters_output_path = (data['Reuters_output_path'])

for w in range(0,len(code)):
    link = "https://www.reuters.com/companies/"+code[w]+"/"+sys.argv[2]
    links.append(link)
	
def func(link):
	ts = time.strftime('%Y-%m-%d %H-%M-%S', time.gmtime())
	fname = Reuters_output_path
	if not os.path.exists(fname):
		os.makedirs(fname)
	opFile = fname+"\\"+code[i]+"_"+"Reuters"+"_"+sys.argv[2]+"_"+ts+".csv"
	myFile = open(opFile, 'w',newline = '',encoding='utf-8')
	with myFile:
		writer = csv.writer(myFile)
			
		writer.writerows([["Universal site symbol","Site Symbol","TimeStamp","Label", "Value"]])
	print("inside function")
	url = link
	
	driver.get(url)
	print("driver got url")

	#mylist = []
	header = []
	
	#--------------------------------------------------------------------------------

	soup = BeautifulSoup(driver.page_source,"html.parser")

	print("bs got the site")

	requests.packages.urllib3.disable_warnings()
	
	try:
		divparent = soup.find_all('div', attrs={'class':'TwoColumnsLayout-body-86gsE CompanyQuotePage-body-container-19ttA'})
		print("found first div")
	except:
		print("no table div")
		pass #(this must be return later)


	try:
		divparent1 = divparent[0].find_all('div', attrs = {'class':'TwoColumnsLayout-left-column-CYquM'})
	except:
		print("no table div 1")
		return

	try:
		divparent2 = divparent1[0].find_all('div', attrs = {'class':'KeyMetrics-container-3QO5T'})
	except:
		print("no div2")
		return

	try:
		divparent3 = divparent2[0].find_all('div', attrs = {'class':'KeyMetrics-table-container-3wVZN'})
	except:
		print("no div3")
		return
	
	for c in range(0,len(divparent3)):
		mylist = []
		my_table = divparent3[c].find_all('table')
		heading = divparent3[c].find('h3')
		rows = my_table[0].findChildren(['tr'])
		for row in rows:
			for data in row:
				if data.text!="":
						mylist.append(data.text)
						
		composite_list = [mylist[x:x+2] for x in range(0, len(mylist),2)]
		for k in range(0,len(composite_list)):
			composite_list[k].insert(0,code[i])
			composite_list[k].insert(1,code[i])
			composite_list[k].insert(2,time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime()))
			composite_list[k].insert(3,heading.text)
		
		fname = Reuters_output_path
		if not os.path.exists(fname):
			os.makedirs(fname)
		opFile = fname+"\\"+code[i]+"_"+"Reuters"+"_"+sys.argv[2]+"_"+ts+".csv"
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