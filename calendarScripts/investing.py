#THIS IS THE WORKING CODE

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
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

options = Options()
options.add_argument("--headless")
options.add_argument("--window-size=1920x1080")
options.add_argument("--disable-notifications")
options.add_argument('--no-sandbox')
options.add_argument('--log-level=3')
#options.add_argument('--verbose')

options.add_argument('--disable-gpu')
options.add_argument('--disable-software-rasterizer')
chromepath = r"C:\Users\hp\Downloads\chromedriver_win32 (7)\chromedriver.exe"
# driver = webdriver.Chrome(options=options, executable_path=r'C:\Users\hp\Desktop\scrapingProject\settings\chromedriver\chromedriver.exe')
# driver.get("https://www.investing.com/earnings-calendar/")
def func(start_date,stop_date,output_path):
	ts = time.strftime('%Y-%m-%d %H-%M-%S', time.gmtime())
	# start_date = "04/23/2020"
	# stop_date = "10/14/2020"
	# headerCount = 0
	start = datetime.datetime.strptime(start_date, "%d-%m-%Y")
	stop = datetime.datetime.strptime(stop_date, "%d-%m-%Y")
	driver = webdriver.Chrome(options=options, executable_path=chromepath)
	driver.get("https://www.investing.com/earnings-calendar/")
	print("starting")
	while start <= stop:
		start_date_entry = start.strftime('%m/%d/%Y')
		# stop_date_entry = stop.strftime('%m/%d/%Y')
		# print("in loop")
		# driver.get("https://www.investing.com/earnings-calendar/")
		# //*[@id="datePickerToggleBtn"]
		WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="datePickerToggleBtn"]'))).click()
		# print("click")
		WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="startDate"]'))).clear()
		# print("click")
		WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="endDate"]'))).clear()
		# print("click")
		WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="startDate"]'))).send_keys(start_date_entry)
		# print("click")
		WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="endDate"]'))).send_keys(start_date_entry)
		# print("click")
		WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="applyBtn"]'))).click()
		# investing_output_path = r'C:\Users\hp\Desktop\scrapingProject\output files\calendar\Investing'
		investing_output_path = output_path+"\\investing"
		time.sleep(5)
		

		soup = BeautifulSoup(driver.page_source,"html.parser")
		mylist = []
		header = []	

		print("bs got the site")
		requests.packages.urllib3.disable_warnings()
		
		divparent = soup.find_all('div', attrs={'class':'eCalNew eCalMainNew'})
		try:
			my_table = divparent[0].find_all('table', attrs={'class':'genTbl closedTbl ecoCalTbl earnings persistArea js-earnings-table'})
			thead = my_table[0].find('thead')
		except:
			print("no table div here!")
			start = start + timedelta(days=1)
			continue
			
		# thead = my_table[0].find('thead')
		
		for row in thead.findAll('tr'):
			for data in row.findAll('th'):
				if data.text == "":
					continue
				# if data.text == "/  Forecast":
					# continue
				else:
					header.append(data.text)
		print("--------------------------------------------------------------------")		
		for j in range(0,len(header)):
			if("\xa0\xa0" in header[j]):
				header[j] = header[j].replace("\xa0\xa0","")
		header[1:3] = [''.join(header[1:3])]
		header[2:4] = [''.join(header[2:4])]
		#print(header)
		header.pop()
		header.insert(0,"Country")			
		# print(header)
		
		# if data.find(['class'][0]) == "right":
		# 
		# print(header)
		
		for row in my_table[0].findAll('tr'):
			for data in row.find_all('td'):
				if data.attrs['class'][0] == 'right':
					mylist.append(data.text)
					break
				if data.attrs['class'][0] == "left noWrap earnCalCompany":
					mylist.append(data.find('span').text)
					continue
				if data.text == '\n\n':
					mylist.append(data.find('span')['title'])
					continue	
				else:
					mylist.append(data.text.replace('\n',"").strip())
					
		mylist.pop(0)
		composite_list = [mylist[x:x+7] for x in range(0, len(mylist),7)]
		
		for j in composite_list:
			j[2:4] = [''.join(j[2:4])]
			j[3:5] = [''.join(j[3:5])]
			for k in range(0,len(j)):
				if("\xa0\xa0" in j[k]):
					j[k] = j[k].replace("\xa0\xa0","")
				if("\xa0" in j[k]):
					j[k] = j[k].replace("\xa0","")
		# try:
			# print(composite_list[3])
		# except:
			# print("no data here")
			# start = start + timedelta(days=1)
			# continue
		# start_date_filename = datetime.datetime.strptime(start_date, "%m-%d-%Y")
		# stop_date_filename = datetime.datetime.strptime(stop_date, "%m-%d-%Y")
		start_date_filename1 = start.strftime('%d-%m-%Y')
		# stop_date_filename1 = stop_date_filename.strftime('%m-%d-%Y')
		start_date_filename = start.strftime('%Y-%m-%d')
		header.append("Date")
		for k in range(0,len(composite_list)):
			composite_list[k].append(start_date_filename1)
			
		# if headerCount == 0:
		fname = investing_output_path
		if not os.path.exists(fname):
			os.makedirs(fname)
		opFile = fname+"\\"+"calendar_3_investing_"+start_date_filename+"_"+ts+".csv"
		myFile = open(opFile, 'w',newline = '')
		with myFile:
			writer = csv.writer(myFile)
			writer.writerows([header])
			# headerCount = 1
			

		fname = investing_output_path
		if not os.path.exists(fname):
			os.makedirs(fname)
		opFile = fname+"\\"+"calendar_3_investing_"+start_date_filename+"_"+ts+".csv"
		myFile = open(opFile, 'a',newline = '',encoding='utf-8')
		with myFile:
				writer = csv.writer(myFile)
				for z in range(0,len(composite_list)):
					writer.writerows([composite_list[z]])

					
		
		start = start + timedelta(days=1)  # increase day one by one
		print("done ",start_date_filename1)
		time.sleep(1)
		# break
		# 2019/12/04
		

		
# func()

# start_date = "13-07-2020"
# stop_date = "14-11-2020"
# output_path = "C:\\Users\\hp\\Desktop\\scrapingProject\\output files\\calendar\\july 13 outputs"
# func(start_date,stop_date,output_path)