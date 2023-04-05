# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 02:11:45 2023

@author: Raghul S
"""
from preprocessing import target, Dict, cols, unique_values, scaler, label_encoder

cols.remove(target)

# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk
import pickle

# Creating the main window
root = tk.Tk()
root.title("Skilled-based Career Recommendation System")

# Creating a canvas with a scrollbar
canvas = tk.Canvas(root, width=500, height=500)
scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollable_frame = ttk.Frame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

title = ttk.Label(scrollable_frame, font=("Arial", 20), text="Skilled-based Career Recommendation System").grid(row=0, column=25, padx=10, pady=50)

# Adding the form elements to the scrollable frame
entry={}
label={}
j=1
for i in cols:
    label[i] = ttk.Label(scrollable_frame, text=i+" : ")
#    entry[i] = ttk.Entry(scrollable_frame)
    entry[i] = ttk.Combobox(scrollable_frame, values=unique_values[i])
    label[i].grid(row=j, column=0, padx=10, pady=10, sticky="w")
    entry[i].grid(row=j, column=1, padx=10, pady=10, sticky="ew")
    j+=1
    
#temp = Dict[target];
#temp = {v: k for k, v in temp.items()}
#Dict.pop(target);

def submit_form():
    args={}
    for i in cols:
        if(i not in list(Dict.keys())):
             args[i]=int(entry[i].get().strip())
        else:
            args[i]=entry[i].get().strip()

        print(args[i])
          
    for i in list(Dict.keys()):
        args[i] = Dict[i][args[i]]
        print(args[i])
        
    tk.messagebox.showinfo("Success", "Form submitted successfully!")
    
    with open("./models/rf_model.pkl","rb") as f:
        mp = pickle.load(f)
    
    value =  mp.predict(scaler.transform([list(args.values())]))
    print(value)
    
    #predicted_career=temp[round(value[0])];
    predicted_career = label_encoder.inverse_transform([round(value[0])])
    print("Recommended career is "+predicted_career[0])
    output_label.config(text="Recommended career is "+predicted_career[0])

        
    
submit_button = ttk.Button(scrollable_frame, text="Submit", command=submit_form)
submit_button.grid(row=j+1, column=1, padx=10, pady=10, sticky="e")

output_label = ttk.Label(scrollable_frame, font=("Arial", 18), text="")
#output_label.configure(fg="(30, 166, 100)")
output_label.grid(row=j+2, column=25, padx=10, pady=30, sticky="w")

# Packing the scrollbar and canvas into the main window
scrollbar.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)

# Run the main loop
root.mainloop()

