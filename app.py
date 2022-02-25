import os
from random import randint
import pandas as pd
from flask import Flask, abort, request, render_template, redirect, url_for
def suggest_function(height, weight, activity):
	
	# 計算BMI
	BMI = round(weight/(height/100) ** 2, 1)
	
	# 活動量轉換成活動係數
	activity_co = 0
	if activity == '輕量':
		activity_co = 30
	elif activity == '中量':
		activity_co = 35
	else:
		activity_co = 40
	
	# 計算建議攝取熱量
	suggect_cal = weight * activity_co
	if suggect_cal < 1200:
		suggect_cal = 1200
	
	lose_weight_cal = suggect_cal - 500
	if lose_weight_cal < 1200:
		lose_weight_cal = 1200
	
	return BMI, suggect_cal, lose_weight_cal

app = Flask(__name__)


@app.route("/") #根目錄
def home():
    return render_template("home.html")

@app.route("/result", methods=["POST"])
def sendresult():
    types=["japan","korea","china","taiwan","usa","thai","southeast"]
    prefs=[]
    for type in types:
        try:
            prefs.append(request.form.get(type))
        except:
            pass
    calories = request.form.get("calories")
    price = request.form.get("price")
    options = request.form.get("options") 
    return render_template("result.html", calories=calories, prefs=prefs,price=price,options=options)

if __name__=="__main__":
    app.run()

