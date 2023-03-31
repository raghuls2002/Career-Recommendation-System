# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 02:11:45 2023

@author: Raghul S
"""
qList = ['Logical quotient rating',
 'hackathons',
 'coding skills rating',
 'public speaking points',
 'self-learning capability?_code',
 'Extra-courses did_code',
 'certifications_code',
 'workshops_code',
 'reading and writing skills_code',
 'memory capability score_code',
 'Interested subjects_code',
 'interested career area _code',
 'Type of company want to settle in?_code',
 'Taken inputs from seniors or elders_code',
 'Interested Type of Books_code',
 'Management or Technical_code',
 'hard/smart worker_code',
 'worked in teams ever?_code',
 'Introvert_code']

Dict = {'self-learning capability?_code': {'yes': 1, 'no': 0}, 'Extra-courses did_code': {'no': 0, 'yes': 1}, 'certifications_code': {'information security': 4, 'shell programming': 8, 'r programming': 7, 'distro making': 1, 'machine learning': 5, 'full stack': 2, 'hadoop': 3, 'app development': 0, 'python': 6}, 'workshops_code': {'testing': 6, 'database security': 2, 'game development': 3, 'data science': 1, 'system designing': 5, 'hacking': 4, 'cloud computing': 0, 'web technologies': 7}, 'reading and writing skills_code': {'poor': 2, 'excellent': 0, 'medium': 1}, 'memory capability score_code': {'poor': 2, 'medium': 1, 'excellent': 0}, 'Interested subjects_code': {'programming': 9, 'Management': 2, 'data engineering': 5, 'networks': 7, 'Software Engineering': 3, 'cloud computing': 4, 'parallel computing': 8, 'IOT': 1, 'Computer Architecture': 0, 'hacking': 6}, 'interested career area _code': {'testing': 5, 'system developer': 4, 'Business process analyst': 0, 'security': 3, 'developer': 2, 'cloud computing': 1}, 'Type of company want to settle in?_code': {'BPA': 0, 'Cloud Services': 1, 'product development': 9, 'Testing and Maintainance Services': 7, 'SAaS services': 4, 'Web Services': 8, 'Finance': 2, 'Sales and Marketing': 5, 'Product based': 3, 'Service Based': 6}, 'Taken inputs from seniors or elders_code': {'no': 0, 'yes': 1}, 'Interested Type of Books_code': {'Series': 28, 'Autobiographies': 3, 'Travel': 29, 'Guide': 13, 'Health': 14, 'Journals': 17, 'Anthology': 1, 'Dictionaries': 9, 'Prayer books': 21, 'Art': 2, 'Encyclopedias': 11, 'Religion-Spirituality': 22, 'Action and Adventure': 0, 'Comics': 6, 'Horror': 16, 'Satire': 24, 'Self help': 27, 'History': 15, 'Cookbooks': 7, 'Math': 18, 'Biographies': 4, 'Drama': 10, 'Diaries': 8, 'Science fiction': 26, 'Poetry': 20, 'Romance': 23, 'Science': 25, 'Trilogy': 30, 'Fantasy': 12, 'Childrens': 5, 'Mystery': 19}, 'Management or Technical_code': {'Management': 0, 'Technical': 1}, 'hard/smart worker_code': {'smart worker': 1, 'hard worker': 0}, 'worked in teams ever?_code': {'yes': 1, 'no': 0}, 'Introvert_code': {'no': 0, 'yes': 1}, 'Suggested Job Role_code': {'Applications Developer': 0, 'CRM Technical Developer': 1, 'Database Developer': 2, 'Mobile Applications Developer': 3, 'Network Security Engineer': 4, 'Software Developer': 5, 'Software Engineer': 6, 'Software Quality Assurance (QA) / Testing': 7, 'Systems Security Administrator': 8, 'Technical Support': 9, 'UX Designer': 10, 'Web Developer': 11}}

dropdownList = {'Logical quotient rating':[5, 7, 2, 9, 1, 6, 4, 8, 3], 
                'hackathons': [0, 6, 3, 1, 5, 4, 2], 
                'coding skills rating': [6, 4, 9, 3, 5, 1, 8, 2, 7], 
                'public speaking points': [2, 3, 1, 5, 4, 7, 9, 6, 8], 
                'self-learning capability?': ['yes', 'no'], 
                'Extra-courses did': ['no', 'yes'], 
                'certifications': ['information security', 'shell programming', 'r programming', 'distro making', 'machine learning', 'full stack', 'hadoop', 'app development', 'python'], 
                'workshops': ['testing', 'database security', 'game development', 'data science', 'system designing', 'hacking', 'cloud computing', 'web technologies'], 
                'reading and writing skills': ['poor', 'excellent', 'medium'], 
                'memory capability score': ['poor', 'medium', 'excellent'], 
                'Interested subjects': ['programming', 'Management', 'data engineering', 'networks', 'Software Engineering', 'cloud computing', 'parallel computing', 'IOT', 'Computer Architecture', 'hacking'], 
                'interested career area ': ['testing', 'system developer', 'Business process analyst', 'security', 'developer', 'cloud computing'], 
                'Type of company want to settle in?': ['BPA', 'Cloud Services', 'product development', 'Testing and Maintainance Services', 'SAaS services', 'Web Services', 'Finance', 'Sales and Marketing', 'Product based', 'Service Based'], 
                'Taken inputs from seniors or elders': ['no', 'yes'],
                'Interested Type of Books': ['Series', 'Autobiographies', 'Travel', 'Guide', 'Health', 'Journals', 'Anthology', 'Dictionaries', 'Prayer books', 'Art', 'Encyclopedias', 'Religion-Spirituality', 'Action and Adventure', 'Comics', 'Horror', 'Satire', 'Self help', 'History', 'Cookbooks', 'Math', 'Biographies', 'Drama', 'Diaries', 'Science fiction', 'Poetry', 'Romance', 'Science', 'Trilogy', 'Fantasy', 'Childrens', 'Mystery'], 
                'Management or Technical': ['Management', 'Technical'], 
                'hard/smart worker': ['smart worker', 'hard worker'], 
                'worked in teams ever?': ['yes', 'no'], 'Introvert': ['no', 'yes'], 
                'Suggested Job Role': ['Applications Developer', 'CRM Technical Developer', 'Database Developer', 'Mobile Applications Developer', 'Network Security Engineer', 'Software Developer', 'Software Engineer', 'Software Quality Assurance (QA) / Testing', 'Systems Security Administrator', 'Technical Support', 'UX Designer', 'Web Developer']}

# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk
import pickle
import re

# Create the main window
root = tk.Tk()
root.title("Registration Form")

# Create a canvas with a scrollbar
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

title = ttk.Label(scrollable_frame, font=("Arial", 20), text="Skilled-based Career Recommendation System").grid(row=0, column=60, padx=10, pady=50)

# Add the form elements to the scrollable frame
entry={}
label={}
j=1
for i in qList:
    l=re.sub(r'\_code\b', '', i)
    label[i] = ttk.Label(scrollable_frame, text=l+" : ")
    entry[i] = ttk.Entry(scrollable_frame)
    label[i].grid(row=j, column=0, padx=10, pady=10, sticky="w")
    entry[i].grid(row=j, column=1, padx=10, pady=10, sticky="ew")
    j+=1
    
temp = Dict["Suggested Job Role_code"];
temp = {v: k for k, v in temp.items()}
Dict.pop("Suggested Job Role_code");

def submit_form():
    args={}
    for i in qList:
        if(i not in list(Dict.keys())):
             args[i]=int(entry[i].get().strip())
        else:
            args[i]=entry[i].get().strip()

        print(args[i])
        

    
    for i in list(Dict.keys()):
        args[i] = Dict[i][args[i]]
        print(args[i])
        
    tk.messagebox.showinfo("Success", "Registration form submitted successfully!")
    
    with open("./model.pkl","rb") as f:
        mp = pickle.load(f)
    
    mp.feature_names = None
    value =  mp.predict([list(args.values())])
    print(value)
    
    predicted_career=temp[round(value[0])];
    print("Recommended career is "+predicted_career)
    outputLabel = ttk.Label(scrollable_frame, font=("Arial", 15), text='Recommended career is '+predicted_career)
    outputLabel.grid(row=j+2, column=50, padx=10, pady=30, sticky="w")
        
    
submit_button = ttk.Button(scrollable_frame, text="Submit", command=submit_form)
submit_button.grid(row=j+1, column=1, padx=10, pady=10, sticky="e")


# Pack the scrollbar and canvas into the main window
scrollbar.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)

# Run the main loop
root.mainloop()

