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
options.binary_location = path1+"\\zacksScripts\\GoogleChromePortable\\App\\Chrome-bin\\chrome.exe"
driver = webdriver.Chrome(executable_path=chromepath, chrome_options=options)
with open(path1+"\\settings\\setting.txt") as json_file:
    
		data = json.load(json_file) 
		Zacks_output_path = (data['Zacks_output_path'])

for w in range(0,len(code)):
    link = "https://www.zacks.com/stock/quote/"+code[w]+"/"+sys.argv[2]
    links.append(link)
    
		
		
		
def func(link):
	ts = time.strftime('%Y-%m-%d %H-%M-%S', time.gmtime())
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
		divparent = soup.find_all('section', attrs={'id':'agreement_estimate'})
	except:
		print("no table div")
		return
		
	try:
		my_table = divparent[0].find_all('table')
	except:
			print("no table div here!")
			return	
	
	for record in my_table[0].findAll('tr'):
		for data in record.findAll('th'):
			if data.text!="":
				header.append(data.text)
			

		

	for record in my_table[0].findAll('tr'):
			for data in record.findAll('td'):
				mylist.append(data.text)
				
				
	header.insert(0,"Universal site symbol")
	header.insert(1,"Site symbol")
	header.insert(2,"Time stamp")
	header.insert(3,"Data name")
	
	fname = Zacks_output_path
	if not os.path.exists(fname):
		os.makedirs(fname)
	opFile = fname+"\\"+code[i]+"_"+"Zacks"+"_"+sys.argv[2]+"_"+ts+".csv"
	myFile = open(opFile, 'w',newline = '')
	with myFile:
		writer = csv.writer(myFile)
		writer.writerows([header])
		
		
	composite_list = [mylist[x:x+5] for x in range(0, len(mylist),5)]
	for k in range(0,len(composite_list)):
		composite_list[k].insert(0,code[i])
		composite_list[k].insert(1,code[i])
		composite_list[k].insert(2,time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime()))
		
		
	fname = Zacks_output_path
	if not os.path.exists(fname):
		os.makedirs(fname)
	opFile = fname+"\\"+code[i]+"_"+"Zacks"+"_"+sys.argv[2]+"_"+ts+".csv"
	myFile = open(opFile, 'a',newline = '',encoding='utf-8')
	with myFile:
			writer = csv.writer(myFile)
			for z in range(0,len(composite_list)):
				writer.writerows([composite_list[z]])
				
				
	fname = Zacks_output_path
	if not os.path.exists(fname):
		os.makedirs(fname)
	opFile = fname+"\\"+code[i]+"_"+"Zacks"+"_"+sys.argv[2]+"_"+ts+".csv"
	myFile = open(opFile, 'a',newline = '',encoding='utf-8')
	with myFile:
			writer = csv.writer(myFile)
			writer.writerows([""])
			
	#---------------------------------------------------------------
	
	mylist = []
	header = []
	
	try:
		divparent = soup.find_all('section', attrs={'id':'magnitude_estimate'})
	except:
		print("no table div")
		return
		
	try:
		my_table = divparent[0].find_all('table')
	except:
			print("no table div here!")
			return	
	
	for record in my_table[0].findAll('tr'):
		for data in record.findAll('th'):
			if data.text!="":
				header.append(data.text)
			

		

	for record in my_table[0].findAll('tr'):
			for data in record.findAll('td'):
				mylist.append(data.text)
				
				
	header.insert(0,"Universal site symbol")
	header.insert(1,"Site symbol")
	header.insert(2,"Time stamp")
	header.insert(3,"Data name")
	
	fname = Zacks_output_path
	if not os.path.exists(fname):
		os.makedirs(fname)
	opFile = fname+"\\"+code[i]+"_"+"Zacks"+"_"+sys.argv[2]+"_"+ts+".csv"
	myFile = open(opFile, 'a',newline = '')
	with myFile:
		writer = csv.writer(myFile)
		writer.writerows([header])
		
		
	composite_list = [mylist[x:x+5] for x in range(0, len(mylist),5)]
	for k in range(0,len(composite_list)):
		composite_list[k].insert(0,code[i])
		composite_list[k].insert(1,code[i])
		composite_list[k].insert(2,time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime()))
		
		
	fname = Zacks_output_path
	if not os.path.exists(fname):
		os.makedirs(fname)
	opFile = fname+"\\"+code[i]+"_"+"Zacks"+"_"+sys.argv[2]+"_"+ts+".csv"
	myFile = open(opFile, 'a',newline = '',encoding='utf-8')
	with myFile:
			writer = csv.writer(myFile)
			for z in range(0,len(composite_list)):
				writer.writerows([composite_list[z]])
				
	fname = Zacks_output_path
	if not os.path.exists(fname):
		os.makedirs(fname)
	opFile = fname+"\\"+code[i]+"_"+"Zacks"+"_"+sys.argv[2]+"_"+ts+".csv"
	myFile = open(opFile, 'a',newline = '',encoding='utf-8')
	with myFile:
			writer = csv.writer(myFile)
			writer.writerows([""])
			
	#---------------------------------------------------------------
	
	mylist = []
	header = []
	
	try:
		divparent = soup.find_all('section', attrs={'id':'detailed_earnings_estimates'})
	except:
		print("no table div")
		return
		
	try:
		my_table = divparent[1].find_all('table')
	except:
			print("no table div here!")
			return	
	
	for record in my_table[0].findAll('tr'):
		for data in record.findAll('th'):
			if data.text!="":
				header.append(data.text)
			

		

	for record in my_table[0].findAll('tr'):
			for data in record.findAll('td'):
				mylist.append(data.text)
				
				
	header.insert(0,"Universal site symbol")
	header.insert(1,"Site symbol")
	header.insert(2,"Time stamp")
	header.insert(3,"Data name")
	
	fname = Zacks_output_path
	if not os.path.exists(fname):
		os.makedirs(fname)
	opFile = fname+"\\"+code[i]+"_"+"Zacks"+"_"+sys.argv[2]+"_"+ts+".csv"
	myFile = open(opFile, 'a',newline = '')
	with myFile:
		writer = csv.writer(myFile)
		writer.writerows([header])
		
		
	composite_list = [mylist[x:x+5] for x in range(0, len(mylist),5)]
	for k in range(0,len(composite_list)):
		composite_list[k].insert(0,code[i])
		composite_list[k].insert(1,code[i])
		composite_list[k].insert(2,time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime()))
		
		
	fname = Zacks_output_path
	if not os.path.exists(fname):
		os.makedirs(fname)
	opFile = fname+"\\"+code[i]+"_"+"Zacks"+"_"+sys.argv[2]+"_"+ts+".csv"
	myFile = open(opFile, 'a',newline = '',encoding='utf-8')
	with myFile:
			writer = csv.writer(myFile)
			for z in range(0,len(composite_list)):
				writer.writerows([composite_list[z]])
				
	fname = Zacks_output_path
	if not os.path.exists(fname):
		os.makedirs(fname)
	opFile = fname+"\\"+code[i]+"_"+"Zacks"+"_"+sys.argv[2]+"_"+ts+".csv"
	myFile = open(opFile, 'a',newline = '',encoding='utf-8')
	with myFile:
			writer = csv.writer(myFile)
			writer.writerows([""])
			
	#---------------------------------------------------------------
	
	mylist = []
	header = []
	
	try:
		divparent = soup.find_all('section', attrs={'id':'detailed_earnings_estimates'})
	except:
		print("no table div")
		return
		
	try:
		my_table = divparent[0].find_all('table')
	except:
			print("no table div here!")
			return	
	
	for record in my_table[0].findAll('tr'):
		for data in record.findAll('th'):
			if data.text!="":
				header.append(data.text)
			

		

	for record in my_table[0].findAll('tr'):
			for data in record.findAll('td'):
				mylist.append(data.text)
				
				
	header.insert(0,"Universal site symbol")
	header.insert(1,"Site symbol")
	header.insert(2,"Time stamp")
	header.insert(3,"Data name")
	
	fname = Zacks_output_path
	if not os.path.exists(fname):
		os.makedirs(fname)
	opFile = fname+"\\"+code[i]+"_"+"Zacks"+"_"+sys.argv[2]+"_"+ts+".csv"
	myFile = open(opFile, 'a',newline = '')
	with myFile:
		writer = csv.writer(myFile)
		writer.writerows([header])
		
		
	composite_list = [mylist[x:x+5] for x in range(0, len(mylist),5)]
	for k in range(0,len(composite_list)):
		composite_list[k].insert(0,code[i])
		composite_list[k].insert(1,code[i])
		composite_list[k].insert(2,time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime()))
		
		
	fname = Zacks_output_path
	if not os.path.exists(fname):
		os.makedirs(fname)
	opFile = fname+"\\"+code[i]+"_"+"Zacks"+"_"+sys.argv[2]+"_"+ts+".csv"
	myFile = open(opFile, 'a',newline = '',encoding='utf-8')
	with myFile:
			writer = csv.writer(myFile)
			for z in range(0,len(composite_list)):
				writer.writerows([composite_list[z]])
				
				
	fname = Zacks_output_path
	if not os.path.exists(fname):
		os.makedirs(fname)
	opFile = fname+"\\"+code[i]+"_"+"Zacks"+"_"+sys.argv[2]+"_"+ts+".csv"
	myFile = open(opFile, 'a',newline = '',encoding='utf-8')
	with myFile:
			writer = csv.writer(myFile)
			writer.writerows([""])
			
	#---------------------------------------------------------------
	
	mylist = []
	header = []
	
	try:
		divparent = soup.find_all('section', attrs={'id':'quote_upside'})
	except:
		print("no table div")
		return
		
	try:
		my_table = divparent[0].find_all('table')
	except:
			print("no table div here!")
			return	
	
	for record in my_table[0].findAll('tr'):
		for data in record.findAll('th'):
			if data.text!="":
				header.append(data.text)
			

		

	for record in my_table[0].findAll('tr'):
			for data in record.findAll('td'):
				mylist.append(data.text)
				
				
	header.insert(0,"Universal site symbol")
	header.insert(1,"Site symbol")
	header.insert(2,"Time stamp")
	header.insert(3,"Data name")
	
	fname = Zacks_output_path
	if not os.path.exists(fname):
		os.makedirs(fname)
	opFile = fname+"\\"+code[i]+"_"+"Zacks"+"_"+sys.argv[2]+"_"+ts+".csv"
	myFile = open(opFile, 'a',newline = '')
	with myFile:
		writer = csv.writer(myFile)
		writer.writerows([header])
		
		
	composite_list = [mylist[x:x+5] for x in range(0, len(mylist),5)]
	for k in range(0,len(composite_list)):
		composite_list[k].insert(0,code[i])
		composite_list[k].insert(1,code[i])
		composite_list[k].insert(2,time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime()))
		
		
	fname = Zacks_output_path
	if not os.path.exists(fname):
		os.makedirs(fname)
	opFile = fname+"\\"+code[i]+"_"+"Zacks"+"_"+sys.argv[2]+"_"+ts+".csv"
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