# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 20:49:11 2023

@author: Raghul S
"""

import preprocessing
data = preprocessing.data
target = preprocessing.target

from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix,accuracy_score

X=data.drop([target], axis=1)
y=data[target]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)


from sklearn.ensemble import RandomForestRegressor

forest=RandomForestRegressor(random_state=10)
forest.fit(X_train, y_train)
y_predict = forest.predict(X_test)


from sklearn.tree import DecisionTreeClassifier

dtree = DecisionTreeClassifier(random_state=1)
dtree = dtree.fit(X_train, y_train)

y_pred = dtree.predict(X_test)
cm = confusion_matrix(y_test,y_pred)
accuracy = accuracy_score(y_test,y_pred)
print("confusion matrics=",cm)
print("  ")
print("accuracy=",accuracy*10)

from xgboost import XGBClassifier

xgb = XGBClassifier(random_state = 42, learning_rate=0.02, n_estimators=300)
xgb.fit(X_train, y_train)
xgb_y_pred = xgb.predict(X_test)
xgb_cm = confusion_matrix(y_test,xgb_y_pred)
xgb_accuracy = accuracy_score(y_test,xgb_y_pred)
print("confusion matrics=",xgb_cm)
print("  ")
print("accuracy=",xgb_accuracy*10)

from sklearn import svm

svm = svm.SVC()
svm.fit(X_train, y_train)
svm_y_pred = svm.predict(X_test)
svm_cm = confusion_matrix(y_test,svm_y_pred)
svm_accuracy = accuracy_score(y_test,svm_y_pred)
print("confusion matrics=",svm_cm)
print("  ")
print("accuracy=",svm_accuracy*10)


import pickle

pickle.dump(forest, open("./rf_model.pkl","wb"))
pickle.dump(dtree, open("./dt_model.pkl","wb"))
pickle.dump(xgb, open("./xgb_model.pkl","wb"))
pickle.dump(svm, open("./svm_model.pkl","wb"))

