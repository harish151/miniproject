from seleniumrun2 import search
def tabledata(search_query1,search_query2):
    product_data1,img_url1 = search(search_query1)
    product_data2,image_url2 = search(search_query2)
    table_data=[{'data1':product_data1['Product Name'],'data2':product_data2['Product Name'],'data3':product_data1['Technology'],'data4':product_data2['Technology'],'data5':product_data1['Announced'],'data6':product_data2['Announced'],'data7':product_data1['Status'],'data8':product_data2['Status'],'data9':product_data1['Dimensions'],'data10':product_data2['Dimensions'],
                 
                 'data11':product_data1['Weight'],'data12':product_data2['Weight'],'data13':product_data1['Build'],'data14':product_data2['Build'],'data15':product_data1['SIM'],'data16':product_data2['SIM'],'data17':product_data1['Display Type'],'data18':product_data2['Display Type'],'data19':product_data1['Display Size'],'data20':product_data2['Display Size'],

                 'data21':product_data1['Display Resolution'],'data22':product_data2['Display Resolution'],'data23':product_data1['Display Protection'],'data24':product_data2['Display Protection'],'data25':product_data1['OS'],'data26':product_data2['OS'],'data27':product_data1['Chipset'],'data28':product_data2['Chipset'],'data29':product_data1['CPU'],'data30':product_data2['CPU'],

                 'data31':product_data1['GPU'],'data32':product_data2['GPU'],'data33':product_data1['Memory Card Slot'],'data34':product_data2['Memory Card Slot'],'data35':product_data1['Internal Memory'],'data36':product_data2['Internal Memory'],'data37':product_data1['Main Camera - Single'],'data38':product_data2['Main Camera - Single'],'data39':product_data1['Main Camera - Features'],'data40':product_data2['Main Camera - Features'],

                 'data41':product_data1['Main Camera - Video'],'data42':product_data2['Main Camera - Video'],'data43':product_data1['Selfie Camera - Single'],'data44':product_data2['Selfie Camera - Single'],'data45':product_data1['Selfie Camera - Features'],'data46':product_data2['Selfie Camera - Features'],'data47':product_data1['Selfie Camera - Video'],'data48':product_data2['Selfie Camera - Video'],'data49':product_data1['Loudspeaker'],'data50':product_data2['Loudspeaker'],

                 'data51':product_data1['3.5mm Jack'],'data52':product_data2['3.5mm Jack'],'data53':product_data1['WLAN'],'data54':product_data2['WLAN'],'data55':product_data1['Bluetooth'],'data56':product_data2['Bluetooth'],'data57':product_data1['Positioning'],'data58':product_data2['Positioning'],'data59':product_data1['NFC'],'data60':product_data2['NFC'],

                 'data61':product_data1['Infrared Port'],'data62':product_data2['Infrared Port'],'data63':product_data1['Radio'],'data64':product_data2['Radio'],'data65':product_data1['USB'],'data66':product_data2['USB'],'data67':product_data1['Sensors'],'data68':product_data2['Sensors'],'data69':product_data1['Battery Type'],'data70':product_data2['Battery Type'],

                 'data71':product_data1['Charging'],'data72':product_data2['Charging'],'data73':product_data1['Colors'],'data74':product_data2['Colors'],'data75':product_data1['Models'],'data76':product_data2['Models'],'data77':product_data1['SAR'],'data78':product_data2['SAR'],'data79':product_data1['SAR EU'],'data80':product_data2['SAR EU'],

                 'data81':product_data1['Price'],'data82':product_data2['Price'],'data83':product_data1['Review Rating'],'data84':product_data2['Review Rating'],'data85':img_url1,'data86':image_url2 

                }]
    
    #suggest value
    def rate(x,y):
        if x>="4" and y>="4":
            rating=f'Both "{product_data1['Product Name']}" and "{product_data2['Product Name']}" are Better'
        elif x>=y:
            rating=f'"{product_data1['Product Name']}" is Better'
        elif x<=y:
            rating=f'"{product_data2['Product Name']}" is Better'
        return rating
    x=product_data1['Review Rating']
    y=product_data2['Review Rating']
    
    if product_data1['Product Name'] != 'Not Found' and product_data2['Product Name'] != 'Not Found':
       review = rate(x, y)
    else:
       review = "-"

         #return suggest
    return table_data,review
