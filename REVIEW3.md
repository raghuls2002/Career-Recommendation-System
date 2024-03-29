**Name :** Raghul.S <br>
**Reg.no :** 20BCE0915<br>
**Course code :** CSE1901<br>
**Class Nbr :** VL2022230505138<br>
**Faculty Name :** Manoov R <br>

# **Review - 3** : **Skill-based Career Recommendation System using Random Forest Classifier**

<br>

## **Abstract**

According to a recent study, most college
graduates find it challenging to choose their career
field. A lot of engineers are working to make IT the
dominant discipline. Therefore, they are doing
various online courses and aimlessly looking for
employment. Many students today are interested
in careers in the IT industry, but they are unsure of
which field is best for them. To avoid this situation
candidates, need a Job recommendation that
analyses the skills to recommend a suitable job for
the candidate. The solution is to design a system
that reads a resume and their skills.


## **Introduction**

A student may find it challenging to choose the correct job route because they are going
through a number of different stages at this time, including peer pressure and parental
pressure. Therefore, a model that directs the student based on his or her profile and skill ratings
can be designed to assist pupils in such situations. An algorithm can be used to pull special
characteristics from the profile and forecast both the best career option and the career options
one should avoid choosing. This will enable the learner to succeed in the area where he or she
is most talented.

This skill-based career recommendation system focuses on predicting the suitable jobs for the
candidates. It uses machine learning models to find similarities between jobs description and
resumes to predict accurately. This application can be used by any candidates who need or
who want to know about their suitable jobs and to improve themselves with both soft skills and
hard skills. It will be helpful to them by not wasting their time searching for jobs. They can also
grow their skills in their domain and grow faster in their domain.


## **Literature Survey**

| Study | Year | Methodology | Results |
|-------|------|-------------|---------|
|[ Career Prediction System](https://ijsrst.com/IJSRST218411)| 2021 | XGBoost | Career Prediction System developed using machine learning is very effective in predicting correct career based on the student skills possessed in required fields. |
| [Student Future Prediction Using Machine Learning](https://www.researchgate.net/publication/332408552_Student_Future_Prediction_Using_Machine_Learning)| 2019 | Linear Regression, Decision Tree Regression, Random Tree classifier |The system  will  help  student  used  to  predict  the suitable  course. The system can facilitate the students, as it will guide them to take appropriate decision while choosing the stream  as  his/her  career.|
| [Random Forests and Decision Trees](https://www.researchgate.net/publication/259235118_Random_Forests_and_Decision_Trees)| 2012 | Random Forests, Decision Trees | From the results, it can be concluded that the Random Forest achieves increased classification performance and yields results that are accurate and precise in the cases of large number of instances. These scenarios also cover the missing values problem in the datasets and thus besides accuracy, it also overcomes the over-fitting problem generated due to missing values in the datasets |
|[An artificial neural network approach in predicting career strand of incoming senior high school students](https://www.researchgate.net/publication/336385371_An_artificial_neural_network_approach_in_predicting_career_strand_of_incoming_senior_high_school_students)| 2018 | Artificial Neural Network (ANN) | With an accuracy of 74.1%, this study built a predictive model that can forecast an incoming senior high school student's choice of strand. This study demonstrated the application of the discretization method to improve prediction accuracy.|
|[Career Choice Prediction Based on Campus Big Data—Mining the Potential Behavior of College Students](https://www.researchgate.net/publication/340838530_Career_Choice_Prediction_Based_on_Campus_Big_Data-Mining_the_Potential_Behavior_of_College_Students)| 2020 | XGBoost | To forecast students' profession choices, this study proposed the Approach Cluster Centres Based On XGBOOST (ACCBOX) model. By analysing behavioural data from over four thousand students, the experimental results show that this techniques outperforms existing techniques.|


## **Architecture**

Previously, the questionnaire method was used to forecast a student's career. However, it is a time-consuming process, and it is difficult to determine the status of students' opinions. Various computing techniques are used to forecast the student's future career. In this project, we aim to synthesize existing research on skill-based career recommendation systems. 

### **Existing System**

There are multiple models available in the market to address the same problem, each with its own advantages and disadvantages. Some existing systems use these methods as input: 

* **Forecasting using Academic Grades** <br> 
Using student academic grades as input for forecasting may not be efficient as individual grades depend on factors such as college, exam models, paper evaluation, and so on.

* **Forecasting using YES/NO Questionnaire** <br>
Asking a questionnaire with various required fields and receiving a yes/no answer may confuse students. For instance, in a particular course, a student may only have basic knowledge, and hence, not know whether to answer yes or no. In such cases, the student might not provide input, leading to incorrect predictions.

* **Lack of Clear Career Roadmap for Forecasting** <br>
Predicting a career without providing a clear roadmap on how to proceed may leave students in a dilemma. Predictions with a clear roadmap can help students understand their career path.

### **Proposed System**

The proposed system will use a dataset consisting of various attributes such as education, experience, skills, interests, and personality traits of individuals to predict their future career path. The system will be designed to leverage the power of machine learning algorithms, specifically random forest, to predict the most suitable career path for an individual based on their skill set. Random forest is a well-established ML algorithm that has been widely used for classification and regression problems. It has proven to be effective in handling high-dimensional data, reducing overfitting, and improving prediction accuracy.

![](./assets/proposed_system.PNG)

## Methodology

### **Data Collection ([mldata.csv](https://github.com/raghuls2002/Weasel/blob/main/data/mldata.csv))**

Questioning students and receiving responses in the form of yes or no may not provide accurate data for predicting a student's career path. To accurately predict a student's career, many parameters such as knowledge in different subjects, specializations, programming skills, hackathons, workshops, certifications, and preferred courses are required. To train a model for this purpose, a [dataset] with over 6,500 records that includes all necessary fields has been collected. The input data is obtained in the form of ratings for various fields of computer science students. Asking students to rate themselves in required fields is the best way to get precise knowledge about their abilities.


### **Data Pre-Processing**

#### **Importing libraries and loading data** <br>

Importing python libraries required for data pre-processing and loading the required CSV file using pandas library

  ```python
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns
    df = data.read_csv('./data/mldata.csv')
    print("Columns in our dataset:\n" , df.columns)
  ``` 
  ###### **Output:**
```
   Columns in our dataset: Index(['Logical quotient rating', 'hackathons', 'coding skills rating',
       'public speaking points', 'self-learning capability?',
       'Extra-courses did', 'certifications', 'workshops',
       'reading and writing skills', 'memory capability score',
       'Interested subjects', 'interested career area ',
       'Type of company want to settle in?',
       'Taken inputs from seniors or elders', 'Interested Type of Books',
       'Management or Technical', 'hard/smart worker', 'worked in teams ever?',
       'Introvert', 'Suggested Job Role'],
      dtype='object')
```


#### **Finding numerical and categorical features**<br>

  ```python
  print("\nList of Numerical features: \n" , data.select_dtypes(include=np.number).columns.tolist())
  print("\nList of Categorical features: \n" , data.select_dtypes(include=['object']).columns.tolist())
  ```
###### **Output:**
  ```
  List of Numerical features: <br>
 ['Logical quotient rating', 'hackathons', 'coding skills rating', 'public speaking points']

  List of Categorical features: <br>
  ['self-learning capability?', 'Extra-courses did', 'certifications', 'workshops', 'reading and writing skills', 'memory capability score', 'Interested subjects', 'interested career area ', 'Type of company want to settle in?', 'Taken inputs from seniors or elders', 'Interested Type of Books', 'Management or Technical', 'hard/smart worker', 'worked in teams ever?', 'Introvert', 'Suggested Job Role']
 ``` 
 
 
#### **Checking missing values**<br>
  In order to check null values in Pandas DataFrame, we use isnull() function this function return dataframe of Boolean values which are True for NaN values.
   ```python
  df.isnull().sum(axis=0)
  ```


#### **Dummy value encoding** <br>
Dummy variable encoding, also known as one-hot encoding, is a technique used in data analysis and machine learning to convert categorical data into numerical data that can be used in statistical and machine learning models.

Using this technique, we avoid having the model interpret the categorical variable as a continuous variable with an inherent order (which may not exist) and instead allow it to treat each category independently. 
  ```python
  for i in data[categorical_cols]:
    data[i] = data[i].astype('category')
    data[i + "_code"] = data[i].cat.codes
    data= data.drop(i, axis=1)
  ```
  
  
#### **Splitting the dataset** <br>
Splitting the dataset is the process of dividing a given dataset into two or more subsets for training and testing purposes in machine learning or data analysis. Here, the dataset is divided into two parts: the training set and the test set. The training set is used to build the machine learning model, while the test set is used to evaluate the performance of the model on new, unseen data.
  ```python
  from sklearn.model_selection import train_test_split

  X=data.drop([target], axis=1)
  y=data[target]
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
  ```
  
  
#### **Label Encoding Target Data** <br>
Label encoding target data refers to the process of converting the categorical labels in the target variable of a machine learning problem into numerical values. This is often necessary because our machine learning algorithms can only handle numerical data as input.
```python
from sklearn.preprocessing import LabelEncoder

label_encoder = LabelEncoder()

y_train_encoded= label_encoder.fit_transform(y_train)
y_test_encoded = label_encoder.transform(y_test)
```

#### **Feature Scaling** <br>
Feature scaling is the process of transforming numerical data in a dataset to a common scale, without distorting differences in the ranges of values. This can help improve the performance and accuracy of machine learning algorithms that are sensitive to the scale of the input features. It involves converting the values of the features in a dataset so that they all fall within a similar range, typically between 0 and 1 or -1 and 1, making them easier to compare and analyze. This can be achieved using various techniques such as normalization, standardization, or rescaling.
  ```python
  from sklearn.preprocessing import StandardScaler
  
  X_train_s = scaler.fit_transform(X_train)
  X_test_s = scaler.transform(X_test)
  ```

### Alogrithms used

#### **Decision Tree**

The decision tree is a basic machine learning technique that can be used for regression tasks. It is structured like a flow-chart, with each non-leaf node representing a test on an attribute and each branch representing the test's outcome. The leaf nodes contain class labels, and the topmost node is called the root node. This model is particularly effective for handling tabular data that has numerical or categorical features with a small number of categories (less than a few hundred). Different machine learning models have varying advantages depending on the situation.

The first step in creating a decision tree involves selecting the root value. Next, the Information Gain (IG) and entropy of each node must be computed before it is divided. Nodes with higher IG or lower entropy values are preferred for division. This process is repeated until there are no further options for division or the entropy value is low. Entropy is an important metric for evaluating the likelihood of information. IG is used to measure the decrease in entropy value before each division. 

To construct a decision tree, two types of entropy are computed using a frequency data table. The entropy value can be calculated using only one attribute in the frequency table, as shown in the following equation.

**$$E(S) = \sum_{i = 1}^{c} - p_{i}\log_{2}(p_{i})$$**

The Entropy value of frequency table is caculated by using two attributes as the following equation:

**$$E(T, X) = \sum_{c \in X}P(c)E(c)$$**

The IG value can be calculated by using the following equation.

**$$Gain(T, X) = Entropy(T) - Entropy(T, X)$$**

#### **Random Forest Classifier**

The Random Forest is a highly effective machine learning model for predictive analytics, widely used in the industry. It is an additive model that generates predictions by combining decisions from a series of base models. Specifically, this class of models can be represented as the sum of simple base models, where each base classifier is a simple decision tree. This technique, which involves using multiple models to improve predictive performance, is known as model ensembling. In the case of random forests, each base model is constructed independently using a different subsample of the data.

The RF approach can be explained as the following steps: 
1. For $b = 1$ to $B$:
  * Draw a bootstrap sample $Z^{*}$ of size $N$ from the training data.
  * Grow a random-forest tree $T_{b}$ to the bootstrapped data, by recursively repeating the following steps for each terminal node of
  the tree, until the minimum node size $n_{min}$ is reached.
    I. Select $m$ variables at random from the $p$ variables.
    II. Pick the best variable/split-point among the $m$.
    III. Split the node into two daughter nodes.
2. Output the ensemble of trees $(T_{b})_{1}^{B}$

To make a prediction at a new point x:
$$Regression: f_{rf}^{B}(x) = \frac{1}{B}{\sum_{b = 1}^{B}}{T_{b}(x)}$$
Let $C_{b}(x)$ be the class prediction of the bth random-forest tree. Then, $$Classification: C_{rf}^{B}(x) = majority vote (C_{b})_{1}^{B}$$

### **Building and training ML Model** 

#### **Intantiating the Model**

Creating random forest classifier object called 'forest'. We are using the hyperparameters : random_states & n_extimators.
```python
from sklearn.ensemble import RandomForestRegressor

forest=RandomForestRegressor(random_state=10, n_estimators = 5)
```
#### **Fitting the Model**

Once we have instantiated the classifier, you can fit the model to the training data using the fit() method. This method takes two arguments: the training features (X_train) and the corresponding training labels (y_train).

```python
forest.fit(X_train, y_train)

rf_y_pred = forest.predict(X_test)
```
After training the model, you can use it to make predictions on new data using the predict()

### **Evaluating Model**

Three following metrics were used for evaluating the performance of the regression model: 

* r2 score, also known as the coefficient of determination, is a metric that measures the proportion of variance in the target variable (y) that can be explained by  the independent variables (X) used in the model. It is a value between 0 and 1, where 1 indicates a perfect fit and 0 indicates that the model does not explain any of the variance in the target variable.
  ```python
  from sklearn.metrics import r2_score, mean_squared_error

  # calculating R2 score
  r2 = r2_score(y_test, rf_y_pred)
  print("R2 score:", r2)
  ```
* MSE (Mean Squared Error) is a metric that measures the average squared difference between the true values of the target variable and the predicted values. It is a popular metric for evaluating the performance of regression models because it penalizes large errors more heavily than small errors.

  ```python
  # calculating mean squared error
  mse = mean_squared_error(y_test,rf_y_pred)
  print("Mean squared error:", mse)
  ```

* RMSE (Root Mean Squared Error) is simply the square root of MSE, and it is also a popular metric for evaluating the performance of regression models. It is more interpretable than MSE because it is in the same units as the target variable.
  ```python
  # calculating root mean squared error
  rmse = mean_squared_error(y_test,rf_y_pred, squared=False)
  print("Root mean squared error:", rmse)
  ```
###### **Output**

![](./assets/ml_evaluation.PNG)

### **Saving ML Model**

Pickle is a Python module used for serializing and de-serializing Python object structures, including machine learning models. Serializing is the process of converting an object's state to a byte stream, while de-serializing is the reverse process of reconstructing the object from the serialized state.

When it comes to machine learning models, Pickle can be used to save a trained model to a file so that it can be loaded later and used for making predictions or further training. The saved model can be used for deployment, sharing or archival purposes.

```python
import pickle

pickle.dump(forest, open("./models/rf_model.pkl","wb"))
```

### **Loading ML Model**

Loading a machine learning model using Pickle is a straightforward process that involves de-serializing the saved object back into a Python object that can be used for making predictions on new data.

```python
import pickle

with open("./models/rf_model.pkl","rb") as f:
     mp = pickle.load(f)
```

### **Making Prediction based on user entered values**

The user-entered values '**args**' undergo dummy variable encoding and standard feature scaling. Then, they are used to make predictions with the help of **predict()** function. The resultant value is decoded using **inverse_transform()**  and rounded off using **round()** to generate a user-readable value.

```python
value =  mp.predict(scaler.transform([list(args.values())]))
    
predicted_career = label_encoder.inverse_transform([round(value[0])])
print("Recommended career is "+predicted_career[0])
```


## **Results and Discussion**

The web app is built using Flash web framework and is host on 'localhost:5000'. The user selects the a series of values from a series of dropdown fields and clicks the submit button. Then, the program predicts a career based on the input entry values and displays it along with the correlation matrix of the data used.

Figure .1: Form gets the input values

![](./assets/Demo1.1/input1.PNG)

Figure .2: Displaying the recommended career

![](./assets/Demo1.1/output1.PNG)

Figure .3: Form gets the input values

![](./assets/Demo1.1/input2.PNG)

Figure .4: Displaying the recommended career

![](./assets/Demo1.1/output2.PNG)

We also visualized the structure of the Random forest model consisting of 5 Decision Trees using the following code: 
```python
from sklearn import tree

for i in range(5):
    plt.figure(figsize=(15,10))
    tree.plot_tree(forest.estimators_[i], filled=True)
    plt.show()
```

##### Output 

Figure 5. Decision Tree no. 1

![](./src/static/rf_1.png)

Figure 6. Decision Tree no. 2

![](./src/static/rf_2.png)

Figure 7. Decision Tree no. 3

![](./src/static/rf_3.png)

Figure 8. Decision Tree no. 4

![](./src/static/rf_4.png)

Figure 9. Decision Tree no. 5

![](./src/static/rf_5.png)

Our results indicate that a skill-based career recommendation system using a random forest classifier can be highly accurate and useful for individuals seeking career guidance. The system can help job seekers identify career paths that align with their skills, interests, and experience. Employers can also use this system to identify potential candidates with the required skills for specific job roles.

One limitation of our study is that we only focused on a limited number of industries, and future studies could include a broader range of industries.

## **Conclusion**

In conclusion, our study demonstrates the effectiveness of a skill-based career recommendation system using a random forest classifier. The system can provide personalized career guidance for individuals and assist employers in identifying potential candidates for job roles. The results of our study could have significant implications for the field of career development and job matching.

## **References**

1. [V Madhan Mohan Reddy, " Career Prediction System", International Journal of Scientific Research in Science and Technology(IJSRST), Print ISSN : 2395-6011, Online ISSN : 2395-602X, Volume 8, Issue 4, pp.54-58, July-August-2021.
Journal](https://ijsrst.com/IJSRST218411)
2. [Chaudhary, Dileep & Prajapati, Harsh & Rathod, Rajan & Patel, Parth & Gurjwar, Rajiv. (2019). Student Future Prediction Using Machine Learning. International Journal of Scientific Research in Computer Science, Engineering and Information Technology. 1104-1108. 10.32628/CSEIT1952300.](https://www.researchgate.net/publication/332408552_Student_Future_Prediction_Using_Machine_Learning)
3. [Ali, Jehad & Khan, Rehanullah & Ahmad, Nasir & Maqsood, Imran. (2012). Random Forests and Decision Trees. International Journal of Computer Science Issues(IJCSI). 9.](https://www.researchgate.net/publication/259235118_Random_Forests_and_Decision_Trees)
4. [Nazareno, Allen & Lopez-Relente, Marie Joy & Gestiada, Geleena & Martinez, M. & Roxas-Villanueva, Ranzivelle. (2019). An artificial neural network approach in predicting career strand of incoming senior high school students. Journal of Physics: Conference Series. 1245. 012005. 10.1088/1742-6596/1245/1/012005. ](https://www.researchgate.net/publication/336385371_An_artificial_neural_network_approach_in_predicting_career_strand_of_incoming_senior_high_school_students)
5. [Nie, Min & Xiong, Zhaohui & Zhong, Ruiyang & Deng, Wei & Yang, Guowu. (2020). Career Choice Prediction Based on Campus Big Data—Mining the Potential Behavior of College Students. Applied Sciences. 10. 2841. 10.3390/app10082841.](https://www.researchgate.net/publication/340838530_Career_Choice_Prediction_Based_on_Campus_Big_Data-Mining_the_Potential_Behavior_of_College_Students)
