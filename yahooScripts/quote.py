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
options.add_argument("--headless")
options.add_argument('--disable-gpu')
options.add_argument('--log-level=3')
options.add_argument('--lang=en')
options.binary_location = path1+"\\yahooScripts\\GoogleChromePortable\\App\\Chrome-bin\\chrome.exe"

driver = webdriver.Chrome(executable_path=chromepath, chrome_options=options)
with open(path1+"\\settings\\setting.txt") as json_file:
    
		data = json.load(json_file) 
		Yahoo_output_path = (data['Yahoo_output_path'])

for w in range(0,len(code)):
	link = "https://finance.yahoo.com/quote/"+code[w]+"/"+sys.argv[2]
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
	
	
	
	divparent = soup.find_all('div', attrs={'id':'quote-summary'})
	
	try:
		my_table = divparent[0].findAll('table')
	except:
		print("no table div here!")
		return
	
	for t in range(0,len(my_table)):
		mylist = []
		header = []
		
		
		
		for row in my_table[t].findAll('tr'):
			for data in row.findAll('th'):
				mylist.append(data.text)
			for data in row.findAll('td'):
				mylist.append(data.text)

		
		header.append("Universal Site Symbol")
		header.append("Site Symbol")
		header.append("Timestamp")
		header.append("Data")
		header.append("Value")
		fname = Yahoo_output_path
		if not os.path.exists(fname):
			os.makedirs(fname)
		opFile = fname+"\\"+code[i]+"_"+"Yahoo"+"_"+sys.argv[2]+"_"+ts+".csv"
		myFile = open(opFile, 'w',newline = '')
		with myFile:
			writer = csv.writer(myFile)
			writer.writerows([header])
			
		#mylist = mylist[5:]
		composite_list = [mylist[x:x+2] for x in range(0, len(mylist),2)]
		
		for k in range(0,len(composite_list)):
			composite_list[k].insert(0,code[i])
			composite_list[k].insert(1,code[i])
			composite_list[k].insert(2,time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime()))
			
		fname = Yahoo_output_path
		if not os.path.exists(fname):
			os.makedirs(fname)
		opFile = fname+"\\"+code[i]+"_"+"Yahoo"+"_"+sys.argv[2]+"_"+ts+".csv"
		myFile = open(opFile, 'a',newline = '',encoding='utf-8')
		with myFile:
				writer = csv.writer(myFile)
				for z in range(0,len(composite_list)):
					writer.writerows([composite_list[z]])
					
		
		fname = Yahoo_output_path
		if not os.path.exists(fname):
			os.makedirs(fname)
		opFile = fname+"\\"+code[i]+"_"+"Yahoo"+"_"+sys.argv[2]+"_"+ts+".csv"
		myFile = open(opFile, 'a',newline = '')
		with myFile:
			writer = csv.writer(myFile)
			writer.writerows([" "])
				
for i in range(0,len(links)):
	print("doing for ",i)		
	url = links[i]
	func(url)
	print("sleeping for 5 seconds")
	time.sleep(5)		
print("done ^_^")