import pandas as pd
from sklearn.ensemble import RandomForestRegressor

# Load dataset
data = pd.read_csv("data.csv")

X = data[['energy_usage', 'waste', 'water_usage']]
y = data['carbon_emission']

# Train model
model = RandomForestRegressor()
model.fit(X, y)

def predict(energy, waste, water):
    return model.predict([[energy, waste, water]])[0]
