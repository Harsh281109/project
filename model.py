import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

# Load data
data = pd.read_csv("data.csv")

X = data[['energy_usage', 'waste', 'water_usage']]
y = data['carbon_emission']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Models
lr = LinearRegression()
rf = RandomForestRegressor()

lr.fit(X_train, y_train)
rf.fit(X_train, y_train)

# Accuracy
lr_score = r2_score(y_test, lr.predict(X_test))
rf_score = r2_score(y_test, rf.predict(X_test))

# Choose best model
model = rf if rf_score > lr_score else lr
model_name = "Random Forest" if rf_score > lr_score else "Linear Regression"
accuracy = max(lr_score, rf_score)

def predict(energy, waste, water):
    return model.predict([[energy, waste, water]])[0]
