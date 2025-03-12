#import packages
from bs4 import BeautifulSoup
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

#initialize the webdriver
options = webdriver.ChromeOptions()
#remember to use double hyphens when setting options for selenium (--)
#options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
#service = Service("C:/Users/research1/OneDrive - 碁石智庫股份有限公司/Keystone Intern/Sean Milligan/python_practice/chromedriver.exe")
#driver = webdriver.Chrome(service=service, options=options)
driver = webdriver.Chrome(options=options)

#open the desired page
url = 'https://esggenplus.twse.com.tw/inquiry/report'
#url = 'https://www.yahoo.com.tw'
driver.get(url)

def select():
    #find and click market dropdown to establish options
    #open first menu
    menus = driver.find_elements(By.CLASS_NAME, 'mt-3')
    menu1_dropdownbutton = menus[0]
    menu1_dropdownbutton.click()
    time.sleep(1)

    #select first option in series
    market_options = driver.find_elements(By.CLASS_NAME, 'option-item')
    shang_shi = market_options[0]
    shang_shi.click()
    time.sleep(1)

    #find and click year dropdown to establish options
    menu2_dropdownbutton = menus[1]
    menu2_dropdownbutton.click()
    time.sleep(1)

    #select second option in series (2023年)
    year_options = driver.find_elements(By.CLASS_NAME, 'option-item')
    lastyear = year_options[1]
    lastyear.click()
    time.sleep(1)

    #find and click company code dropdown to establish options
    menu3_dropdownbutton = menus[3]
    menu3_dropdownbutton.click()
    time.sleep(1)

    #select first option in series (全選)
    code_options = driver.find_elements(By.CLASS_NAME, 'option-item')
    select_all = code_options[0]
    select_all.click()
    time.sleep(1)

    #click button to query options
    search_button = menus[4]
    search_button.click()
    time.sleep(3)

    #download first file 
    download_section = driver.find_element(By.CSS_SELECTOR, 'div[style="padding-top: 7px;"]')
    download1 = download_section.find_element(By.TAG_NAME, 'a')
    download1.click()
    time.sleep(3)

    #reselect market selection 1
    menu1_dropdownbutton.click()
    time.sleep(1)
    #choose shang gui option
    market_options = driver.find_elements(By.CLASS_NAME, 'option-item')
    shang_gui = market_options[1]
    shang_gui.click()
    time.sleep(1)

    #reselect company code dropdown menu
    menu3_dropdownbutton.click()
    time.sleep(1)
    #choose all options
    code_options = driver.find_elements(By.CLASS_NAME, 'option-item')
    select_all = code_options[0]
    select_all.click()
    time.sleep(1)

    #click button to query 2nd round of options
    search_button = menus[4]
    search_button.click()
    time.sleep(3)

    #download 2nd file 
    download2 = download_section.find_element(By.TAG_NAME, 'a')
    download2.click()
    time.sleep(3)

    #reselect market selection 2
    menu1_dropdownbutton.click()
    time.sleep(1)
    #choose gongfa option
    market_options = driver.find_elements(By.CLASS_NAME, 'option-item')
    gongfa = market_options[2]
    gongfa.click()

    #reselect company code dropdown menu
    menu3_dropdownbutton.click()
    time.sleep(1)
    #choose all options
    code_options = driver.find_elements(By.CLASS_NAME, 'option-item')
    select_all = code_options[0]
    select_all.click()
    time.sleep(1)

    #click button to query 3rd round of options
    search_button = menus[4]
    search_button.click()
    time.sleep(3)

    #download 3rd file 
    download3 = download_section.find_element(By.TAG_NAME, 'a')
    download3.click()
    time.sleep(3)

    #reselect market selection 3
    menu1_dropdownbutton.click()
    time.sleep(1)
    #choose xing_gui option
    market_options = driver.find_elements(By.CLASS_NAME, 'option-item')
    xing_gui = market_options[3]
    xing_gui.click()

    #reselect company code dropdown menu
    menu3_dropdownbutton.click()
    time.sleep(1)
    #choose all options
    code_options = driver.find_elements(By.CLASS_NAME, 'option-item')
    select_all = code_options[0]
    select_all.click()
    time.sleep(1)

    #click button to query 4th round of options
    search_button = menus[4]
    search_button.click()
    time.sleep(3)

    #download 4th file 
    download4 = download_section.find_element(By.TAG_NAME, 'a')
    download4.click()
    time.sleep(3)

select()

time.sleep(10)






