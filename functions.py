from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


#list of functions :
#-clean_by() :
#
#       input :text,text
#       output :a list that is cleaned and is more readable
#
#-create_driver() : 
#
#       input : url, path 
#       output : driver
#  



#this will split a text with a specific delimiter
def clean_by(t,x):
    l=t.split(x)
    return l




#this will create a chrome driver 
def create_driver(url,path):
    options=Options()
    options.add_argument("--headless")
    options.add_argument("--log-level=3")
    service_0=Service(executable_path=path)
    driver=webdriver.Chrome(service=service_0,options=options)
    driver.get(url)
    return driver

