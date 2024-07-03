from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

def search(search_query):
    options = webdriver.ChromeOptions()
    options=Options()
    #options.add_argument('--headless')  # Run in headless mode
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    driver.get("https://www.gsmarena.com/")
    


    # Enter the search query
    search_box = driver.find_element(By.XPATH, ".//input[@id='topsearch-text']")
    search_box.send_keys(search_query)  #search_query
    search_box.send_keys(Keys.ENTER)
              
    try:
       
       search_box=driver.find_element(By.XPATH,"""//*[@id="review-body"]/div/ul/li[1]/a""").click()
       #search_box.submit()

       # Wait for the results to load and display the titles
       #driver.implicitly_wait(5) 
    

       img_element=driver.find_element(By.XPATH,"""//*[@id="body"]/div/div[1]/div/div[2]/div/a/img""")
       img_url=img_element.get_attribute('src')

       products = driver.find_elements(By.XPATH, """//*[@id="body"]/div/div[1]/div/div[1]/h1""")
       product_names=[b.text for b in products[:1]]
    

       technologys = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[1]/tbody/tr[1]/td[2]/a""")
       technology_names=[b.text for b in technologys[:1]]
    

       announceds = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[2]/tbody/tr[1]/td[2]""")
       announced_names=[b.text for b in announceds[:1]]
    

       statuss = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[2]/tbody/tr[2]/td[2]""")
       status_names=[b.text for b in statuss[:1]]
    
 
       dimensions = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[3]/tbody/tr[1]/td[2]""")
       dimension_names=[b.text for b in dimensions[:1]]
    

       weights = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[3]/tbody/tr[2]/td[2]""")
       weight_count=[b.text for b in weights[:1]]
    
     
       builds = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[3]/tbody/tr[3]/td[2]""")
       build_names=[b.text for b in builds[:1]]
    

       sims = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[3]/tbody/tr[4]/td[2]""")
       sim_names=[b.text for b in sims[:1]]
    

       t_ypes = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[4]/tbody/tr[1]/td[2]""")
       t_ypes_names=[b.text for b in t_ypes[:1]]
    

       sizes = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[4]/tbody/tr[2]/td[2]""")
       size_names=[b.text for b in sizes[:1]]
    

       resolutions = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[4]/tbody/tr[3]/td[2]""")
       resolution_names=[b.text for b in resolutions[:1]]
    

       oss = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[5]/tbody/tr[1]/td[2]""")
       os_names=[b.text for b in oss[:1]]
    

       chipsets = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[5]/tbody/tr[2]/td[2]""")
       chipset_names=[b.text for b in chipsets[:1]]
    

       cpus = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[5]/tbody/tr[3]/td[2]""")
       cpu_names=[b.text for b in cpus[:1]]
    

       gpus = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[5]/tbody/tr[4]/td[2]""")
       gpu_names=[b.text for b in gpus[:1]]
    

       cardslots = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[6]/tbody/tr[1]/td[2]""")
       cardslot_names=[b.text for b in cardslots[:1]]
    

       internals = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[6]/tbody/tr[2]/td[2]""")
       internal_names=[b.text for b in internals[:1]]
    

       singles = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[7]/tbody/tr[1]/td[2]""")
       single_names=[b.text for b in singles[:1]]
    

       featuress = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[7]/tbody/tr[2]/td[2]""")
       features_names=[b.text for b in featuress[:1]]
    

       videos = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[7]/tbody/tr[3]/td[2]""")
       video_names=[b.text for b in videos[:1]]
    

       sin_gles = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[8]/tbody/tr[1]/td[2]""")
       sin_gle_names=[b.text for b in sin_gles[:1]]
    

       feat_uress = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[8]/tbody/tr[2]/td[2]""")
       feat_ures_names=[b.text for b in feat_uress[:1]]
    

       v_ideos = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[8]/tbody/tr[3]/td[2]""")
       v_ideo_names=[b.text for b in v_ideos[:1]]
    

       loudspeakers = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[9]/tbody/tr[1]/td[2]""")
       loudspeaker_names=[b.text for b in loudspeakers[:1]]
    

       jacks = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[9]/tbody/tr[2]/td[2]""")
       jack_names=[b.text for b in jacks[:1]]
    

       wlans = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[10]/tbody/tr[1]/td[2]""")
       wlan_names=[b.text for b in wlans[:1]]
    

       blutooths = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[10]/tbody/tr[2]/td[2]""")
       blutooth_names=[b.text for b in blutooths[:1]]
    

       positionings = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[10]/tbody/tr[2]/td[2]""")
       positioning_names=[b.text for b in positionings[:1]]
    

       nfcs = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[10]/tbody/tr[4]/td[2]""")
       nfc_names=[b.text for b in nfcs[:1]]
    

       radios = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[10]/tbody/tr[5]/td[2]""")
       radio_names=[b.text for b in radios[:1]]
    

       usbs = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[10]/tbody/tr[6]/td[2]""")
       usb_names=[b.text for b in usbs[:1]]
    

       sensorss = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[11]/tbody/tr/td[2]""")
       sensors_names=[b.text for b in sensorss[:1]]
    

       ty_pes = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[12]/tbody/tr[1]/td[2]""")
       ty_pe_names=[b.text for b in ty_pes[:1]]
    

       chargings = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[12]/tbody/tr[2]/td[2]""")
       charging_names=[b.text for b in chargings[:1]]
    

       colorss = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[13]/tbody/tr[1]/td[2]""")
       colors_names=[b.text for b in colorss[:1]]

       for data in zip(product_names,technology_names,announced_names,status_names,dimension_names,weight_count,build_names,sim_names,t_ypes_names,size_names,
                    resolution_names,os_names,chipset_names,cpu_names,gpu_names,cardslot_names,internal_names,single_names,features_names,video_names,
                    sin_gle_names,feat_ures_names,v_ideo_names,loudspeaker_names,jack_names,wlan_names,blutooth_names,positioning_names,nfc_names,radio_names,
                    usb_names,sensors_names,ty_pe_names,charging_names,colors_names):
        print(data)
   
    except:
       data=list(range(40))
       data[0:40]=["Not Found"]*(40)
       img_url=""
       return data,img_url
       


    driver.quit()

    return data,img_url





    
    
