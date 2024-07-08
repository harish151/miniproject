from seleniumrun import search
def tabledata(search_query1,search_query2):
    product_data1,img_url1 = search(search_query1)
    product_data2,image_url2 = search(search_query2)
    table_data=[{'data1':product_data1[0],'data2':product_data2[0],'data3':product_data1[1],'data4':product_data2[1],'data5':product_data1[2],'data6':product_data2[2],'data7':product_data1[3],'data8':product_data2[3],'data9':product_data1[4],'data10':product_data2[4],
                 'data11':product_data1[5],'data12':product_data2[5],'data13':product_data1[6],'data14':product_data2[6],'data15':product_data1[7],'data16':product_data2[7],'data17':product_data1[8],'data18':product_data2[8],'data19':product_data1[9],'data20':product_data2[9],
                 'data21':product_data1[10],'data22':product_data2[10],'data23':product_data1[11],'data24':product_data2[11],'data25':product_data1[12],'data26':product_data2[12],'data27':product_data1[13],'data28':product_data2[13],'data29':product_data1[14],'data30':product_data2[14],
                 'data31':product_data1[15],'data32':product_data2[15],'data33':product_data1[16],'data34':product_data2[16],'data35':product_data1[17],'data36':product_data2[17],'data37':product_data1[18],'data38':product_data2[18],'data39':product_data1[19],'data40':product_data2[19],
                 'data41':product_data1[20],'data42':product_data2[20],'data43':product_data1[21],'data44':product_data2[21],'data45':product_data1[22],'data46':product_data2[22],'data47':product_data1[23],'data48':product_data2[23],'data49':product_data1[24],'data50':product_data2[24],
                 'data51':product_data1[25],'data52':product_data2[25],'data53':product_data1[26],'data54':product_data2[26],'data55':product_data1[27],'data56':product_data2[27],'data57':product_data1[28],'data58':product_data2[28],'data59':product_data1[29],'data60':product_data2[29],
                 'data61':product_data1[30],'data62':product_data2[30],'data63':product_data1[31],'data64':product_data2[31],'data65':product_data1[32],'data66':product_data2[32],'data67':product_data1[33],'data68':product_data2[33],'data69':product_data1[34],'data70':product_data2[34],
                 'data71':product_data1[35],'data72':product_data2[35],'data73':product_data1[36],'data74':product_data2[36],'data75':product_data1[37],'data76':product_data2[37],'data77':product_data1[38],'data78':product_data2[38],'data79':product_data1[39],'data80':product_data2[39],
                 'data81':product_data1[40],'data82':product_data2[40],'data83':img_url1,'data84':image_url2 
                }]
    suggest=product_data1[0]
    return table_data,suggest
