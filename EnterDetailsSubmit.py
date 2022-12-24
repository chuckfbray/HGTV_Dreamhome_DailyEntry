############################################################################
###                                                                     ####
### Title:  Enter Food Network and HGTV Dream Home Sweepstakes          ####
### Author: Charlie Bray                                                ####
### Date:   12/24/2022                                                  ####
###                                                                     ####
############################################################################

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


### Landing pages; form fills
#HGTV = 'https://www.hgtv.com/sweepstakes/hgtv-dream-home/sweepstakes'
HGTV = 'https://xd.wayin.com/display/container/dc/997d3737-1b52-47af-837d-e7330ee64f30/entry?source=hgtv'
#foodnet = 'https://www.foodnetwork.com/sponsored/sweepstakes/hgtv-dream-home-sweepstakes'
foodnet = 'https://xd.wayin.com/display/container/dc/aec2d57e-bfc8-43c2-bd78-d41493e796c0?source=food network'


### set download directory
chrome_options = webdriver.ChromeOptions()
prefs = {'download.default_directory' : 'C:\\Users\\cache\\OneDrive\\Documents\\HMS\\Web_Scraping',
         'download.prompt_for_download': False,
         'download.directory_upgrade': True,
         'safebrowsing.enabled': True}
chrome_options.add_experimental_option('prefs', prefs)


for site in [foodnet, HGTV]:
    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='C:/Users/cache/OneDrive/Documents/HMS/Web_Scraping/chromedriver.exe')
    driver.get()
    time.sleep(15)
    # content = driver.page_source
    # driver.quit()
    
    
    ### pass info to landing page form
    inputElement = driver.find_element_by_id("xReturningUserEmail")
    inputElement.send_keys('[ENTER EMAIL]')
    inputElement.send_keys(Keys.ENTER)
    
    
    ### Select element by id
    
    # name details entry
    inputElement = driver.find_element_by_id("name_Firstname")
    inputElement.send_keys('[ENTER FIRST NAME]')
    inputElement = driver.find_element_by_id("name_Lastname")
    inputElement.send_keys('[ENTER LAST NAME]')
    
    # address details entry
    inputElement = driver.find_element_by_id("address_Address1")
    inputElement.send_keys('[ENTER STREET ADDRESS]')
    inputElement = driver.find_element_by_id("address_City")
    inputElement.send_keys('[ENTER CITY OF RESIDENCE]')
    inputElement = driver.find_element_by_id("address_State")
    inputElement.send_keys('[ENTER STATE OF RESIDENCE]')
    inputElement = driver.find_element_by_id("address_Zip")
    inputElement.send_keys('[ENTER ZIP CODE OF RESIDENCE]')
    
    # birth day details entry
    inputElement = driver.find_element_by_id("date_of_birth_month")
    inputElement.send_keys('[ENTER BIRTH MONTH]')
    inputElement = driver.find_element_by_id("date_of_birth_day")
    inputElement.send_keys('[ENTER BIRTH MONTH DAY]')
    inputElement = driver.find_element_by_id("date_of_birth_year")
    inputElement.send_keys('[ENTER BIRTH YEAR]')
      
    
    ### form submit
    #inputElement.send_keys(Keys.ENTER)
    inputElement = driver.find_element_by_id("xSubmitContainer")
    inputElement.click()

# FIN
