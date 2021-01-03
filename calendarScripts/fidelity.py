from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
import os
import requests
import time
import pandas as pd
from bs4 import BeautifulSoup
import urllib.request as ur
import re
import json
from lxml import etree
from bs4 import Comment
import csv
import sys
import datetime
from datetime import timedelta
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
path1 = "C:\\Users\\hp\\Desktop\\scrapingProject"
# with open(path1+"\\settings\\setting.txt") as json_file:
    
		# data = json.load(json_file) 
		# username = (data['watchlist_username'])
		# password = (data['watchlist_password'])
		# watchlist_download_path = (data['watchlist_download_path'])
		# view = (data['view'])



options = Options()
options.add_argument("--headless")
options.add_argument("--window-size=1920x1080")
options.add_argument("--disable-notifications")
options.add_argument('--no-sandbox')
options.add_argument('--log-level=3')
#options.add_argument('--verbose')
geckodriver = r"C:\Users\hp\Downloads\geckodriver-v0.26.0-win64 (2)\geckodriver.exe"
options.add_argument('--disable-gpu')
options.add_argument('--disable-software-rasterizer')

# driver = webdriver.Firefox(options=options, executable_path=geckodriver)
# headerCount = 0

def func(start_date,stop_date,output_path):
	headerCount = 0
	driver = webdriver.Firefox(options=options, executable_path=geckodriver)
	# ts = time.strftime('%Y-%m-%d %H-%M-%S', time.gmtime())
	# start_date = "2020-06-24"
	# stop_date = "2020-07-29"
	# 05/30/2020
	
	start = datetime.datetime.strptime(start_date, "%d-%m-%Y")
	stop = datetime.datetime.strptime(stop_date, "%d-%m-%Y")
	while start <= stop:
		start_date_entry1 = start.strftime('%d-%m-%Y')
		start_date_for_site = start.strftime('%m/%d/%Y')
		ts = time.strftime('%Y-%m-%d %H-%M-%S', time.gmtime())
		# Fidelity_output_path = r"C:\Users\hp\Desktop\scrapingProject\output files\calendar\fidelity"
		Fidelity_output_path = output_path+"\\fidelity"
		driver.get("https://eresearch.fidelity.com/eresearch/conferenceCalls.jhtml?tab=earnings&begindate="+start_date_for_site)


		soup = BeautifulSoup(driver.page_source,"html.parser")
		mylist = []
		header = []	

		print("bs got the site")
		requests.packages.urllib3.disable_warnings()

		divparent = soup.find_all('div', attrs={'class':'tabbed-box'})
		try:
			my_table = divparent[0].find_all('table', attrs={'class':'datatable-component events-calender-table-earnings events-calender-table-earnings-future-time-of-day'})
			thead = my_table[0].find('thead')
			tbody = my_table[0].find('tbody')
		except:
			print("no table div here!")
			start = start + timedelta(days=1)
			continue
		
		# thead = my_table[0].find('thead')
		try:
			for row in thead.findAll('tr'):
				for data in row.findAll('th'):
					for d in data.findAll('a'):
						if d.text == "Over the Last 4 Weeks":
							continue
						else:
							header.append(d.text.replace("\n","").strip())
					# for data in row.findAll('td'):
						# if data.text!="":
							# print(data.text)
		except:
				print("no table here!")
				start = start + timedelta(days=1)
				break
		
		
		print("--------------------------------")
		# tbody = my_table[0].find('tbody')
		try:
			for row in tbody.findAll('tr'):
				for data in row.findAll('th'):
					for d in data.findAll('a'):
						if d.text == "Company Website . opens in new window.":
							continue
						else:
							mylist.append(d.text.replace("\n","").strip())
				for data in row.findAll('td'):
					if data.findAll('a'):
						for d in data.findAll('a'):
							if d.findAll('strong'):
								for s in d.findAll('strong'):
									mylist.append(d.text.replace("\n","").strip())
							if data.text!="":
								mylist.append(d.text.replace("\n","").strip())
								
					else:
						if data.text!="":
							mylist.append(data.text.replace("\n","").strip())
		except:
				print("no table here!")
				start = start + timedelta(days=1)
				break
		while "Company Website . opens in new window." in mylist: mylist.remove("Company Website . opens in new window.")
		composite_list = [mylist[x:x+len(header)] for x in range(0, len(mylist),len(header))]
		header.append("Date_of_scrape")
		# if headerCount == 0:
		start_date_filename = start.strftime('%Y-%m-%d')
		fname = Fidelity_output_path
		if not os.path.exists(fname):
			os.makedirs(fname)
		opFile = fname+"\\"+"calendar_3_fidelity_"+start_date_filename+"_"+ts+".csv"
		myFile = open(opFile, 'w',newline = '')
		with myFile:
			writer = csv.writer(myFile)
			writer.writerows([header])
			# headerCount = 1
			
			
		# composite_list = [mylist[x:x+6] for x in range(0, len(mylist),6)]
		for k in range(0,len(composite_list)):
			composite_list[k].append(start_date_entry1)
		fname = Fidelity_output_path
		if not os.path.exists(fname):
			os.makedirs(fname)
		opFile = fname+"\\"+"calendar_3_fidelity_"+start_date_filename+"_"+ts+".csv"
		myFile = open(opFile, 'a',newline = '',encoding='utf-8')
		with myFile:
				writer = csv.writer(myFile)
				for z in range(0,len(composite_list)):
					writer.writerows([composite_list[z]])
					
		print("done for "+str(start.date()))
		start = start + timedelta(days=1)  # increase day one by one
		# break
		
				
				
# func()