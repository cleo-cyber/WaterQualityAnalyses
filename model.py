import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
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
print(dataset.info())
x_test = sc.transform(x_test)
# print(x.head())
# Fitting Random Forest Classification to the Training set
classifier = RandomForestClassifier(n_estimators = 100, max_depth=5, criterion = 'entropy')
classifier.fit(x_train, y_train)


# Saving model to disk
# Predicting the Test set results
y_pred = classifier.predict(x_test)

pickle.dump(classifier, open('water_model.pkl','wb'))

# Making the Confusion Matrix
cm = confusion_matrix(y_test, y_pred)

# Print confusion matrix
print(cm)
print("Accuracy of Random Forest Classifier is:",accuracy_score(y_test, y_pred))

