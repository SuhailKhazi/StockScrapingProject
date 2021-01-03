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
arg1 = sys.argv[2]
arg2 = arg1.split("-quarter",1)[0]
with open(path1+"\\settings\\setting.txt") as json_file:
    
		data = json.load(json_file) 
		TD_output_path = (data['TD_output_path'])
for w in range(0,len(code)):
	link = "https://research.tdameritrade.com/grid/public/research/stocks/fundamentals/statement/"+arg2+"?symbol="+code[w]
	links.append(link)
	print("inside for loop")
	
def func(link):
	ts = time.strftime('%Y-%m-%d %H-%M-%S', time.gmtime())
	fname = TD_output_path
	if not os.path.exists(fname):
		os.makedirs(fname)
	opFile = fname+"\\"+code[i]+"_"+"TD"+"_"+sys.argv[2]+"_"+ts+".csv"
	myFile = open(opFile, 'w',newline = '')
	with myFile:
		writer = csv.writer(myFile)
		writer.writerows([" "])
	
	print("inside function")
	url = link
	
	driver.get(url)
	driver.get("https://research.tdameritrade.com/grid/public/research/stocks/fundamentals/statement/incomestatement?period=Q")
	
	print("driver got url")
	soup = BeautifulSoup(driver.page_source,"html.parser")

	print("bs got the site")

	requests.packages.urllib3.disable_warnings()
	try:
		divparent = soup.find_all('div', attrs = {'class':'row contain data-view'})
	except:
		print("no table div here!")
		return
		
	try:
		div = divparent[0].find_all('div', attrs = {'class':'col-xs-12'})
	except:
		print("no table div here!")
		return
	
	
	for n in range(0,len(div)):
		mylist = []
		header = []
		try:
			my_table = div[n].findAll('table')
		except:
			print("no table div here!")
			return
		try:
			label = div[n].find('label')
		except:
			print("no label here!")
			return
			
			
		for row in my_table[0].findAll('tr'):
			for data in row.findAll('th'):
				if data.text!="":
					mylist.append(data.text)
			for data in row.findAll('td'):
				if data.text!="":
					mylist.append(data.text)
				
		
				
		header = mylist[:4]
		header.insert(0,"Universal Site Symbol")
		header.insert(1,"Site Symbol")
		header.insert(2,"Timestamp")
		header.insert(3,label.text)
		fname = TD_output_path
		if not os.path.exists(fname):
			os.makedirs(fname)
		opFile = fname+"\\"+code[i]+"_"+"TD"+"_"+sys.argv[2]+"_"+ts+".csv"
		myFile = open(opFile, 'a',newline = '')
		with myFile:
			writer = csv.writer(myFile)
			writer.writerows([header])
			
		mylist = mylist[4:]
		composite_list = [mylist[x:x+5] for x in range(0, len(mylist),5)]
		
		for k in range(0,len(composite_list)):
			composite_list[k].insert(0,code[i])
			composite_list[k].insert(1,code[i])
			composite_list[k].insert(2,time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime()))
			
		fname = TD_output_path
		if not os.path.exists(fname):
			os.makedirs(fname)
		opFile = fname+"\\"+code[i]+"_"+"TD"+"_"+sys.argv[2]+"_"+ts+".csv"
		myFile = open(opFile, 'a',newline = '',encoding='utf-8')
		with myFile:
				writer = csv.writer(myFile)
				for z in range(0,len(composite_list)):
					writer.writerows([composite_list[z]])
					
		
		fname = TD_output_path
		if not os.path.exists(fname):
			os.makedirs(fname)
		opFile = fname+"\\"+code[i]+"_"+"TD"+"_"+sys.argv[2]+"_"+ts+".csv"
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