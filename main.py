from selenium import webdriver
from datetime import datetime
import time
# import texteditor
import configparser
from utility_methods.utility_methods import *
import urllib.request

#Have a way of storing the report to a text file and find a way to compare the
# result you just returned to the last time you ran the code to see if there are new grades or nah

class gradesBot:
	def __init__(self, username=None, password=None):
		self.username = config['PPY_AUTH']['USERNAME']
		self.password = config['PPY_AUTH']['PASSWORD']

		self.all_grades_url = config['PPY_GRADE_URLS']['FULL_LIST']
		self.curr_year_url = config['PPY_GRADE_URLS']['CURR_YEAR']

		self.driver = webdriver.Chrome(config['ENVIRONMENT']['CHROMEDRIVER_PATH'])

	def login(self):
		self.driver.get(self.all_grades_url)

		login_btn = self.driver.find_element_by_xpath("//input[@value='Login']")
		username_input =  self.driver.find_element_by_xpath("//input[@name='mli']")
		password_input = self.driver.find_element_by_xpath("//input[@name='password']")

		username_input.send_keys(self.username)
		password_input.send_keys(self.password)
		login_btn.click()
		time.sleep(3)

	def getGrades(self):
		self.tableOfGrades = self.driver.find_elements_by_xpath("//table[@class='bodytext']")[0]
		
		now = datetime.now() # current date and time
		date_time = now.strftime("%A %B %d %I:%M %P")
		filename = 'Grades_checked_on_{}.txt'.format(date_time)
		f = open(filename, "w+")
		for i in self.tableOfGrades.find_elements_by_xpath(".//tr"):
			f.write('{}\n'.format(i.text))
			print('{}'.format(i.text))
		f.close()
		#text = texteditor.open(filename) """ automatically open the file afterwards"""
	

if __name__ == '__main__':
	config_file_path = './config.ini'
	logger_file_path = '.bot.log'
	config = init_config(config_file_path)
	logger = get_logger(logger_file_path)

	bot = gradesBot()
	bot.login()
	bot.getGrades()
