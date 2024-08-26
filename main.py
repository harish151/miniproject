from flask import Flask, render_template, request, redirect, url_for
from tabledata import productdata
app = Flask(__name__,template_folder='template')


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
            search_query1,search_query2 = request.form.get('search_query1'),request.form.get('search_query2')
            data1,data2,suggest=productdata(search_query1,search_query2)
            return render_template('project.html',data1=data1,data2=data2,suggest=suggest)
    return render_template('project.html')

if __name__=='__main__':
    app.run(debug=True)
    
