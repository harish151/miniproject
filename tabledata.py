from seleniumrun1 import perform_task
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
