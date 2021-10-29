import time;
import sys;
import itertools;
import threading;
import selenium;
from selenium import webdriver;

PATH = "C:\Program Files (x86)\chromedriver.exe"

#time to refresh page
Timer = 5 #(3 seconds)

#youtube link
link = 'ENTER LINK HERE'

#numer of views
views = 200

driver = webdriver.Chrome(PATH)
driver.get(link)

for i in range(views):
	time.sleep(Timer)
	driver.refresh()
	print("Sending views...")


