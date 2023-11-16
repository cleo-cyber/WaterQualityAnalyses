# Logistic Regression Model
from sklearn.linear_model import LogisticRegression
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
# Metrics
from sklearn.metrics import confusion_matrix, accuracy_score
import pickle

# Importing the dataset
dataset = pd.read_csv('processed_data.csv')

# Splitting the dataset into the Training set and Test set
x=dataset.drop('Potability',axis=1)

y=dataset['Potability']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.30,random_state=50)

# Feature Scaling
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)
# print(x.head())
# Fitting Random Forest Classification to the Training set
classifier = LogisticRegression(random_state=0)
classifier.fit(x_train, y_train)

print("Accuracy of Logistic Regression Classifier is:",classifier.score(x_test, y_test))
print("Classification Report of Logistic Regression Classifier is:",confusion_matrix(y_test, classifier.predict(x_test)))