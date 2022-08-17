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
    link = "https://www.zacks.com/stock/research/"+code[w]+"/"+sys.argv[2]
    links.append(link)
	
def func(link):
	ts = time.strftime('%Y-%m-%d %H-%M-%S', time.gmtime())
	print("inside function")
	url = link
	
	driver.get(url)
	print("driver got url")

	
	
	#--------------------------------------------------------------------------------

	soup = BeautifulSoup(driver.page_source,"html.parser")

	print("bs got the site")

	requests.packages.urllib3.disable_warnings()
	
	mylist = []
	header = []
	
	try:
		divparent = soup.find_all('section', attrs={'id':'financials'})
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
	header.insert(3,"financials")
	
	fname = Zacks_output_path
	if not os.path.exists(fname):
		os.makedirs(fname)
	opFile = fname+"\\"+code[i]+"_"+"Zacks"+"_"+sys.argv[2]+"_"+ts+".csv"
	myFile = open(opFile, 'w',newline = '')
	with myFile:
		writer = csv.writer(myFile)
		writer.writerows([header])
		
		
	composite_list = [mylist[x:x+3] for x in range(0, len(mylist),3)]
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
			
	#------------------------------------------------------------
	mylist = []
	header = []
	
	try:
		divparent = soup.find_all('section', attrs={'id':'growth_rates'})
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
	header.insert(3,"Growth Rates")
	
	fname = Zacks_output_path
	if not os.path.exists(fname):
		os.makedirs(fname)
	opFile = fname+"\\"+code[i]+"_"+"Zacks"+"_"+sys.argv[2]+"_"+ts+".csv"
	myFile = open(opFile, 'a',newline = '')
	with myFile:
		writer = csv.writer(myFile)
		writer.writerows([header])
		
		
	composite_list = [mylist[x:x+4] for x in range(0, len(mylist),4)]
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
			
	#------------------------------------------------------------
	mylist = []
	header = []
	
	try:
		divparent = soup.find_all('section', attrs={'id':'industry_report'})
	except:
		print("no table div")
		pass #(this must be return later)

	try:
		paragraph = divparent[0].find_all('p')
	except:
		print("no table div here!")
		pass
	#this is paragraph 0	
	head = paragraph[0].find_all('a')
	header.append(head[0].text)
	data = paragraph[0].find_all('strong')
	mylist.append(data[0].text)
	# this is paragraph 1
	data1 = paragraph[1].find_all('a')
	mylist.append(data1[1].text)
	head1 = paragraph[1].text
	head1 = head1.replace(data1[1].text,"")
	header.append(head1)
	#this is paragraph 2
	data1 = paragraph[2].find_all('a')
	mylist.append(data1[0].text)
	head1 = paragraph[2].text
	head1 = head1.replace(data1[0].text,"")
	header.append(head1)
	
	header.insert(0,"Universal site symbol")
	header.insert(1,"Site symbol")
	header.insert(2,"Time stamp")
	
	mylist.insert(0,code[i])
	mylist.insert(1,code[i])
	mylist.insert(2,time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime()))
	
	
	fname = Zacks_output_path
	if not os.path.exists(fname):
		os.makedirs(fname)
	opFile = fname+"\\"+code[i]+"_"+"Zacks"+"_"+sys.argv[2]+"_"+ts+".csv"
	myFile = open(opFile, 'a',newline = '',encoding='utf-8')
	with myFile:
			writer = csv.writer(myFile)
			
			writer.writerows([header])
			writer.writerows([mylist])
			
	fname = Zacks_output_path
	if not os.path.exists(fname):
		os.makedirs(fname)
	opFile = fname+"\\"+code[i]+"_"+"Zacks"+"_"+sys.argv[2]+"_"+ts+".csv"
	myFile = open(opFile, 'a',newline = '',encoding='utf-8')
	with myFile:
			writer = csv.writer(myFile)
			writer.writerows([""])
			
	#------------------------------------------------------------
	mylist = []
	header = []
	
	try:
		divparent = soup.find_all('section', attrs={'id':'recommendations_estimates'})
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
	header.insert(3,"Recommendations And Estimates")
	
	fname = Zacks_output_path
	if not os.path.exists(fname):
		os.makedirs(fname)
	opFile = fname+"\\"+code[i]+"_"+"Zacks"+"_"+sys.argv[2]+"_"+ts+".csv"
	myFile = open(opFile, 'a',newline = '')
	with myFile:
		writer = csv.writer(myFile)
		writer.writerows([header])
		
		
	composite_list = [mylist[x:x+4] for x in range(0, len(mylist),4)]
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
			
	#------------------------------------------------------------
	
for i in range(0,len(links)):
	print("doing for ",i)		
	url = links[i]
	func(url)
	print("sleeping for 5 seconds")
	time.sleep(5)
print("done ^_^")