import zacks #1
import bloomberg #2
import cnbc #3
import investing #4
import fidelity #5
import yahoo #6

import json
import threading

import datetime
from datetime import timedelta
from datetime import datetime


def ZACKS(start_date, stop_date,output_path):
	zacks.func(start_date, stop_date,output_path)
	
def BLOOMBERG(start_date, stop_date,output_path):
	bloomberg.func(start_date, stop_date,output_path)
	
def CNBC(start_date, stop_date,output_path):
	cnbc.func(start_date, stop_date,output_path)
	
def INVESTING(start_date, stop_date,output_path):
	investing.func(start_date, stop_date,output_path)
	
def FIDELITY(start_date, stop_date,output_path):
	fidelity.func(start_date, stop_date,output_path)
	
def YAHOO(start_date, stop_date,output_path):
	yahoo.func(start_date, stop_date,output_path)
	


with open(r'C:\Users\hp\Desktop\scrapingProject\calender\calendarScriptsTogether\settingsFileCalendar.txt') as json_file:
    
	data = json.load(json_file) 
	site = (data['sites'])
	start_date = (data['start_date'])
	stop_date = (data['stop_date'])
	output_path = (data['output_path'])
	simultanious = (data['simultanious'])
	mode_of_dates = (data['mode_of_dates'])
	days_for_mode_2 = (data['days_for_mode_2'])
	
	#here take option 0 or 1 from the json file to see if we want simultaneous running or one at a time running.
	
	if mode_of_dates == 1:
		if simultanious == 1:
		
		
			if 1 in site:
				print("gonna start zacks")
				threading.Thread(target=ZACKS,args=([start_date,stop_date,output_path])).start()
			
			if 2 in site:
				print("gonna start bloomberg")
				threading.Thread(target=BLOOMBERG,args=([start_date,stop_date,output_path])).start()
				
			if 3 in site:
				print("gonna start cnbc")
				threading.Thread(target=CNBC,args=([start_date,stop_date,output_path])).start()
				
			if 4 in site:
				print("gonna start investing")
				threading.Thread(target=INVESTING,args=([start_date,stop_date,output_path])).start()
				
			if 5 in site:
				print("gonna start fidelity")
				threading.Thread(target=FIDELITY,args=([start_date,stop_date,output_path])).start()
				
			if 6 in site:
				print("gonna start yahoo")
				threading.Thread(target=YAHOO,args=([start_date,stop_date,output_path])).start()
				
				
				
		elif simultanious == 0:
			if 1 in site:
				print("gonna start zacks")
				ZACKS(start_date,stop_date,output_path)
			
			if 2 in site:
				print("gonna start bloomberg")
				BLOOMBERG(start_date,stop_date,output_path)
				
			if 3 in site:
				print("gonna start cnbc")
				CNBC(start_date,stop_date,output_path)
				
			if 4 in site:
				print("gonna start investing")
				INVESTING(start_date,stop_date,output_path)
				
			if 5 in site:
				print("gonna start fidelity")
				FIDELITY(start_date,stop_date,output_path)
				
			if 6 in site:
				print("gonna start yahoo")
				YAHOO(start_date,stop_date,output_path)
				
				
				
	elif mode_of_dates == 2:
		start_date = datetime.today().strftime("%d-%m-%Y")
		start = datetime.strptime(start_date, "%d-%m-%Y")
		finish = start + timedelta(days=days_for_mode_2)
		stop_date = finish.strftime("%d-%m-%Y")
		if simultanious == 1:
		
		
			if 1 in site:
				print("gonna start zacks")
				threading.Thread(target=ZACKS,args=([start_date,stop_date,output_path])).start()
			
			if 2 in site:
				print("gonna start bloomberg")
				threading.Thread(target=BLOOMBERG,args=([start_date,stop_date,output_path])).start()
				
			if 3 in site:
				print("gonna start cnbc")
				threading.Thread(target=CNBC,args=([start_date,stop_date,output_path])).start()
				
			if 4 in site:
				print("gonna start investing")
				threading.Thread(target=INVESTING,args=([start_date,stop_date,output_path])).start()
				
			if 5 in site:
				print("gonna start fidelity")
				threading.Thread(target=FIDELITY,args=([start_date,stop_date,output_path])).start()
				
			if 6 in site:
				print("gonna start yahoo")
				threading.Thread(target=YAHOO,args=([start_date,stop_date,output_path])).start()
				
				
				
		elif simultanious == 0:
			if 1 in site:
				print("gonna start zacks")
				ZACKS(start_date,stop_date,output_path)
			
			if 2 in site:
				print("gonna start bloomberg")
				BLOOMBERG(start_date,stop_date,output_path)
				
			if 3 in site:
				print("gonna start cnbc")
				CNBC(start_date,stop_date,output_path)
				
			if 4 in site:
				print("gonna start investing")
				INVESTING(start_date,stop_date,output_path)
				
			if 5 in site:
				print("gonna start fidelity")
				FIDELITY(start_date,stop_date,output_path)
				
			if 6 in site:
				print("gonna start yahoo")
				YAHOO(start_date,stop_date,output_path)