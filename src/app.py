# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 20:16:08 2023

@author: Raghul S
"""

from preprocessing import target, Dict, cols, unique_values, scaler, label_encoder
from flask import Flask, render_template, request
import pickle
cols.remove(target)

app = Flask(__name__)

@app.route('/')
def home():
    
    return render_template('form.html', cols = cols, unique_values = unique_values)

@app.route('/submit', methods=['POST'])
def register():

    args ={}
    for i in cols:
        if(i not in list(Dict.keys())):
             args[i]=int(request.form[i].strip())
        else:
            args[i]=request.form[i].strip()
            
    for i in list(Dict.keys()):
            args[i] = Dict[i][args[i]]
            print(args[i])       
        
    with open("./models/rf_model.pkl","rb") as f:
            mp = pickle.load(f)
        
    value =  mp.predict(scaler.transform([list(args.values())]))
    print(value)
        
    predicted_career = label_encoder.inverse_transform([round(value[0])])
    print("Recommended career is "+predicted_career[0])
            
    return render_template('success.html', predicted_career=predicted_career)

if __name__ == '__main__':
    app.run(debug=True)



