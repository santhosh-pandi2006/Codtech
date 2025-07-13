# Import necessary libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# Load dataset
url = "https://raw.githubusercontent.com/justmarkham/pycon-2016-tutorial/master/data/sms.tsv"
df = pd.read_csv(url, sep='\t', header=None, names=['label', 'message'])

# Display basic info
print("Dataset Sample:")
print(df.head())

# Convert labels to binary (spam=1, ham=0)
df['label'] = df['label'].map({'ham': 0, 'spam': 1})

# Text preprocessing and vectorization
cv = CountVectorizer()
X = cv.fit_transform(df['message'])
y = df['label']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model Training
model = MultinomialNB()
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Evaluation
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("\nAccuracy Score:", accuracy_score(y_test, y_pred))

# Optional: Predicting custom messages
sample = ["Congratulations! You've won a free ticket!", "Hey, are we still meeting for lunch?"]
sample_vec = cv.transform(sample)
predictions = model.predict(sample_vec)
for msg, pred in zip(sample, predictions):
    print(f"'{msg}' => {'Spam' if pred == 1 else 'Not Spam'}")
