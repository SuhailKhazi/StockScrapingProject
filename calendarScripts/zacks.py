import json 
import calendar
import requests
from bs4 import BeautifulSoup
import csv
import os
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import datetime
from datetime import timedelta
from selenium.common.exceptions import StaleElementReferenceException

# mylist = []
# header = []
chromepath = r"C:\Users\hp\Downloads\chromedriver_win32 (7)\chromedriver.exe"
options = Options()
options.add_argument("--headless")
options.add_argument('--disable-gpu')
options.add_argument('--log-level=3')
options.add_argument('--lang=en')
options.add_argument("--window-size=1920x1080")
options.add_argument("--disable-notifications")
options.add_argument('--no-sandbox')

options.add_argument('--disable-software-rasterizer')
# start_date = "2020/04/20"
# stop_date = "2020/05/30"
# start = datetime.datetime.strptime(start_date, '%Y/%m/%d') 
# stop = datetime.datetime.strptime(stop_date, '%Y/%m/%d') 
# desired_year = start.strftime("%Y")
# desired_month =start.strftime("%B")
# driver = webdriver.Chrome(executable_path=chromepath, options=options)
# driver.get("https://www.zacks.com/earnings/earnings-calendar")
# zacks_output_path = r'C:\Users\hp\Desktop\scrapingProject\output files\calendar\zacks_rescrape'
	
def func(start_date,stop_date,output_path):	
	# start_date = "2020/05/09"
	driver = webdriver.Chrome(executable_path=chromepath, options=options)
	# stop_date = "2020/06/09"
	zacks_output_path = output_path+"\\zacks"
	start = datetime.datetime.strptime(start_date, "%d-%m-%Y") 
	stop = datetime.datetime.strptime(stop_date, "%d-%m-%Y") 
	
	
	try:
		driver.get("https://www.zacks.com/earnings/earnings-calendar")
	except:
		driver.get("https://www.zacks.com/earnings/earnings-calendar")
	while start < stop:
		weekday  = calendar.day_name[start.weekday()] 
		
		
		
		if weekday == 'Saturday':
			print("weekend date")
			start = start + timedelta(days=1)
			continue
			
		if weekday == 'Sunday':
			print("weekend date")
			start = start + timedelta(days=1)
			continue
		
		
		
		start_date_entry1 = start.strftime('%d-%m-%Y')
		ts = time.strftime('%Y-%m-%d %H-%M-%S', time.gmtime())
		print("Starting: ",start_date_entry1)
		header = []
		mylist = []
		# start = datetime.datetime.strptime(start_date, '%Y/%m/%d')  #
		desired_year = start.strftime("%Y")
		desired_month =start.strftime("%B")
		buttonFlag = 0
		# function to handle setting up headless download
		# driver = webdriver.Chrome(executable_path=chromepath, options=options)
		# enable_download_headless(driver, download_dir)
		word = ""
		# WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="date_select"]/img'))).click()
		
		element = driver.find_element_by_xpath('//*[@id="date_select"]/img')
		driver.execute_script("arguments[0].click();", element)


		soup = BeautifulSoup(driver.page_source,"html.parser")

		# print("bs got the site")
		requests.packages.urllib3.disable_warnings()

		divparent = soup.find_all('div', attrs={'id':'minical_place_holder'})
		try:
			my_table = divparent[0].find('table')
		except:
			print("no table div here!")
			pass
			
		try:
			for row in my_table.findAll('tr'):
				for data in row.findAll('td'):
					if data.text!="":
						word = data.text
						break
				break
		except:
			print("no table here!")
			pass
		month_displayed = word[:-5]	
		year_displayed = word[-4:]
		# print("month displayed:",month_displayed)
		# print("year displayed:" ,year_displayed)

		#take year and compare
		#while desired year is less than the year currently displayed, click left button till you get that year. it will be in december
		if(str(desired_year) < year_displayed):
			while(str(desired_year) < year_displayed):
				#click left button till you get 2018
				# print("gonna click button")
				WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="prevCal"]'))).click()
				soup = BeautifulSoup(driver.page_source,"html.parser")

				
				requests.packages.urllib3.disable_warnings()

				divparent = soup.find_all('div', attrs={'id':'minical_place_holder'})
				try:
					my_table = divparent[0].find('table')
				except:
					print("no table div here!")
					pass
					
				try:
					for row in my_table.findAll('tr'):
						for data in row.findAll('td'):
							if data.text!="":
								word = data.text
								break
						break
				except:
					print("no table here!")
					pass
				month_displayed = word[:-5]	
				year_displayed = word[-4:]
				# print("month displayed now:",month_displayed)
				# print("year displayed now:" ,year_displayed)
				buttonFlag = 1
				

		if(str(desired_year) > year_displayed):
			while(str(desired_year) > year_displayed):
				#click left button till you get 2018
				print("gonna click button")
				WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="nextCal"]'))).click()
				soup = BeautifulSoup(driver.page_source,"html.parser")

				
				requests.packages.urllib3.disable_warnings()

				divparent = soup.find_all('div', attrs={'id':'minical_place_holder'})
				try:
					my_table = divparent[0].find('table')
				except:
					print("no table div here!")
					pass
					
				try:
					for row in my_table.findAll('tr'):
						for data in row.findAll('td'):
							if data.text!="":
								word = data.text
								break
						break
				except:
					print("no table here!")
					pass
				month_displayed = word[:-5]	
				year_displayed = word[-4:]
				# print("month displayed now:",month_displayed)
				# print("year displayed now:" ,year_displayed)
				buttonFlag = 2
				
		if(buttonFlag == 0):
			#convert displayed/current month to an integer
			current_month_object = datetime.datetime.strptime(month_displayed,'%B')
			current_month_int = current_month_object.strftime("%m")
			#print(current_month_int, type(current_month_int)) #although its string..but still
			
			#convert desired month to an integer
			desired_month =start.strftime("%m")
			#print(desired_month,type(desired_month))
			
			#you have to go left if the month you want is less than the current month
			while(desired_month < current_month_int):
				print("gonna click button")
				WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="prevCal"]'))).click()
				soup = BeautifulSoup(driver.page_source,"html.parser")

				
				requests.packages.urllib3.disable_warnings()

				divparent = soup.find_all('div', attrs={'id':'minical_place_holder'})
				try:
					my_table = divparent[0].find('table')
				except:
					print("no table div here!")
					pass
					
				try:
					for row in my_table.findAll('tr'):
						for data in row.findAll('td'):
							if data.text!="":
								word = data.text
								break
						break
				except:
					print("no table here!")
					pass
				month_displayed = word[:-5]	
				year_displayed = word[-4:]
				print("month displayed now:",month_displayed)
				print("year displayed now:" ,year_displayed)
				month_displayed_object = datetime.datetime.strptime(month_displayed,'%B')
				current_month_int = month_displayed_object.strftime("%m")
				
				
				
			while(desired_month > current_month_int):
				print("gonna click button")
				WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="nextCal"]'))).click()
				soup = BeautifulSoup(driver.page_source,"html.parser")

				
				requests.packages.urllib3.disable_warnings()

				divparent = soup.find_all('div', attrs={'id':'minical_place_holder'})
				try:
					my_table = divparent[0].find('table')
				except:
					print("no table div here!")
					pass
					
				try:
					for row in my_table.findAll('tr'):
						for data in row.findAll('td'):
							if data.text!="":
								word = data.text
								break
						break
				except:
					print("no table here!")
					pass
				month_displayed = word[:-5]	
				year_displayed = word[-4:]
				print("month displayed now:",month_displayed)
				print("year displayed now:" ,year_displayed)
				month_displayed_object = datetime.datetime.strptime(month_displayed,'%B')
				current_month_int = month_displayed_object.strftime("%m")
				
			#now that you got your year and month, search for your day
			#14: //*[@id="dt_14"]
			#31: //*[@id="dt_31"]
			desired_day =start.strftime("%d")
			if("0" in desired_day[0]):
				desired_day1= desired_day[1]
				desired_day = desired_day1
			day_id = "dt_"+desired_day
			# print("day_id is: ",day_id)
			WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID,day_id))).click()
			# print("got the day!")
			#earnings_rel_data_all_table_length
			time.sleep(5)
			select = Select(driver.find_element_by_name('earnings_rel_data_all_table_length'))
			select.select_by_visible_text('ALL')
			
			
			
			
			soup = BeautifulSoup(driver.page_source,"html.parser")
			#return
			

			print("bs got the site")
			#left-column-div
			requests.packages.urllib3.disable_warnings()
			#
			# divparent = soup.find_all('div', attrs={'class':'DTFC_ScrollWrapper'})
			# divparent1 = divparent[0].find_all('div', attrs={'class':'dataTables_scroll'})
			try:
				divparent = soup.find_all('div', attrs={'class':'DTFC_ScrollWrapper'})
				divparent1 = divparent[0].find_all('div', attrs={'class':'dataTables_scroll'})
				my_table = divparent[0].find_all('table', attrs={'display dataTable no-footer'})
			except:
				print("no table div here!")
				start = start + timedelta(days=1)
				continue
			# try:
			thead = my_table[0].find('thead')
			i = 0
			
			for row in thead.findAll('tr'):
				for data in row.findAll('th'):
					if data.text == "":
						continue
					if data.text == "/  Forecast":
						continue
					if data.text == "Report":
						continue
					else:
						header.append(data.text)
						# i = i+1
				
			# header.append("Date")	
			#return
			try:
				divparent2 = divparent1[0].find_all('div', attrs={'class':'dataTables_scrollBody'})
			except:
				print("no table div here!")
				start = start + timedelta(days=1)
				continue
			my_table = divparent2[0].find_all('table', attrs = {'id':'earnings_rel_data_all_table'})
			tbody = my_table[0].find('tbody')
			i = 0
			print("----------------------------------------------------")
			for row in tbody.findAll('tr'):
				for data in row.findAll('td'):
					if data.text == "":
						continue
					if data.text == "No data available in table":
						continue
					else:
						mylist.append(data.text)
						# i = i+1
			if(len(mylist)) == 0:
				print("no data")
				start = start + timedelta(days=1)
				continue
				
				
			composite_list = [mylist[x:x+len(header)] for x in range(0, len(mylist),len(header))]
			header.append("Date")
			for k in range(0,len(composite_list)):
				composite_list[k].append(start_date_entry1)
				
			# print(composite_list[0])
			# break
				
			start_date_filename = start.strftime('%Y-%m-%d')	
			fname = zacks_output_path
			if not os.path.exists(fname):
				os.makedirs(fname)
			opFile = fname+"\\"+"calendar_3_zacks_"+start_date_filename+"_"+ts+".csv"
			myFile = open(opFile, 'w',newline = '')
			with myFile:
				writer = csv.writer(myFile)
				writer.writerows([header])


				
			# composite_list = [mylist[x:x+5] for x in range(0, len(mylist),5)]

			fname = zacks_output_path
			if not os.path.exists(fname):
				os.makedirs(fname)
			opFile = fname+"\\"+"calendar_3_zacks_"+start_date_filename+"_"+ts+".csv"
			myFile = open(opFile, 'a',newline = '',encoding='utf-8')
			with myFile:
					writer = csv.writer(myFile)
					for z in range(0,len(composite_list)):
						writer.writerows([composite_list[z]])
			
			
			
			
		if(buttonFlag == 1):
			#convert displayed/current month to an integer
			current_month_object = datetime.datetime.strptime(month_displayed,'%B')
			current_month_int = current_month_object.strftime("%m")
			#print(current_month_int, type(current_month_int)) #although its string..but still
			
			#convert desired month to an integer
			desired_month =start.strftime("%m")
			#print(desired_month,type(desired_month))
			
			#you have to go left if the month you want is less than the current month
			while(desired_month < current_month_int):
				print("gonna click button")
				WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="prevCal"]'))).click()
				soup = BeautifulSoup(driver.page_source,"html.parser")

				
				requests.packages.urllib3.disable_warnings()

				divparent = soup.find_all('div', attrs={'id':'minical_place_holder'})
				try:
					my_table = divparent[0].find('table')
				except:
					print("no table div here!")
					pass
					
				try:
					for row in my_table.findAll('tr'):
						for data in row.findAll('td'):
							if data.text!="":
								word = data.text
								break
						break
				except:
					print("no table here!")
					pass
				month_displayed = word[:-5]	
				year_displayed = word[-4:]
				print("month displayed now:",month_displayed)
				print("year displayed now:" ,year_displayed)
				month_displayed_object = datetime.datetime.strptime(month_displayed,'%B')
				current_month_int = month_displayed_object.strftime("%m")
			desired_day =start.strftime("%d")
			if("0" in desired_day[0]):
				desired_day[0] = desired_day[0].replace('0', '')
			day_id = "dt_"+desired_day
			print("day_id is: ",day_id)
			WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID,day_id))).click()
			print("got the day!")
			
			select = Select(driver.find_element_by_name('earnings_rel_data_all_table_length'))
			select.select_by_visible_text('ALL')
			
			
			soup = BeautifulSoup(driver.page_source,"html.parser")
			print("bs got the site")
			requests.packages.urllib3.disable_warnings()
			#
			divparent = soup.find_all('div', attrs={'class':'DTFC_ScrollWrapper'})
			try:
				my_table = divparent[0].find_all('table', attrs={'display dataTable no-footer'})
			except:
				print("no table div here!")
				start = start + timedelta(days=1)
				continue
			# try:
			thead = my_table[0].find('thead')
			
			for row in thead.findAll('tr'):
				for data in row.findAll('th'):
					if data.text == "":
						continue
					else:
						print(data.text)
						
			try:
				my_table = divparent[0].find_all('table', attrs={'display dataTable no-footer'})
			except:
				print("no table div here!")
				pass
			tbody = my_table[1].find('tbody')
			print("----------------------------------------------------")
			for row in tbody.findAll('tr'):
				for data in row.findAll('td'):
					if data.text == "":
						continue
					else:
						print(data.text)
				
				
				
				
		if(buttonFlag == 2):
			#convert displayed/current month to an integer
			current_month_object = datetime.datetime.strptime(month_displayed,'%B')
			current_month_int = current_month_object.strftime("%m")
			#print(current_month_int, type(current_month_int)) #although its string..but still
			
			#convert desired month to an integer
			desired_month =start.strftime("%m")
			#print(desired_month,type(desired_month))
			while(desired_month > current_month_int):
				print("gonna click button")
				WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="nextCal"]'))).click()
				soup = BeautifulSoup(driver.page_source,"html.parser")

				
				requests.packages.urllib3.disable_warnings()

				divparent = soup.find_all('div', attrs={'id':'minical_place_holder'})
				try:
					my_table = divparent[0].find('table')
				except:
					print("no table div here!")
					pass
					
				try:
					for row in my_table.findAll('tr'):
						for data in row.findAll('td'):
							if data.text!="":
								word = data.text
								break
						break
				except:
					print("no table here!")
					pass
				month_displayed = word[:-5]	
				year_displayed = word[-4:]
				print("month displayed now:",month_displayed)
				print("year displayed now:" ,year_displayed)
				month_displayed_object = datetime.datetime.strptime(month_displayed,'%B')
				current_month_int = month_displayed_object.strftime("%m")
				
			desired_day =start.strftime("%d")
			if("0" in desired_day[0]):
				desired_day[0] = desired_day[0].replace('0', '')
			day_id = "dt_"+desired_day
			print("day_id is: ",day_id)
			WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID,day_id))).click()
			print("got the day!")
			
			select = Select(driver.find_element_by_name('earnings_rel_data_all_table_length'))
			select.select_by_visible_text('ALL')
			
			soup = BeautifulSoup(driver.page_source,"html.parser")
			#return
			

			print("bs got the site")
			#left-column-div
			requests.packages.urllib3.disable_warnings()
			#
			divparent = soup.find_all('div', attrs={'class':'DTFC_ScrollWrapper'})
			divparent1 = divparent[0].find_all('div', attrs={'class':'dataTables_scroll'})
			try:
				my_table = divparent[0].find_all('table', attrs={'display dataTable no-footer'})
			except:
				print("no table div here!")
				start = start + timedelta(days=1)
				continue
			# try:
			thead = my_table[0].find('thead')
			i = 0
			
			for row in thead.findAll('tr'):
				for data in row.findAll('th'):
					if data.text == "":
						continue
					if data.text == "/  Forecast":
						continue
					else:
						print(i,data.text)
						i = i+1
				
						
			try:
				my_table = divparent[0].find_all('table', attrs={'display dataTable no-footer'})
			except:
				print("no table div here!")
				# return
				start = start + timedelta(days=1)
				continue
			tbody = my_table[1].find('tbody')
			i = 0
			print("----------------------------------------------------")
			for row in tbody.findAll('tr'):
				for data in row.findAll('td'):
					if data.text == "":
						continue
					else:
						print(i,data.text)
						i = i+1
		print("done for "+str(start.date()))
		start = start + timedelta(days=1)  # increase day one by one
# func()


# start_date = "07-08-2020"
# stop_date = "05-09-2020"
# output_path = "C:\\Users\\hp\\Desktop\\scrapingProject\\output files\\calendar\\july 13 outputs"
# func(start_date,stop_date,output_path)