def Validate_form(request_form):
    error1=''
    error2=''
    text1=request_form.get("search_query1")
    text2=request_form.get("search_query2")
    if not text1 and not text2:
        error1="*Field is required"
        error2="*Field is required"
        
    if not text1:
        error1="*Field is required"
        
    elif not text2:
        error2="*Field is required"
    
    elif text1 and text2:
        error1=""
        error2=""
        
    return error1,error2
