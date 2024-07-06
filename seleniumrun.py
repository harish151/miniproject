from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

def search(search_query):
    options = webdriver.ChromeOptions()
    options=Options()
    options.add_argument('--headless')  # Run in headless mode
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    driver.get("https://www.gsmarena.com/")
    


    # Enter the search query
    search_box = driver.find_element(By.XPATH, ".//input[@id='topsearch-text']")
    search_box.send_keys(search_query)  #search_query
    search_box.send_keys(Keys.ENTER)
    
              
    try:
          search_box=driver.find_element(By.XPATH,"""//*[@id="review-body"]/div/ul/li[1]/a""").click() 
    
          def check_and_replace_empty_list(input_list):
               if not input_list:
                    return "-"
               return input_list
    
          #Image =>Url
          img_element=driver.find_element(By.XPATH,"""//*[@id="body"]/div/div[1]/div/div[2]/div/a/img""")
          img_url=img_element.get_attribute('src')
       
          #Heading => Product name
          products = driver.find_elements(By.XPATH, "//h1[@data-spec='modelname']")
          product_name=[b.text for b in products[:1]]
          product_names=check_and_replace_empty_list(product_name)
       
          #Network =>Technology
          technologys = driver.find_elements(By.XPATH, "//a[@data-spec='nettech']")
          technology_name=[b.text for b in technologys[:1]]
          technology_names=check_and_replace_empty_list(technology_name)

         #Launch =>Announced
          announceds = driver.find_elements(By.XPATH, "//td[@data-spec='year']")
          announced_name=[b.text for b in announceds[:1]]
          announced_names=check_and_replace_empty_list(announced_name)
       
         #Launch =>Status
          statuss = driver.find_elements(By.XPATH, "//td[@data-spec='status']")
          status_name=[b.text for b in statuss[:1]]
          status_names=check_and_replace_empty_list(status_name)

    
          #Body => Dimensions
          dimensions = driver.find_elements(By.XPATH, "//td[@data-spec='dimensions']")
          dimension_name=[b.text for b in dimensions[:1]]
          dimension_names=check_and_replace_empty_list(dimension_name)

    
          #Body => Weight
          weights = driver.find_elements(By.XPATH, "//td[@data-spec='weight']")
          weight_counts=[b.text for b in weights[:1]]
          weight_count=check_and_replace_empty_list(weight_counts)

          #Body => Build
           
          builds = driver.find_elements(By.XPATH, "//td[@data-spec='build']")
          build_name=[b.text for b in builds[:1]]
          build_names=check_and_replace_empty_list(build_name)

         #Body =>SIM

          sims = driver.find_elements(By.XPATH, "//td[@data-spec='sim']")
          sim_name=[b.text for b in sims[:1]]
          sim_names=check_and_replace_empty_list(sim_name)

           
          #Display =>Type

          t_ypes = driver.find_elements(By.XPATH, "//td[@data-spec='displaytype']")
          t_ypes_name=[b.text for b in t_ypes[:1]]
          t_ypes_names=check_and_replace_empty_list(t_ypes_name)

 
    
         #Display =>Size

          sizes = driver.find_elements(By.XPATH, "//td[@data-spec='displaysize']")
          size_name=[b.text for b in sizes[:1]]
          size_names=check_and_replace_empty_list(size_name)

    
         #Display =>Resolution

          resolutions = driver.find_elements(By.XPATH, "//td[@data-spec='displayresolution']")
          resolution_name=[b.text for b in resolutions[:1]]
          resolution_names=check_and_replace_empty_list(resolution_name)

         #Display =>Protection

          protections = driver.find_elements(By.XPATH, "//td[@data-spec='displayprotection']")
          protections_name=[b.text for b in protections[:1]]
          protections_names=check_and_replace_empty_list(protections_name)
    
         #Platform =>OS

          oss = driver.find_elements(By.XPATH, "//td[@data-spec='os']")
          os_name=[b.text for b in oss[:1]]
          os_names=check_and_replace_empty_list(os_name)

          #Platform =>Chipset

          chipset = driver.find_elements(By.XPATH, "//td[@data-spec='chipset']")
          chipset_name=[b.text for b in chipset[:1]]
          chipset_names=check_and_replace_empty_list(chipset_name)
      
         #Platform =>CPU

          cpus=driver.find_elements(By.XPATH, "//td[@data-spec='cpu']")
          cpu_name=[b.text for b in cpus[:1]]
          cpu_names=check_and_replace_empty_list(cpu_name)

         #Platform =>Gpu

          gpus=driver.find_elements(By.XPATH, "//td[@data-spec='gpu']")
          gpu_name=[b.text for b in gpus[:1]]
          gpu_names=check_and_replace_empty_list(gpu_name)
       
          #Memory =>Card slot

          cardslots = driver.find_elements(By.XPATH, "//td[@data-spec='memoryslot']")
          cardslot_name=[b.text for b in cardslots[:1]]
          cardslot_names=check_and_replace_empty_list(cardslot_name)
        
          #Memory => Internal

          internals= driver.find_elements(By.XPATH, "//td[@data-spec='internalmemory']")
          internal_name=[b.text for b in internals[:1]]
          internal_names=check_and_replace_empty_list(internal_name)
    
          #Main camera => Single

          singles = driver.find_elements(By.XPATH, "//td[@data-spec='cam1modules']")
          single_name=[b.text for b in singles[:1]]
          single_names=check_and_replace_empty_list(single_name)
    
          #Main camera => Features

          featuress = driver.find_elements(By.XPATH, "//td[@data-spec='cam1features']")
          features_name=[b.text for b in featuress[:1]]
          features_names=check_and_replace_empty_list(features_name)
    
          #Main camera => Video

          videos = driver.find_elements(By.XPATH, "//td[@data-spec='cam1video']")
          video_name=[b.text for b in videos[:1]]
          video_names=check_and_replace_empty_list(video_name)

    
          #Selfie Camera => Single


          sin_gles = driver.find_elements(By.XPATH,"//td[@data-spec='cam2modules']")
          sin_gle_name=[b.text for b in sin_gles[:1]]
          sin_gle_names=check_and_replace_empty_list(sin_gle_name)
    
          #Selfie Camera => Features

          feat_uress = driver.find_elements(By.XPATH,"//td[@data-spec='cam2features']")
          feat_ures_name=[b.text for b in feat_uress[:1]]
          feat_ures_names=check_and_replace_empty_list(feat_ures_name)
    
          #Selfie Camera => Video

          v_ideos = driver.find_elements(By.XPATH, "//td[@data-spec='cam2video']")
          v_ideo_name=[b.text for b in v_ideos[:1]]
          v_ideo_names= check_and_replace_empty_list(v_ideo_name)
                     
    
          #Sound =>Loudspeaker

          loudspeakers = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[9]/tbody/tr[1]/td[2]""")
          loudspeaker_name=[b.text for b in loudspeakers[:1]]
          loudspeaker_names=check_and_replace_empty_list(loudspeaker_name)
    
          #Sound => 3.5mm Jack

          jacks = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[9]/tbody/tr[2]/td[2]""")
          jack_name=[b.text for b in jacks[:1]]
          jack_names=check_and_replace_empty_list(jack_name)
    
          #Comms => Wlan

          wlans = driver.find_elements(By.XPATH, "//td[@data-spec='wlan']")
          wlan_name=[b.text for b in wlans[:1]]
          wlan_names=check_and_replace_empty_list(wlan_name)
    
          #Comms =>Blutooth
 
          blutooths = driver.find_elements(By.XPATH, "//td[@data-spec='bluetooth']")
          blutooth_name=[b.text for b in blutooths[:1]]
          blutooth_names=check_and_replace_empty_list(blutooth_name)
    
          #Comms =>Positioning

          positionings = driver.find_elements(By.XPATH, "//td[@data-spec='gps']")
          positioning_name=[b.text for b in positionings[:1]]
          positioning_names=check_and_replace_empty_list(positioning_name)
    
          #Comms=>NFC

          nfcs = driver.find_elements(By.XPATH, "//td[@data-spec='nfc']")
          nfc_name=[b.text for b in nfcs[:1]]
          nfc_names=check_and_replace_empty_list(nfc_name)
       
          #Comms=>Infrared port
          
          try:
                        infrared_title=driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[10]/tbody/tr[5]/td[1]/a""")
                        infrared_titles=[b.text for b in infrared_title[:1]]
                        for infrared in infrared_titles:
                            if infrared=="Infrared port":
                                infrareds = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[10]/tbody/tr[5]/td[2]""")
                                infrared_name=[b.text for b in infrareds[:1]]
                            else:
                                infrared_name="-"
                        infrared_names=infrared_name
          except:
                        infrared_name="-"
                        infrared_names=infrared_name
       

          #Comms =>Radio

          radios = driver.find_elements(By.XPATH, "//td[@data-spec='radio']")
          radio_name=[b.text for b in radios[:1]]
          radio_names=check_and_replace_empty_list(radio_name)
    
          #Comms =>USB
    
          usbs = driver.find_elements(By.XPATH, "//td[@data-spec='usb']")
          usb_name=[b.text for b in usbs[:1]]
          usb_names=check_and_replace_empty_list(usb_name)
    
          #Features => Sensors

          sensorss = driver.find_elements(By.XPATH, "//td[@data-spec='sensors']")
          sensors_name=[b.text for b in sensorss[:1]]
          sensors_names=check_and_replace_empty_list(sensors_name)
    
          #Battery =>Type

          ty_pes = driver.find_elements(By.XPATH, "//td[@data-spec='batdescription1']")
          ty_pe_name=[b.text for b in ty_pes[:1]]
          ty_pe_names=check_and_replace_empty_list(ty_pe_name)
    
          #Battery =>Charging
          try:
                        charge_title=driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[12]/tbody/tr[2]/td[1]/a""")
                        charging_titles=[b.text for b in charge_title[:1]]
                        for charge in charging_titles:
                            if charge=="Charging":
                                charging = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[12]/tbody/tr[2]/td[2]""")
                                charging_name=[b.text for b in charging[:1]]
                            else:
                                charging_name="-"
                        charging_names=charging_name
          except:
                        charging_name="-"
                        charging_names=charging_name
    
          # Misc =>Color

          colorss = driver.find_elements(By.XPATH, "//td[@data-spec='colors']")
          colors_name=[b.text for b in colorss[:1]]
          colors_names=check_and_replace_empty_list(colors_name)
        
          # Misc => Models

          model= driver.find_elements(By.XPATH, "//td[@data-spec='models']")
          model_name=[b.text for b in model[:1]]
          model_names=check_and_replace_empty_list(model_name)
      
          # Misc => SAR

          sar= driver.find_elements(By.XPATH, "//td[@data-spec='sar-us']")
          sar_name=[b.text for b in sar[:1]]
          sar_names=check_and_replace_empty_list(sar_name)


          #Misc => SAR EU

          sar_eu= driver.find_elements(By.XPATH, "//td[@data-spec='sar-eu']")
          sar_eu_name=[b.text for b in sar_eu[:1]]          
          sar_eu_names=check_and_replace_empty_list(sar_eu_name)
        
          #Misc => Price


          price = driver.find_elements(By.XPATH, "//td[@data-spec='price']")
          price_Name=[b.text for b in price[:1]]
          price_Names=check_and_replace_empty_list(price_Name)
          price_name=[s.replace('\u2009','') for s in price_Names]
          price_names=price_name




          for data in zip(product_names,technology_names,announced_names,status_names,dimension_names,weight_count,build_names,sim_names,t_ypes_names,size_names,
                    resolution_names,os_names,chipset_names,cpu_names,gpu_names,cardslot_names,internal_names,single_names,features_names,video_names,
                    sin_gle_names,feat_ures_names,v_ideo_names,loudspeaker_names,jack_names,wlan_names,blutooth_names,positioning_names,nfc_names,radio_names,
                    usb_names,sensors_names,ty_pe_names,charging_names,colors_names,protections_names,infrared_names,model_names,sar_names,sar_eu_names,
                    price_names):
            data
    except:
         data=list(range(50))
         data[0:50]=["Not Found"]*(50)
         img_url=""
       
       
       
    driver.quit()

    return data,img_url
