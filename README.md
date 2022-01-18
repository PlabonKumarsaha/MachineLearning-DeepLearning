# MachineLearning-DeepLearning

***Install JupyterNoteBook***
1. Go to App Data(run -> %Appdata%) >> Local >> Program >> python >> scripts
2. open CMD on that location
3. pip insatll jupyter 
4. After installation write jupyter notebook

**Use Google Colab**
- go to colab
- start new Notebook
*Import file in colab*
```
from google.colab import files
files.upload()

```
## Project :

* [Spam mail detection](https://github.com/PlabonKumarsaha/MachineLearning-DeepLearning/tree/main/ML/05.Spam%20mail%20detector%20TF-IDF%20Vectorizer)
1. pre processing : Count Vectorizer
2. ML model : MultinomialNB(naive_bayes)
3. 99 % accurate
4.show performance matrix
5. show confusion matrix
6.show classification report
7.K fold cross validation for getting accuracy scores

* Profit Prediction

1. Null value checking and resolving
2. one hot encoding for data pre processing
3. concating onehot encoding values to the table
4. Testing on single input and multiple  test set
5. R-Squared Value for model accuracy testing

**House Price Prediction**

[dataset](https://archive.ics.uci.edu/ml/machine-learning-databases/housing/?C=N;O=D)

1.Supervised learning <br>
2.No Null values in the dataset
3.Linear Regression
4.Random forest  

**Predicting Heart Disease using Random Forest**

[dataset](https://www.kaggle.com/sulianova/cardiovascular-disease-dataset)
70k dataset 
1. Supervised learning to predict if a patient has Heart Disease
2. find coefficincy 
3. f_classif for learning and removing the least related features
4.  use seaborn to plot the data
5.  Do RandomForest and DecisionTreeClassifier
6.  Feature importance using ExtraTreesClassifier
7.  Univariate feature selection() -SelectKBest
8.  Feature importace - 

**Customer churn prediction**

[dataset](https://www.kaggle.com/studymart/customer-churn-prediction)

1.Supervised learning <br>
2.No Null values in the dataset
3.vizualize data using seaborn countplots
4.LabelEncoder to remove multiple text realted data columns
5. scale the data using StandardScaler(reduces calculation later for training)
6.Logistic Regression
7.accuracy_score
8.confusion_matrix generation
9.classification_report
10.Perfromance Metrices

ML
12. KNN - Data preProc - LabelEncoder , Model - KNN

Must checked link
- vaex : https://pypi.org/project/vaex/
- Vaex api doc : https://vaex.readthedocs.io/en/latest/api.html
- https://www.kaggle.com/lavanyashukla01/how-i-made-top-0-3-on-a-kaggle-competition
- feature enginnering https://www.youtube.com/watch?v=6WDFfaYtN6s&list=PLZoTAELRMXVPwYGE2PXD3x0bfKnR0cJjN&ab_channel=KrishNaik-  
- MLprojects :https://www.youtube.com/channel/UCX802rmp2Sg2ddyLU7Qo1bQ/videos
- feature selection : https://www.youtube.com/watch?v=YaKMeAlHgqQ&ab_channel=DataSchool
- web scrapping : https://www.youtube.com/watch?v=r_xb0vF1uMc&list=PL5-da3qGB5IDbOi0g5WFh1YPDNzXw4LNL&ab_channel=DataSchool


**Use of Naive Bayes**
1. Real time prediction
2. Recommendation system
3. Text classifier
4. Multi class predictor
5. Sklearn's naive bayes variants - GaussianNB, BernoulliNB, MultinomialNB(skip this if there is any negative value in any row) 

**13.K means clustering**
1. Useage : for similar product showing by ecommerce , market basket , biology , finidng disticnt types of classes from this
2. unsupervised learning so the data is Unlabled.
3. Elbow mehod to learn the optimized number of cluster

**Deep Learning**
1.Hand written digit classifier
- use mnist
- keras
- Normalization
- flattening of an image array
- show image of a matrix using matshow
- Training a multi layer model
- optimize the model using 'adam'
- evaluating the model
- generating a confusion matrix
2. Customer churn prediction Impact Learning
This was done using ML algorithms but a new proposed method named Impact Leanring was used to do it again
Doc - https://pypi.org/project/ImpactLearning/
3. Data augmentation : https://blog.keras.io/building-powerful-image-classification-models-using-very-little-data.html

**Save a model**
-> Using pickle
1. import pickle
2. save the model
```
with open('svm_model','wb') as f:
    pickle.dump(model,f)
```
3.open the model from file
```
with open('svm_model','rb') as f:
     loadedModel = pickle.load(f)
```
-> using joblib
1. import joblib
2. joblib.dump(model,'model_joblib') # save the model
3. svm = joblib.load('model_joblib') # load the model


Location to run scripts : C:\Users\PKS\AppData\Local\Programs\Python\Python37\Scripts
**Handling imbalance dataset**
* Over Sampling : when dataset is not huge
* Under Sampling : when dataset is huge. It makes the outcome variable more balanced

### To learn
* Unsupervised learning using sklearn
* sklearn pipelining
* import pickle
* call from frontend
* Beautiful Soup
* graphx
* hadoop
