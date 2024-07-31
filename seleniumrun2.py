from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def search(search_query):
    options = webdriver.ChromeOptions()
    options=Options()
    #options.add_argument('--headless')  # Run in headless mode
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.gsmarena.com/")
    
    # Enter the search query
    search_box = driver.find_element(By.XPATH, ".//input[@id='topsearch-text']")
    search_box.send_keys(search_query)
    search_box.send_keys(Keys.ENTER)
    
    result_data = {}  # Dictionary to store all data
    img_url=" "
    
    try:
        # Click on the first result
        driver.find_element(By.XPATH, """//*[@id="review-body"]/div/ul/li[1]/a""").click()

        def check_and_replace_empty_list(input_list):
            if not input_list:
                return "-"
            return input_list[0]
        
        def check_and_replace_review_rate(input_list):
            if not input_list:
                return "3.9"
            return input_list[0]

        # Extracting various details
        img_url = driver.find_element(By.XPATH, """//*[@id="body"]/div/div[1]/div/div[2]/div/a/img""").get_attribute('src')
        result_data['Product Name'] = check_and_replace_empty_list([b.text for b in driver.find_elements(By.XPATH, "//h1[@data-spec='modelname']")])
        result_data['Technology'] = check_and_replace_empty_list([b.text for b in driver.find_elements(By.XPATH, "//a[@data-spec='nettech']")])
        result_data['Announced'] = check_and_replace_empty_list([b.text for b in driver.find_elements(By.XPATH, "//td[@data-spec='year']")])
        result_data['Status'] = check_and_replace_empty_list([b.text for b in driver.find_elements(By.XPATH, "//td[@data-spec='status']")])
        result_data['Dimensions'] = check_and_replace_empty_list([b.text for b in driver.find_elements(By.XPATH, "//td[@data-spec='dimensions']")])
        result_data['Weight'] = check_and_replace_empty_list([b.text for b in driver.find_elements(By.XPATH, "//td[@data-spec='weight']")])
        result_data['Build'] = check_and_replace_empty_list([b.text for b in driver.find_elements(By.XPATH, "//td[@data-spec='build']")])
        result_data['SIM'] = check_and_replace_empty_list([b.text for b in driver.find_elements(By.XPATH, "//td[@data-spec='sim']")])
        result_data['Display Type'] = check_and_replace_empty_list([b.text for b in driver.find_elements(By.XPATH, "//td[@data-spec='displaytype']")])
        result_data['Display Size'] = check_and_replace_empty_list([b.text for b in driver.find_elements(By.XPATH, "//td[@data-spec='displaysize']")])
        result_data['Display Resolution'] = check_and_replace_empty_list([b.text for b in driver.find_elements(By.XPATH, "//td[@data-spec='displayresolution']")])
        result_data['Display Protection'] = check_and_replace_empty_list([b.text for b in driver.find_elements(By.XPATH, "//td[@data-spec='displayprotection']")])
        result_data['OS'] = check_and_replace_empty_list([b.text for b in driver.find_elements(By.XPATH, "//td[@data-spec='os']")])
        result_data['Chipset'] = check_and_replace_empty_list([b.text for b in driver.find_elements(By.XPATH, "//td[@data-spec='chipset']")])
        result_data['CPU'] = check_and_replace_empty_list([b.text for b in driver.find_elements(By.XPATH, "//td[@data-spec='cpu']")])
        result_data['GPU'] = check_and_replace_empty_list([b.text for b in driver.find_elements(By.XPATH, "//td[@data-spec='gpu']")])
        result_data['Memory Card Slot'] = check_and_replace_empty_list([b.text for b in driver.find_elements(By.XPATH, "//td[@data-spec='memoryslot']")])
        result_data['Internal Memory'] = check_and_replace_empty_list([b.text for b in driver.find_elements(By.XPATH, "//td[@data-spec='internalmemory']")])
        result_data['Main Camera - Single'] = check_and_replace_empty_list([b.text for b in driver.find_elements(By.XPATH, "//td[@data-spec='cam1modules']")])
        result_data['Main Camera - Features'] = check_and_replace_empty_list([b.text for b in driver.find_elements(By.XPATH, "//td[@data-spec='cam1features']")])
        result_data['Main Camera - Video'] = check_and_replace_empty_list([b.text for b in driver.find_elements(By.XPATH, "//td[@data-spec='cam1video']")])
        result_data['Selfie Camera - Single'] = check_and_replace_empty_list([b.text for b in driver.find_elements(By.XPATH, "//td[@data-spec='cam2modules']")])
        result_data['Selfie Camera - Features'] = check_and_replace_empty_list([b.text for b in driver.find_elements(By.XPATH, "//td[@data-spec='cam2features']")])
        result_data['Selfie Camera - Video'] = check_and_replace_empty_list([b.text for b in driver.find_elements(By.XPATH, "//td[@data-spec='cam2video']")])
        result_data['Loudspeaker'] = check_and_replace_empty_list([b.text for b in driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[9]/tbody/tr[1]/td[2]""")])
        result_data['3.5mm Jack'] = check_and_replace_empty_list([b.text for b in driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[9]/tbody/tr[2]/td[2]""")])
        result_data['WLAN'] = check_and_replace_empty_list([b.text for b in driver.find_elements(By.XPATH, "//td[@data-spec='wlan']")])
        result_data['Bluetooth'] = check_and_replace_empty_list([b.text for b in driver.find_elements(By.XPATH, "//td[@data-spec='bluetooth']")])
        result_data['Positioning'] = check_and_replace_empty_list([b.text for b in driver.find_elements(By.XPATH, "//td[@data-spec='gps']")])
        result_data['NFC'] = check_and_replace_empty_list([b.text for b in driver.find_elements(By.XPATH, "//td[@data-spec='nfc']")])

        #result_data['Infrared Port'] = check_and_replace_empty_list([b.text for b in driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[10]/tbody/tr[5]/td[2]""")])
        # infrared port
        infrared_title=driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[10]/tbody/tr[5]/td[1]/a""")
        infrared_titles=[b.text for b in infrared_title[:1]]
        for infrared in infrared_titles:
                            if infrared=="Infrared port":
                                infrareds = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[10]/tbody/tr[5]/td[2]""")
                                infrared_name=[b.text for b in infrareds[:1]]
                            else:
                                infrared_name="-"
        result_data['Infrared Port']=check_and_replace_empty_list(infrared_name)

        result_data['Radio'] = check_and_replace_empty_list([b.text for b in driver.find_elements(By.XPATH, "//td[@data-spec='radio']")])
        result_data['USB'] = check_and_replace_empty_list([b.text for b in driver.find_elements(By.XPATH, "//td[@data-spec='usb']")])
        result_data['Sensors'] = check_and_replace_empty_list([b.text for b in driver.find_elements(By.XPATH, "//td[@data-spec='sensors']")])
        result_data['Battery Type'] = check_and_replace_empty_list([b.text for b in driver.find_elements(By.XPATH, "//td[@data-spec='batdescription1']")])

        #result_data['Charging'] = check_and_replace_empty_list([b.text for b in driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[12]/tbody/tr[2]/td[2]""")])
        #battery charging
        
        charge_title=driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[12]/tbody/tr[2]/td[1]/a""")
        charging_titles=[b.text for b in charge_title[:1]]
        for charge in charging_titles:
                            if charge=="Charging":
                                charging = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[12]/tbody/tr[2]/td[2]""")
                                charging_name=[b.text for b in charging[:1]]
                            else:
                                charging_name="-"
        result_data['Charging']=check_and_replace_empty_list(charging_name)

        result_data['Colors'] = check_and_replace_empty_list([b.text for b in driver.find_elements(By.XPATH, "//td[@data-spec='colors']")])
        result_data['Models'] = check_and_replace_empty_list([b.text for b in driver.find_elements(By.XPATH, "//td[@data-spec='models']")])
        result_data['SAR'] = check_and_replace_empty_list([b.text for b in driver.find_elements(By.XPATH, "//td[@data-spec='sar-us']")])
        result_data['SAR EU'] = check_and_replace_empty_list([b.text for b in driver.find_elements(By.XPATH, "//td[@data-spec='sar-eu']")])
        result_data['Price'] = check_and_replace_empty_list([b.text for b in driver.find_elements(By.XPATH, "//td[@data-spec='price']")])
        
        # Extract review rating
        driver.find_element(By.XPATH, """//*[@id="body"]/div/div[1]/div/div[3]/ul/li[1]/a""").click()
        result_data['Review Rating'] = check_and_replace_review_rate([b.text for b in driver.find_elements(By.XPATH, "//span[@class='score']")])

    except:
        keys=['Technology','Announced','Status','Dimensions',
               'Weight','Build','SIM','Display Type','Display Size',
               'Display Resolution','Display Protection','OS','Chipset','CPU',
               'GPU','Memory Card Slot','Internal Memory','Main Camera - Single','Main Camera - Features',
               'Main Camera - Video','Selfie Camera - Single','Selfie Camera - Features','Selfie Camera - Video','Loudspeaker',
               '3.5mm Jack','WLAN','Bluetooth','Positioning','NFC',
               'Infrared Port','Radio','USB','Sensors','Battery Type',
               'Charging','Colors','Models','SAR','SAR EU','Price','Review Rating']
        result_data['Product Name']="Not Found"
        for key in keys:
            result_data[f'{key}']="-"
            
        
    return result_data,img_url
