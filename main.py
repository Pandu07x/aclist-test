from flask import Flask,render_template,request,redirect
from pymongo import *

app=Flask(__name__,template_folder="template")
mycli=MongoClient("mongodb://localhost:27017")
mydba=mycli['AC']
mytba=mydba["list"]

@app.route('/')
def home():

    data = mytba.find()
    return render_template("index.html",data=data)



@app.route('/added',methods=['POST'])
def add():
    Cname = request.form['cname']
    acmodel = request.form['model']
    shop = request.form['shop']
    acprice = request.form['price']
    install = request.form['install']
    offer = request.form['offer']
    totalprice=int(acprice)+int(install)
    rec = {
            "cname": Cname,
            "acmodel": acmodel,
            "shop": shop,
            "acprice": acprice,
            "install": install,
            "offer": offer,
            "totalprice": totalprice
        }
    mytba.insert_one(rec)

    return redirect('/')





if __name__=="__main__":
    app.run(debug=True)

