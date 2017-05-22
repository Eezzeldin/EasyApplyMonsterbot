import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sqlite3
import requests
from bs4 import BeautifulSoup as bs
import re
import pandas as pd



def openbrowser():
    global browser
    current_directory = os.getcwd()
    path_to_chromedriver = current_directory + '/chromedriver'
    browser = webdriver.Chrome(executable_path = path_to_chromedriver)

    
SpeedApply = browser.find_elements_by_partial_link_text ('Speed Apply') [0]
fastapply  = browser.find_elements_by_class_name('fast-apply-text')



#[str(tag.get_attribute('data-m_impr_j_jobid')) for tag in browser.find_elements_by_tag_name ('a') if str(tag.get_attribute('data-m_impr_j_jobid'))!= 'None' and str(tag.get_attribute('data-m_impr_j_jobid'))!='0' and str(tag.get_attribute('data-m_impr_j_jobid'))[0:2]== '18']
#[str(tag.get_attribute('data-m_impr_j_jobid')) for tag in browser.find_elements_by_tag_name ('a') if str(tag.get_attribute('data-m_impr_j_jobid'))!= 'None' and str(tag.get_attribute('data-m_impr_j_jobid'))!='0']
#[tag.get_attribute('href') for tag in browser.find_elements_by_tag_name ('a')]
#http://job-openings.monster.com/v2/job/View?JobID=182634071&MESCOID=1500144001001&jobPosition=3
#JobID=182634071&MESCOID=1500144001001&jobPosition=3