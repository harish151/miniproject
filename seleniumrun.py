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
    
              
    #try:
    search_box=driver.find_element(By.XPATH,"""//*[@id="review-body"]/div/ul/li[1]/a""").click()
         #search_box.submit()

         # Wait for the results to load and display the titles
         #driver.implicitly_wait(5) 
       
         #Image =>Url
    img_element=driver.find_element(By.XPATH,"""//*[@id="body"]/div/div[1]/div/div[2]/div/a/img""")
    img_url=img_element.get_attribute('src')
       
         #Heading => Product name
    products = driver.find_elements(By.XPATH, """//*[@id="body"]/div/div[1]/div/div[1]/h1""")
    product_names=[b.text for b in products[:1]]
       
          #Network =>Technology
    technologys = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[1]/tbody/tr[1]/td[2]/a""")
    technology_names=[b.text for b in technologys[:1]]

         #Launch =>Announced
    announceds = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[2]/tbody/tr[1]/td[2]""")
    announced_names=[b.text for b in announceds[:1]]
       
         #Launch =>Status
    statuss = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[2]/tbody/tr[2]/td[2]""")
    status_names=[b.text for b in statuss[:1]]
    
          #Body => Dimensions
    dimensions = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[3]/tbody/tr[1]/td[2]""")
    dimension_names=[b.text for b in dimensions[:1]]
    
          #Body => Weight
    weights = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[3]/tbody/tr[2]/td[2]""")
    weight_count=[b.text for b in weights[:1]]

          #Body => Build
    try:
           build_title=driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[3]/tbody/tr[3]/td[1]/a""")
           build_titles=[b.text for b in build_title[:1]]
           for build in build_titles:
               if build=="Build":
                   builds = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[3]/tbody/tr[3]/td[2]""")
                   build_name=[b.text for b in builds[:1]]
                   break
               else:
                    build_name="-"
           build_names=build_name
    except:
             build_name="-"
             build_names=build_name

         #Body =>SIM
    try:
           sim_title=driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[3]/tbody/tr[3]/td[1]/a""")
           sim_titles=[b.text for b in sim_title[:1]]
           for sim in sim_titles:
               if sim=="SIM":
                   sims = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[3]/tbody/tr[3]/td[2]""")
                   sim_name=[b.text for b in sims[:1]]
                   break
               else:
                   sims = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[3]/tbody/tr[4]/td[2]""")
                   sim_name=[b.text for b in sims[:1]]
           sim_names=sim_name
    except:
           sim_name="-"
           sim_names=sim_name
          
       
       #Display =>Type
    t_ypes = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[4]/tbody/tr[1]/td[2]""")
    t_ypes_names=[b.text for b in t_ypes[:1]]
    
         #Display =>Size
    sizes = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[4]/tbody/tr[2]/td[2]""")
    size_names=[b.text for b in sizes[:1]]
    
         #Display =>Resolution
    resolutions = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[4]/tbody/tr[3]/td[2]""")
    resolution_names=[b.text for b in resolutions[:1]]

         #Display =>Protection
    try: 
           protection_title=driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[4]/tbody/tr[4]/td[1]/a""")
           protection_titles=[b.text for b in protection_title[:1]]
           for protection in protection_titles: 
               if protection=="Protection":
                    protections = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[4]/tbody/tr[4]/td[2]""")
                    protections_name=[b.text for b in protections[:1]]
                    break
               else:
                    protections_name="-"
           protections_names=protections_name
    except:
            protections_name="-"
            protections_names=protections_name
    
         #Platform =>OS
    oss = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[5]/tbody/tr[1]/td[2]""")
    os_names=[b.text for b in oss[:1]]

          #Platform =>Chipset
    try:
            chipsets_title = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[5]/tbody/tr[2]/td[1]/a""")
            chipset_titles=[b.text for b in chipsets_title[:1]]
            for chip in chipset_titles:
                if chip=="Chipset": 
                    chipset = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[5]/tbody/tr[2]/td[2]""")
                    chipset_name=[b.text for b in chipset[:1]]
                else:
                    chipset_name="-" 
            chipset_names=chipset_name
    except:
            chipset_name="-"
            chipset_names=chipset_name
      
         #Platform =>CPU
    try:
            cpus_title = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[5]/tbody/tr[3]/td[1]/a""")
            cpu_titles=[b.text for b in cpus_title[:1]]
            for cpu in cpu_titles:
                if cpu=="CPU":
                    cpus=driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[5]/tbody/tr[3]/td[2]""")
                    cpu_name=[b.text for b in cpus[:1]]
                else:
                      cpu_name="-"
            cpu_names=cpu_name
    except:
            cpu_name="-"
            cpu_names=cpu_name

         #Platform =>Gpu
    try:
           gpus_title = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[5]/tbody/tr[4]/td[1]/a""")
           gpu_titles=[b.text for b in gpus_title[:1]]
           for gpu in gpu_titles:
              if gpu=="GPU":
                  gpus=driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[5]/tbody/tr[4]/td[2]""")
                  gpu_name=[b.text for b in gpus[:1]]
              else:
                  gpu_name="-"
           gpu_names=gpu_name
    except:
            gpu_name="-"
            gpu_names=gpu_name
       
         #Memory =>Card slot
    cardslots = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[6]/tbody/tr[1]/td[2]""")
    cardslot_names=[b.text for b in cardslots[:1]]
    

    camera = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[7]/tbody/tr[1]/th""")
    cameras=[b.text for b in camera[:1]]
    for cams in cameras:
         if cams !="CAMERA":
                #Memory =>Internal
                internals = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[6]/tbody/tr[2]/td[2]""")
                internal_names=[b.text for b in internals[:1]]

                #Main camera => Single
                try:
                     singles_title=driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[7]/tbody/tr[1]/td[1]/a""")
                     singles_titles=[b.text for b in singles_title[:1]]
                     for single in singles_titles:
                          if single=="Single" or single=="Quad" or single=="Triple":
                               singles = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[7]/tbody/tr[1]/td[2]""")
                               single_name=[b.text for b in singles[:1]]
                          else:
                               single_name="-"
                     single_names=single_name
                except:
                     single_name="-"
                     single_names=single_name
    
                #Main camera => Features
                try:
                     features_title=driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[7]/tbody/tr[2]/td[1]/a""")
                     features_titles=[b.text for b in features_title[:1]]
                     for features in features_titles:
                          if features=="Features":
                               featuress = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[7]/tbody/tr[2]/td[2]""")
                               features_name=[b.text for b in featuress[:1]]
                          else:
                               features_name="-"
                     features_names=features_name
                except:
                     features_name="-"
                     features_names=features_name
    
                 #Main camera => Video
                try:
                     videos_title=driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[7]/tbody/tr[3]/td[1]""")
                     videos_titles=[b.text for b in videos_title[:1]]
                     for video in videos_titles:
                          if video=="Video":
                                videos = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[7]/tbody/tr[3]/td[2]""")
                                video_name=[b.text for b in videos[:1]]
                          else:
                               video_name="-"
                     video_names=video_name
                except:
                     video_name="-"
                     video_names=video_name

    
                #Selfie Camera => Single
                try:
                     sin_gles_title = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[8]/tbody/tr[1]/td[1]""")
                     sin_gles_titles=[b.text for b in sin_gles_title[:1]]
                     for sin_gle in sin_gles_titles:
                          if sin_gle=="Single" or sin_gle=="Quad" or sin_gle=="Triple":
                                sin_gles = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[8]/tbody/tr[1]/td[2]""")
                                sin_gle_name=[b.text for b in sin_gles[:1]]
                          else:
                               sin_gle_name="-"
                     sin_gle_names=sin_gle_name
                except:
                     sin_gle_name="-"
                     sin_gle_names=sin_gle_name
    
                #Selfie Camera => Features
                try:
                     feat_uress_title = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[8]/tbody/tr[2]/td[1]""")
                     feat_uress_titles = [b.text for b in feat_uress_title[:1]]
                     for feat_ures in feat_uress_titles:
                          if feat_ures == "Features":
                               feat_uress = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[8]/tbody/tr[2]/td[2]""")
                               feat_ures_name=[b.text for b in feat_uress[:1]]
                          else:
                               feat_ures_name="-"
                     feat_ures_names=feat_ures_name
                except:
                     feat_ures_name="-"
                     feat_ures_names=feat_ures_name
    
                #Selfie Camera => Video
                try:
                    v_ideo_title = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[8]/tbody/tr[3]/td[1]""") 
                    v_ideo_titles = [b.text for b in v_ideo_title[:1]]
                    for v_ideo in v_ideo_titles:
                            if v_ideo == "Video":
                                v_ideos = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[8]/tbody/tr[3]/td[2]""")
                                v_ideo_name=[b.text for b in v_ideos[:1]]
                            else:
                                v_ideo_name ="-"
                    v_ideo_names= v_ideo_name
                except:
                     v_ideo_name ="-"
                     v_ideo_names= v_ideo_name
                     
    
                #Sound =>Loudspeaker
                loudspeakers = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[9]/tbody/tr[1]/td[2]""")
                loudspeaker_names=[b.text for b in loudspeakers[:1]]
    
                #Sound => 3.5mm Jack
                jacks = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[9]/tbody/tr[2]/td[2]""")
                jack_names=[b.text for b in jacks[:1]]
    
                #Comms => Wlan
                wlans = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[10]/tbody/tr[1]/td[2]""")
                wlan_names=[b.text for b in wlans[:1]]
    
                #Comms =>Blutooth
                blutooths = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[10]/tbody/tr[2]/td[2]""")
                blutooth_names=[b.text for b in blutooths[:1]]
    
                #Comms =>Positioning
                positionings = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[10]/tbody/tr[3]/td[2]""")
                positioning_names=[b.text for b in positionings[:1]]
    
                #Comms=>NFC
                nfcs = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[10]/tbody/tr[4]/td[2]""")
                nfc_names=[b.text for b in nfcs[:1]]
       
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
                radio_title=driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[10]/tbody/tr[5]/td[1]/a""")
                radio_titles=[b.text for b in radio_title[:1]]
                for radio in radio_titles:        
                        if radio=="Radio":
                            radios = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[10]/tbody/tr[5]/td[2]""")
                            radio_name=[b.text for b in radios[:1]]
                        else:
                            radios = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[10]/tbody/tr[6]/td[2]""")
                            radio_name=[b.text for b in radios[:1]]
                radio_names=radio_name
    
                #Comms =>USB      
                usb_title=driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[10]/tbody/tr[6]/td[1]/a""")
                usb_titles=[b.text for b in usb_title[:1]]
                for usb in usb_titles:
                        if usb=="USB":
                            usbs = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[10]/tbody/tr[6]/td[2]""")
                            usb_name=[b.text for b in usbs[:1]]
                        else:
                            usbs = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[10]/tbody/tr[7]/td[2]""")
                            usb_name=[b.text for b in usbs[:1]]
                usb_names=usb_name
    
                #Features => Sensors
                sensorss = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[11]/tbody/tr/td[2]""")
                sensors_names=[b.text for b in sensorss[:1]]
    
                #Battery =>Type
                ty_pes = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[12]/tbody/tr[1]/td[2]""")
                ty_pe_names=[b.text for b in ty_pes[:1]]
    
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
                colorss = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[13]/tbody/tr[1]/td[2]""")
                colors_names=[b.text for b in colorss[:1]]
                # Misc => Models
                try:
                        model_title=driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[13]/tbody/tr[2]/td[1]/a""")
                        model_titles=[b.text for b in model_title[:1]]
                        for models in model_titles:
                            if models=="Models":
                                model= driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[13]/tbody/tr[2]/td[2]""")
                                model_name=[b.text for b in model[:1]]
                            else:
                                model_name="-"
                        model_names=model_name
                except:
                        model_name="-"
                        model_names=model_name
      
                # Misc => SAR
                try:
                        sar_title=driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[13]/tbody/tr[3]/td[1]/a""")
                        sar_titles=[b.text for b in sar_title[:1]]
                        for sars in sar_titles:
                            if sars=="SAR":
                                sar= driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[13]/tbody/tr[3]/td[2]""")
                                sar_name=[b.text for b in sar[:1]]
                            else:
                                sar_name="-"
                        sar_names=sar_name
                except:
                        sar_name="-"
                        sar_names=sar_name


                #Misc => SAR EU
                try:
                        sar_eu_title=driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[13]/tbody/tr[3]/td[1]/a""")
                        sar_eu_titles=[b.text for b in sar_eu_title[:1]]
                        for sar_eu_s in sar_eu_titles:
                            if sar_eu_s=='SAR EU':
                                sar_eu= driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[13]/tbody/tr[3]/td[2]""")
                                sar_eu_name=[b.text for b in sar_eu[:1]]
                            else:
                                sar_eu_title2=driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[13]/tbody/tr[4]/td[1]/a""")
                                sar_eu_titles2=[b.text for b in sar_eu_title2[:1]]
                                for sar_eu_s2 in sar_eu_titles2:
                                    if sar_eu_s2=="SAR EU":
                                        sar_eu2= driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[13]/tbody/tr[4]/td[2]""")
                                        sar_eu_name2=[b.text for b in sar_eu2[:1]]
                                    else:
                                        sar_eu_name2="-"
                                        sar_eu_names2=sar_eu_name2
                                sar_eu_name=sar_eu_name2           
                        sar_eu_names=sar_eu_name
                except:
                        sar_eu_name="-"
                        sar_eu_names=sar_eu_name
        
                #Misc => Price

                try:
                        price_title = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[13]/tbody/tr[3]/td[1]/a""")
                        price_titles=[b.text for b in price_title[:1]]
                        for prices in price_titles:
                            if prices=="Price":
                                price = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[13]/tbody/tr[3]/td[2]/a""")
                                price_name=[b.text for b in price[:1]]
                                break
                            else:
                                price_title2 = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[13]/tbody/tr[4]/td[1]/a""")
                                price_titles2=[b.text for b in price_title2[:1]]
                                for prices2 in price_titles2:
                                    if prices2=="Price":
                                        price2 = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[13]/tbody/tr[4]/td[2]/a""")
                                        price_name2=[b.text for b in price2[:1]]
                                        break
                                    else:
                                        price_title3 = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[13]/tbody/tr[5]/td[1]/a""")
                                        price_titles3=[b.text for b in price_title3[:1]]
                                        for prices3 in price_titles3:
                                            if prices3=="Price":
                                                price3 = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[13]/tbody/tr[5]/td[2]""")
                                                price_name3=[b.text for b in price3[:1]] 
                                            else:
                                                price_name3="-"
                                        price_name2=price_name3
                                price_name=price_name2
                        price_Names=price_name
                        price_names=[s.replace('\u2009','') for s in price_Names]
                except:
                        price_name="-"
                        price_names=price_name
                break
         else:
                print(" ")



    for data in zip(product_names,technology_names,announced_names,status_names,dimension_names,weight_count,build_names,sim_names,t_ypes_names,size_names,
                    resolution_names,os_names,chipset_names,cpu_names,gpu_names,cardslot_names,internal_names,single_names,features_names,video_names,
                    sin_gle_names,feat_ures_names,v_ideo_names,loudspeaker_names,jack_names,wlan_names,blutooth_names,positioning_names,nfc_names,radio_names,
                    usb_names,sensors_names,ty_pe_names,charging_names,colors_names,protections_names,infrared_names,model_names,sar_names,sar_eu_names,
                    price_names):
            data
    '''except:
         data=list(range(40))
         data[0:40]=["Not Found"]*(40)
         img_url=""'''
       
       
       
    driver.quit()

    return data,img_url
