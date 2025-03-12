from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def select_option(menu, option_index):
    #chooses option from dropdown menu
    menu.click()
    time.sleep(1)
    options = driver.find_elements(By.CLASS_NAME, 'option-item')
    options[option_index].click()
    time.sleep(1)

def download_csv():
    #selects download link
    download_section = driver.find_element(By.CSS_SELECTOR, 'div[style="padding-top: 7px;"]')
    download_link = download_section.find_element(By.TAG_NAME, 'a')
    download_link.click()
    time.sleep(3)

def select():
    #cycles through all options and downloads from each link
    
    #find all available dropdowns
    menus = driver.find_elements(By.CLASS_NAME, 'mt-3')

    #define market type indexes
    #上市/上櫃/公發/興櫃
    market_indices = [0, 1, 2, 3]  

    for index in market_indices:
        print(f"Processing Market Selection {index + 1}...")

        #select the market type (市場別)
        select_option(menus[0], index)

        #select the necessary year (報告年度)
        #autoselect option 2(2023年)
        select_option(menus[1], 1)

        #select company code (公司代號) 
        #selects all options 全選
        select_option(menus[3], 0)

        #query for search results
        menus[4].click()
        time.sleep(3)

        #download csv file
        download_csv()

#initialize the webdriver
options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=options)
driver.get('https://esggenplus.twse.com.tw/inquiry/report')

select()

time.sleep(10)  
driver.quit()
