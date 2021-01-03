import json 

import requests

import datetime
from datetime import timedelta
import time
from time import sleep
import os
import csv


# bloomberg_output_path = r'C:\Users\hp\Desktop\scrapingProject\output files\calendar\bloomberg\\'
# driver = webdriver.Firefox(executable_path = geckodriver, options=options)


def func(start_date,stop_date,output_path):
	# start_date = "2020-04-14"
	# stop_date = "2020-10-14"
	bloomberg_output_path = output_path+"\\bloomberg"
	start = datetime.datetime.strptime(start_date, "%d-%m-%Y")
	stop = datetime.datetime.strptime(stop_date, "%d-%m-%Y")
	headers = {'user-agent': 'my-app/0.0.1'}

	while start < stop:
		header = []
		mylist = []
		start_date_entry1 = start.strftime('%d-%m-%Y')
		ts = time.strftime('%Y-%m-%d %H-%M-%S', time.gmtime())

		# result = requests.get("http://webcache.googleusercontent.com/search?q=cache:https://www.bloomberg.com/markets/api/calendar/earnings/US?locale=en&date="+str(start.date()))
		result = requests.get("https://www.bloomberg.com/markets/api/calendar/earnings/US?locale=en&date="+str(start.date()), headers = headers)
		# print(result.text)
		# data = json.loads(result.text)
		# print(data)
		# WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="rawdata-tab"]'))).click()
		# pre = driver.find_element_by_tag_name("pre").text
		# data = json.loads(pre)
		# print(type(data))
		# print(data.keys())
		try:
			data = json.loads(result.text)
			d = (data["events"])
		except:
			print("no data")
			start = start + timedelta(days=1)
			continue
			
		mylist = []
		try:
			for i in range(0,len(d)):
				mylist.append(d[i]["company"]["ticker"]) #0
				mylist.append(d[i]["company"]["name"]) #1
				date = datetime.datetime.strptime(d[i]["eventTime"]["date"], "%m/%d/%Y")
				mylist.append(date.strftime('%d/%m/%Y'))
				mylist.append(str(d[i]["fiscalPeriod"]["period"]) +"/"+ str(d[0]["fiscalPeriod"]["year"])) #3
				mylist.append(str(d[i]["eps"]["estimate"]) +"/"+ str(d[0]["eps"]["actual"] ))
				
		except:
			# print("no data")
			start = start + timedelta(days=1)
			continue
			
			


		header.insert(0,"Ticker")
		header.insert(1,"Company")
		header.insert(2,"Est. Date")
		header.insert(3,"Period Ending")
		header.insert(4,"EST/Actual EPS")

		fname = bloomberg_output_path
		if not os.path.exists(fname):
			os.makedirs(fname)
		opFile = fname+"\\"+"calendar_3_bloomberg_"+start_date_entry1+"_"+ts+".csv"
		myFile = open(opFile, 'w',newline = '')
		with myFile:
			writer = csv.writer(myFile)
			writer.writerows([header])


			
		composite_list = [mylist[x:x+5] for x in range(0, len(mylist),5)]

		fname = bloomberg_output_path
		if not os.path.exists(fname):
			os.makedirs(fname)
		opFile = fname+"\\"+"calendar_3_bloomberg_"+start_date_entry1+"_"+ts+".csv"
		myFile = open(opFile, 'a',newline = '',encoding='utf-8')
		with myFile:
				writer = csv.writer(myFile)
				for z in range(0,len(composite_list)):
					writer.writerows([composite_list[z]])
						
						
						
		print("done for "+str(start.date()))
		start = start + timedelta(days=1)  # increase day one by one
		# time.sleep(1)


# func("05-07-2020","31-12-2020","C:\\Users\\hp\\Desktop\\scrapingProject\\output files\\calendar\\sep 19 outputs")