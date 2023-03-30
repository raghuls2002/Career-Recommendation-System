**Name :** Raghul.S <br>
**Reg.no :** 20BCE0915<br>
**Course code :** CSE1901<br>
**Class Nbr :** VL2022230505138<br>
**Faculty Name :** Manoov R <br>

# **Review - 2** : **Skill-based Career Recommendation System**

<br>

## **Literature Review**

### **Introduction**

Previously, the questionnaire method was used to forecast a student's career. However, it is a time-consuming process, and it is difficult to determine the status of students' opinions. Various computing techniques are used to forecast the student's future career. In this literature review, we aim to synthesize existing research on skill-based career recommendation systems. We will also compare the accuracy of various ML algorithms such as SVM (Scalar Vector Machine), RF (Random Forest), XGB (XGBClassifier ), DT(Decision Tree) and Linear Regression.

### **Methodology**

#### **Data Pre-Processing**

#####

#### **Algorithms used**

##### **Decision Tree**

The decision tree is a basic machine learning technique that can be used for regression tasks. It is structured like a flow-chart, with each non-leaf node representing a test on an attribute and each branch representing the test's outcome. The leaf nodes contain class labels, and the topmost node is called the root node. This model is particularly effective for handling tabular data that has numerical or categorical features with a small number of categories (less than a few hundred). Different machine learning models have varying advantages depending on the situation.

The first step in creating a decision tree involves selecting the root value. Next, the Information Gain (IG) and entropy of each node must be computed before it is divided. Nodes with higher IG or lower entropy values are preferred for division. This process is repeated until there are no further options for division or the entropy value is low. Entropy is an important metric for evaluating the likelihood of information. IG is used to measure the decrease in entropy value before each division. 

To construct a decision tree, two types of entropy are computed using a frequency data table. The entropy value can be calculated using only one attribute in the frequency table, as shown in the following equation.

**$$E(S) = \sum_{i = 1}^{c} - p_{i}\log_{2}(p_{i})$$**

The Entropy value of frequency table is caculated by using two attributes as the following equation:

**$$E(T, X) = \sum_{c \in X}P(c)E(c)$$**

The IG value can be calculated by using the following equation.

**$$Gain(T, X) = Entropy(T) - Entropy(T, X)$$**

##### **Random Forest Classifier**

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
Let $C_{b}(x)$ be the class prediction of the bth random-forest tree. Then, $Classification: $$C_{rf}^{B}(x) = majority vote (C_{b})_{1}^{B}$$

### **Proposed System**
### **Result**



## **Demonstration**
