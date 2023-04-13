# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 20:49:11 2023

@author: Raghul S
"""

from preprocessing import X_train_s, y_train_encoded, X_test_s, y_test_encoded

X_train = X_train_s
X_test = X_test_s
y_train  = y_train_encoded
y_test = y_test_encoded

from sklearn.metrics import confusion_matrix,accuracy_score

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error

forest=RandomForestRegressor(random_state=10, n_estimators = 5)
forest.fit(X_train, y_train)

rf_y_pred = forest.predict(X_test)

print("\nDecision Tree Classifier : \n")

# calculating R2 score
r2 = r2_score(y_test, rf_y_pred)
print("R2 score:", r2)

# calculating mean squared error
mse = mean_squared_error(y_test,rf_y_pred)
print("Mean squared error:", mse)

# calculating root mean squared error
rmse = mean_squared_error(y_test,rf_y_pred, squared=False)
print("Root mean squared error:", rmse)

from sklearn.tree import DecisionTreeClassifier

dtree = DecisionTreeClassifier(random_state=1)
dtree = dtree.fit(X_train, y_train)

dt_y_pred = dtree.predict(X_test)
dt_cm = confusion_matrix(y_test,dt_y_pred)
dt_accuracy = accuracy_score(y_test,dt_y_pred)
print("\n\nDecision Tree Classifier : ")
print("\nconfusion matrics=",dt_cm)
print("  ")
print("accuracy=",dt_accuracy*10)

from xgboost import XGBClassifier

xgb = XGBClassifier(random_state = 40, learning_rate=0.03, n_estimators=250)
xgb.fit(X_train, y_train)

xgb_y_pred = xgb.predict(X_test)
xgb_cm = confusion_matrix(y_test,xgb_y_pred)
xgb_accuracy = accuracy_score(y_test,xgb_y_pred)
print("\n\nXGB Classifier : ")
print("\nconfusion matrics=",xgb_cm)
print("  ")
print("accuracy=",xgb_accuracy*10)

from sklearn import svm

svm = svm.SVC()
svm.fit(X_train, y_train)

svm_y_pred = svm.predict(X_test)
svm_cm = confusion_matrix(y_test,svm_y_pred)
svm_accuracy = accuracy_score(y_test,svm_y_pred)
print("\n\nSVM Classifier : ")
print("\nconfusion matrics=",svm_cm)
print("  ")
print("accuracy=",svm_accuracy*10)


import pickle

pickle.dump(forest, open("./models/rf_model.pkl","wb"))
pickle.dump(dtree, open("./models/dt_model.pkl","wb"))
pickle.dump(xgb, open("./models/xgb_model.pkl","wb"))
pickle.dump(svm, open("./models/svm_model.pkl","wb"))

