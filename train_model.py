import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle

# Load dataset
data = pd.read_csv("phishing.csv")

# Features
X = data[['UrlLength','NumDots','NumDash','AtSymbol','NumUnderscore','NoHttps','PathLength']]

# Target
y = data['CLASS_LABEL']

# Train test split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)

# Model
model = LogisticRegression()

# Train
model.fit(X_train,y_train)

# Save model
pickle.dump(model,open("phishing_model.pkl","wb"))

print("Model trained and saved successfully")