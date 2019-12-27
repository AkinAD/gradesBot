from selenium import webdriver
import os
import time

#Have a way of storing the report to a text file and find a way to compare the
# result you just returned to the last time you ran the code to see if there are new grades or nah

class gradesBot:
	def __init__(self, username=None, password=None):
		self.username = config['PPY_AUTH']['USERNAME']
		self.password = config['PPY_AUTH']['PASSWORD']

		self.all_grades_url = config['PPY_GRADE_URLS']['FULL_LIST']
		self.all_grades_url = config['PPY_GRADE_URLS']['CURR_YEAR']

		self.driver = webdriver.Chrome(config_file_path['ENVIRONMENT']['CHROMEDRIVER_PATH']

if __name__ == '__main__':
	config_file_path = './config.ini'
	logger_file_path = '.bot.log'
	config = init_config(config_file_path)
	logger = get_logger(logger_file_path)

	bot = gradesBot()
	bot.login()