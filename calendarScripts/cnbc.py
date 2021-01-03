#https://apps.cnbc.com/resources/asp/getBufferedEventList.asp?date=1602518400000&..contenttype..=text%2Fjavascript&..requester..=ContentBuffer

#THIS WORKS PERFECT
import calendar
import json 
import requests
from bs4 import BeautifulSoup
import csv
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import csv
import datetime
# goforit = 1
from datetime import timedelta
from selenium.common.exceptions import StaleElementReferenceException
buttonFlagYear = 0
buttonFlagMonth = 0
mylist = []
header = []
chromepath = r"C:\Users\hp\Downloads\chromedriver_win32 (7)\chromedriver.exe"
options = Options()
options.add_argument("--headless")
options.add_argument('--disable-gpu')
options.add_argument('--log-level=3')
options.add_argument('--lang=en')
options.add_argument("--window-size=1920x1080")
options.add_argument("--disable-notifications")
options.add_argument('--no-sandbox')
# 
options.add_argument('--disable-software-rasterizer')
def func(start_date,stop_date,output_path):
	# start_date = "2020-04-20"
	# stop_date = "2020-04-21"
	start = datetime.datetime.strptime(start_date, "%d-%m-%Y")
	stop = datetime.datetime.strptime(stop_date, "%d-%m-%Y")
	CNBC_output = output_path+"\\cnbc"
	
	driver = webdriver.Chrome(executable_path=chromepath, options=options)
	driver.get("https://apps.cnbc.com/view.asp?YYY330_XPDfu5vdhz9HyCRjr3G70R0A9hRO7fWtFsoR8c7jlUv40AuQQ+bZ2e2tRbDtPKi0jNSra6i07nSOl37m3JhZcF6UFhBqkWis+mriZ3WQV9bt1KBPELIlyA==&uid=tools/earningsCenter&view=calendar")
	while start <= stop:
		weekend = 0
		goforit = 1
		start_date_entry1 = start.strftime('%d-%m-%Y')
		 
		print("doing now for CNBC: ", start_date_entry1)
		weekday  = calendar.day_name[start.weekday()] 
		
		
		
		if weekday == 'Saturday':
			print("weekend date")
			start = start + timedelta(days=1)
			continue
			
		if weekday == 'Sunday':
			print("weekend date")
			start = start + timedelta(days=1)
			continue
		# desired_date = "2020/05/30"
		ts = time.strftime('%Y-%m-%d %H-%M-%S', time.gmtime())
		desired_date_object = datetime.datetime.strptime(start_date_entry1, '%d-%m-%Y')  #
		desired_year = desired_date_object.strftime("%Y")
		desired_month =desired_date_object.strftime("%m")
		desired_day =desired_date_object.strftime("%d")
		if("0" in desired_day[0]):
			my_day = desired_day[1]
			desired_day = my_day
			print("desired_day:", desired_day)
		
		desired_stmt = 	desired_day+weekday
		# driver.get("https://apps.cnbc.com/view.asp?YYY330_XPDfu5vdhz9HyCRjr3G70R0A9hRO7fWtFsoR8c7jlUv40AuQQ+bZ2e2tRbDtPKi0jNSra6i07nSOl37m3JhZcF6UFhBqkWis+mriZ3WQV9bt1KBPELIlyA==&uid=tools/earningsCenter&view=calendar")
		
		time.sleep(2)
		soup = BeautifulSoup(driver.page_source,"html.parser")
		# word = ""	
		header = []
		mylist = []
		words = []
		month_displayed_word = []
		month_displayed_int = []
		
		try:
			divparent = soup.find_all('div', attrs={'class':'moduleBox'})
			divparent1 = divparent[0].find_all('div', attrs={'id':'month'})
			divparent2 = divparent1[0].find_all('div')
			
		except:
			print("not there 68")
			pass
		
		
		for d in divparent2:
			if d.text!="":
				words.append(d.text)
				
		for word in words:	
			year_displayed = word[-4:]
			
			if(year_displayed == desired_year):
				print("years match.")
				buttonFlagYear = 0
				break
			
			
		if buttonFlagYear == 0:
			for word in words:
				month_displayed_word.append(word[:-5])
				
			for m in month_displayed_word:
				current_month_object = datetime.datetime.strptime(m,'%B')
				month_displayed_int.append(current_month_object.strftime("%m"))
				
				
			while (desired_month not in month_displayed_int):
				# print("click")
				WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="dayContainer"]/div[7]/a'))).click()
				time.sleep(2)
				soup = BeautifulSoup(driver.page_source,"html.parser")
				try:
					divparent = soup.find_all('div', attrs={'class':'moduleBox'})
					divparent1 = divparent[0].find_all('div', attrs={'id':'month'})
					divparent2 = divparent1[0].find_all('div')
					
				except:
					print("not there 68")
					pass
					
				for d in divparent2:
					if d.text!="":
						words.append(d.text)
				for word in words:
					month_displayed_word.append(word[:-5])
				
				for m in month_displayed_word:
					current_month_object = datetime.datetime.strptime(m,'%B')
					month_displayed_int.append(current_month_object.strftime("%m"))
					
			# print("month_displayed_int: ",month_displayed_int)
			
			
			
			
			
			
			#at this point we are finally in the month we need
			#search for the day
			try:
				divparent = soup.find_all('div', attrs={'class':'moduleBox'})
				divparent1 = divparent[0].find_all('div', attrs={'id':'dayContainer'})
				divparent2 = divparent1[0].find_all('div')
			except:
				print("not there")
				pass
				
			days = []	
			# days.append(divparent1[0].find('b').text)
			for i in range(0,len(divparent2)):
				if divparent2[i].find('b') is None:
					continue
				days.append(divparent2[i].find('h6').text)
			# desired_stmt = days[0].strip()
				
				
				# aaa
				
			# print("days: ", days)
			first_time = 0
			while (True):
				
				
				time.sleep(2)
				soup = BeautifulSoup(driver.page_source,"html.parser")
				
				try:
					divparent = soup.find_all('div', attrs={'class':'moduleBox'})
					divparent1 = divparent[0].find_all('div', attrs={'id':'dayContainer'})
					divparent2 = divparent1[0].find_all('div')
				except:
					print("not there")
					pass
					
				days = []	
				# days.append(divparent1[0].find('b').text)
				for i in range(0,len(divparent2)):
					if divparent2[i].find('b') is None:
						continue
					days.append(divparent2[i].find('h6').text.replace(" ",""))
				current_stmt = days[0].strip()
				# print("desired_stmt: ",desired_stmt)
				# print("current_stmt: ",current_stmt)
				if(desired_stmt in days):
					break
				else:
					print("nope")
				
				# print("click")
				WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="dayContainer"]/div[7]/a'))).click()
					
				# if days[0] > desired_day:
					# #its a weekend datetime
					# print(days)
					# print(desired_day)
					# weekend = 1
					# break
					
				
					
			# if weekend == 1:
				# print("weekend date")
				# start = start + timedelta(days=1)  # increase day one by one
				# continue
				
				
			#now scrape all the data
			
			
			
			
			dayIndex = days.index(desired_stmt)
			linkPath = '//*[@id="expected'+str(dayIndex)+'"]/a'
			# print(dayIndex)
			
			# print(linkPath) //*[@id="expected0"]/a
			try:
				WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,linkPath))).click()
			except:
				print("no data")
				start = start + timedelta(days=1)
				continue
			time.sleep(5)
			#count the number of links here
			
			link = driver.find_element_by_xpath('//*[@id="pagination"]')
			links = link.find_elements_by_xpath('a')
			# print(links)
			# sys.exit()
			pageNum = 1
			headerCount = 0
			while(True):
				# if(pageNum >= len(links)):
					# break
				print("page: ",pageNum)
				header = []
				mylist = []
				soup = BeautifulSoup(driver.page_source,"html.parser")
				requests.packages.urllib3.disable_warnings()
				try:
					my_table = soup.find_all('table', attrs = {'id':'mainTable'})
				except:
					print("no table")
					continue
				for record in my_table[0].findAll('tr'):
					for data in record.findAll('th'):
						if data.text!="":
							header.append(data.text) #DO THE WHOLE TABLE SCRAPE HERE!!!
						
				for record in my_table[0].findAll('tr'):
					for data in record.findAll('td'):
						if data.text!="":
							# print(data.text)
							mylist.append(data.text.strip()) #DO THE WHOLE TABLE SCRAPE HERE!!!
							
							
				composite_list = [mylist[x:x+len(header)] for x in range(0, len(mylist),len(header))]
				header.append("Date")
				for k in range(0,len(composite_list)):
					composite_list[k].append(start_date_entry1)
					
				start_date_filename = start.strftime('%Y-%m-%d')
				
				if headerCount == 0:
					fname = CNBC_output
					if not os.path.exists(fname):
						os.makedirs(fname)
					opFile = fname+"\\"+"calendar_3_cnbc_"+start_date_filename+"_"+ts+".csv"
					myFile = open(opFile, 'w',newline = '')
					with myFile:
						writer = csv.writer(myFile)
						writer.writerows([header])
						headerCount = 1


					
				# composite_list = [mylist[x:x+5] for x in range(0, len(mylist),5)]

				fname = CNBC_output
				if not os.path.exists(fname):
					os.makedirs(fname)
				opFile = fname+"\\"+"calendar_3_cnbc_"+start_date_filename+"_"+ts+".csv"
				myFile = open(opFile, 'a',newline = '',encoding='utf-8')
				with myFile:
						writer = csv.writer(myFile)
						for z in range(0,len(composite_list)):
							writer.writerows([composite_list[z]])
							
							
				#----------------------------------------------------------------------------------
				
				try:
					link = driver.find_element_by_xpath('//*[@id="pagination"]')
					links = link.find_elements_by_xpath('a')
					# print(links)
				except:
					print("this is only page")
					break
					
				# if(pageNum >= len(links)):
					# break
				
				try:
					# print("gonna click")
					link = driver.find_element_by_link_text(str(pageNum+1))
					link.click()
					time.sleep(2)
					pageNum = pageNum + 1
					
				except:
					print("end of the pages")
					break
					
					
				#----------------------------------------------------------------------------------
	# break
		start = start + timedelta(days=1)  # increase day one by one
	
	
	fileNames = os.listdir(CNBC_output)
	cnbc_files = CNBC_output


	for i in range(0,len(fileNames)):
		mylist = []
		header = []
		with open(CNBC_output+"\\"+fileNames[i], 'r') as csvFile:
			reader = csv.reader(csvFile)
			# print(type(next(reader)))
			head = [x.lower() for x in next(reader)]
			for h in head:
				header.append(h.replace(" ","_"))



		e = 0
		with open(CNBC_output+"\\"+fileNames[i], 'r') as csvFile:
			reader = csv.reader(csvFile)
			for row in reader:
				data = []
				if e == 0:
					e = 1
					continue
				else:
					data.append(row[0].replace('Â',''))
					data.append(row[1].replace('Â',''))
					data.append(row[2])
					data.append(row[3])
					data.append(row[4])
					
					
					mylist = mylist+data
					
					
		composite_list = [mylist[x:x+len(header)] for x in range(0, len(mylist),len(header))]
		
		
		fname = cnbc_files
		if not os.path.exists(fname):
			os.makedirs(fname)
		opFile = fname+"\\"+fileNames[i]
		myFile = open(opFile, 'w',newline = '')
		with myFile:
			writer = csv.writer(myFile)
			writer.writerows([header])
				# headerCount = 1
				
				

		fname = cnbc_files
		if not os.path.exists(fname):
			os.makedirs(fname)
		opFile = fname+"\\"+fileNames[i]
		myFile = open(opFile, 'a',newline = '')
		with myFile:
			writer = csv.writer(myFile)
			for z in range(0,len(composite_list)):
				writer.writerows([composite_list[z]])
		
		# break
		
# start_date = "30-10-2020"
# stop_date = "04-11-2020"
# output_path = "C:\\Users\\hp\\Desktop\\scrapingProject\\output files\\calendar\\sep 21 testing"
# func(start_date,stop_date,output_path)