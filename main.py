from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__,template_folder='template')

from concurrent.futures import ThreadPoolExecutor, as_completed
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def productdata(search_query1,search_query2):
    product_data1,product_data2= perform_task(search_query1,search_query2)
    
    #suggest value
    def rate(x,y):
        if x>="4" and y>="4":
            rating=f'Both "{product_data1['data']['Product Name']}" and "{product_data2['data']['Product Name']}" are Better'
        elif x>=y:
            rating=f'"{product_data1['data']['Product Name']}" is Better'
        elif x<=y:
            rating=f'"{product_data2['data']['Product Name']}" is Better'
        return rating
    x=product_data1['data']['Review Rating']
    y=product_data2['data']['Review Rating']
    
    if product_data1['data']['Product Name'] != 'Not Found' and product_data2['data']['Product Name'] != 'Not Found':
       review = rate(x, y)
    elif product_data1['data']['Product Name'] == 'Not Found':
        review=f'"{product_data2['data']['Product Name']}" is Better'
    elif product_data2['data']['Product Name'] == 'Not Found':
        review=f'"{product_data1['data']['Product Name']}" is Better'
    else:
       review = "-"

         #return suggest
    return product_data1,product_data2,review



def perform_task(search_query1, search_query2):
    def search(search_query):
        options = Options()
        options.add_argument("--disable-images")
        #options.add_argument('--headless')  # Uncomment if you need headless mode
        options.add_argument("--disable-extensions")
        # Disable GPU acceleration
        options.add_argument("--disable-gpu")

        # Run in incognito mode
        options.add_argument("--incognito")

        # Disable browser logging
        options.add_argument("--log-level=3")  # Suppresses logging (only errors)

        # Set page load strategy to eager (loads the DOM and skips resources)
        options.set_capability('pageLoadStrategy', 'eager')

        # Disable background apps
        options.add_argument("--disable-background-timer-throttling")

        # Additional optimization arguments
        options.add_argument("--disable-software-rasterizer")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-translate")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--disable-default-apps")
        options.add_argument("--no-proxy-server")
        options.add_argument("--disable-features=IsolateOrigins,site-per-process")

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        wait = WebDriverWait(driver, 5)
        
     
        
        try:
            driver.get("https://www.gsmarena.com/")
            search_box = wait.until(EC.presence_of_element_located((By.ID, 'topsearch-text')))
            search_box.send_keys(search_query)
            search_box.send_keys(Keys.ENTER)

            first_result = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='review-body']/div/ul/li[1]/a")))
            first_result.click()

            def extract_text(xpath):
                try:
                    elements = driver.find_elements(By.XPATH, xpath)
                    return [elem.text for elem in elements] or ["-"]
                except Exception as e:
                    print(f"Error extracting text from XPath '{xpath}': {e}")
                    return ["-"]
                
            def check_and_replace_empty_list(input_list):
                if not input_list:
                    return "-"
                return input_list[0]
                
            def extract_review(xpath):
                try:
                    elements = driver.find_elements(By.XPATH, xpath)
                    return [elem.text for elem in elements] or ["3.8"]
                except Exception as e:
                    print(f"Error extracting text from XPath '{xpath}': {e}")
                    return ["3.8"]

            # Extract image URL
            img_url = driver.find_element(By.XPATH, "//*[@id='body']/div/div[1]/div/div[2]/div/a/img").get_attribute('src')

            # Dictionary for fields to be extracted
            fields = {
                "Product Name": "//h1[@data-spec='modelname']",
                "Technology": "//a[@data-spec='nettech']",
                "Announced": "//td[@data-spec='year']",
                "Status": "//td[@data-spec='status']",
                "Dimensions": "//td[@data-spec='dimensions']",
                "Weight": "//td[@data-spec='weight']",
                "Build": "//td[@data-spec='build']",
                "SIM": "//td[@data-spec='sim']",
                "Display Type": "//td[@data-spec='displaytype']",
                "Size": "//td[@data-spec='displaysize']",
                "Resolution": "//td[@data-spec='displayresolution']",
                "Protection": "//td[@data-spec='displayprotection']",
                "OS": "//td[@data-spec='os']",
                "Chipset": "//td[@data-spec='chipset']",
                "CPU": "//td[@data-spec='cpu']",
                "GPU": "//td[@data-spec='gpu']",
                "Card Slot": "//td[@data-spec='memoryslot']",
                "Internal Memory": "//td[@data-spec='internalmemory']",
                "Main Camera Modules": "//td[@data-spec='cam1modules']",
                "Main Camera Features": "//td[@data-spec='cam1features']",
                "Main Camera Video": "//td[@data-spec='cam1video']",
                "Secondary Camera Modules": "//td[@data-spec='cam2modules']",
                "Secondary Camera Features": "//td[@data-spec='cam2features']",
                "Secondary Camera Video": "//td[@data-spec='cam2video']",
                "Loudspeaker": "//*[@id='specs-list']/table[9]/tbody/tr[1]/td[2]",
                "Jack": "//*[@id='specs-list']/table[9]/tbody/tr[2]/td[2]",
                "WLAN": "//td[@data-spec='wlan']",
                "Bluetooth": "//td[@data-spec='bluetooth']",
                "Positioning": "//td[@data-spec='gps']",
                "NFC": "//td[@data-spec='nfc']",
                "Radio": "//td[@data-spec='radio']",
                "USB": "//td[@data-spec='usb']",
                "Sensors": "//td[@data-spec='sensors']",
                "Battery Description": "//td[@data-spec='batdescription1']",
                "Colors": "//td[@data-spec='colors']",
                "Models": "//td[@data-spec='models']",
                "SAR US": "//td[@data-spec='sar-us']",
                "SAR EU": "//td[@data-spec='sar-eu']",
                "Price": "//td[@data-spec='price']"
            }

            # Collect data
            data = {field: extract_text(xpath)[0] for field, xpath in fields.items()}

            # Clean price data
            if data.get("Price"):
                data["Price"] = data["Price"].replace('\u2009', '')

            infrared_title=driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[10]/tbody/tr[5]/td[1]/a""")
            infrared_titles=[b.text for b in infrared_title[:1]]
            for infrared in infrared_titles:
                            if infrared=="Infrared port":
                                infrareds = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[10]/tbody/tr[5]/td[2]""")
                                infrared_name=[b.text for b in infrareds[:1]]
                            else:
                                infrared_name="-"
            data['Infrared']=check_and_replace_empty_list(infrared_name)

            charge_title=driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[12]/tbody/tr[2]/td[1]/a""")
            charging_titles=[b.text for b in charge_title[:1]]
            for charge in charging_titles:
                            if charge=="Charging":
                                charging = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[12]/tbody/tr[2]/td[2]""")
                                charging_name=[b.text for b in charging[:1]]
                            else:
                                charging_name="-"
            data['Charging']=check_and_replace_empty_list(charging_name)

            # Review rating
            review_box = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='body']/div/div[1]/div/div[3]/ul/li[1]/a")))
            review_box.click()
            data["Review Rating"] = extract_review("//span[@class='score']")[0]

        except Exception as e:
            keys=['Technology','Announced','Status','Dimensions',
               'Weight','Build','SIM','Display Type','Display Size',
               'Display Resolution','Display Protection','OS','Chipset','CPU',
               'GPU','Memory Card Slot','Internal Memory','Main Camera - Single','Main Camera - Features',
               'Main Camera - Video','Selfie Camera - Single','Selfie Camera - Features','Selfie Camera - Video','Loudspeaker',
               '3.5mm Jack','WLAN','Bluetooth','Positioning','NFC',
               'Infrared Port','Radio','USB','Sensors','Battery Type',
               'Charging','Colors','Models','SAR','SAR EU','Price','Review Rating']
            data['Product Name']="Not Found"
            for key in keys:
                data[f'{key}']="-"
        
        finally:
            driver.quit()
        
        return data, img_url

    # Define the search queries
    tasks = [search_query1, search_query2]

    # Run tasks in parallel and store results
    results = {}
    with ThreadPoolExecutor(max_workers=2) as executor:
        future_to_query = {executor.submit(search, query): query for query in tasks}
        for future in as_completed(future_to_query):
            query = future_to_query[future]
            try:
                data, img_url = future.result()
                results[query] = {"data": data, "img_url": img_url}
            except Exception as e:
                print(f"Task generated an exception: {e}")


    return results.get(search_query1),results.get(search_query2)



@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
            search_query1,search_query2 = request.form.get('search_query1'),request.form.get('search_query2')
            data1,data2,suggest=productdata(search_query1,search_query2)
            return render_template('project.html',data1=data1,data2=data2,suggest=suggest)
    return render_template('project.html')

if __name__=='__main__':
    app.run(debug=True)
    
