from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import requests
import time
import pandas as pd
from bs4 import BeautifulSoup
# import urllib.request as ur
import requests
import re
import json
from lxml import etree
from bs4 import Comment
import csv
import sys
import datetime
from datetime import timedelta
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains
path1 = "C:\\Users\\hp\\Desktop\\scrapingProject"
# with open(path1+"\\settings\\setting.txt") as json_file:
    
		# data = json.load(json_file) 
		# username = (data['watchlist_username'])
		# password = (data['watchlist_password'])
		# watchlist_download_path = (data['watchlist_download_path'])
		# view = (data['view'])



# options = Options()
# options.add_argument("--headless")
# options.add_argument("--window-size=1920x1080")
# options.add_argument("--disable-notifications")
# options.add_argument('--no-sandbox')
# options.add_argument('--log-level=3')

# options.add_argument('--disable-gpu')
# options.add_argument('--disable-software-rasterizer')

# driver = webdriver.Chrome(options=options, executable_path=r'C:\Users\hp\Desktop\scrapingProject\settings\chromedriver\chromedriver.exe')
# headerCount = 0

def func(start_date,stop_date,output_path):
	headerCount = 0
	# driver = webdriver.Chrome(options=options, executable_path=r'C:\Users\hp\Desktop\scrapingProject\settings\chromedriver\chromedriver.exe')
	# ts = time.strftime('%Y-%m-%d %H-%M-%S', time.gmtime())
	# start_date = "2020-04-14"
	# stop_date = "2020-10-14"
	# 05/30/2020
	
	start = datetime.datetime.strptime(start_date, "%d-%m-%Y")
	stop = datetime.datetime.strptime(stop_date, "%d-%m-%Y")
	while start < stop:
		start_date_entry1 = start.strftime('%d-%m-%Y')
		ts = time.strftime('%Y-%m-%d %H-%M-%S', time.gmtime())
		# Yahoo_output_path = r"C:\Users\hp\Desktop\scrapingProject\output files\calendar\yahoooutput"
		Yahoo_output_path = output_path+"\\yahoo"
		result = requests.get("https://finance.yahoo.com/calendar/earnings?day="+str(start.date()))


		soup = BeautifulSoup(result.text,"html.parser")
		mylist = []
		header = []	

		print("bs got the site")
		requests.packages.urllib3.disable_warnings()

		divparent = soup.find_all('div', attrs={'class':'Ovx(a) Ovx(h)--print Ovy(h)'})
		try:
			my_table = divparent[0].find_all('table', attrs={'class':'W(100%)'})
		except:
			print("no table div here!")
			start = start + timedelta(days=1)
			continue
		try:
			for row in my_table[0].findAll('tr'):
				for data in row.findAll('th'):
					if data.text == "Over the Last 4 Weeks":
						continue
					else:
						header.append(data.text)
				for data in row.findAll('td'):
					if data.text!="":
						mylist.append(data.text)
		except:
				print("no table here!")
				start = start + timedelta(days=1)
				continue
		start_date_filename = start.strftime('%Y-%m-%d')
		header.append("Date")
		# if headerCount == 0:
		fname = Yahoo_output_path
		if not os.path.exists(fname):
			os.makedirs(fname)
		opFile = fname+"\\"+"calendar_3_yahoo_"+start_date_filename+"_"+ts+".csv"
		myFile = open(opFile, 'w',newline = '')
		with myFile:
			writer = csv.writer(myFile)
			writer.writerows([header])
			headerCount = 1
			
			
		composite_list = [mylist[x:x+6] for x in range(0, len(mylist),6)]
		for k in range(0,len(composite_list)):
			composite_list[k].append(start_date_entry1)
		fname = Yahoo_output_path
		if not os.path.exists(fname):
			os.makedirs(fname)
		opFile = fname+"\\"+"calendar_3_yahoo_"+start_date_filename+"_"+ts+".csv"
		myFile = open(opFile, 'a',newline = '',encoding='utf-8')
		with myFile:
				writer = csv.writer(myFile)
				for z in range(0,len(composite_list)):
					writer.writerows([composite_list[z]])
					
		print("done for "+str(start.date()))
		start = start + timedelta(days=1)  # increase day one by one
		
				
				
# func()