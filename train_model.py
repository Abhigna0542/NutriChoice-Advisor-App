import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# Load dataset
df = pd.read_csv('bmi_data.csv')

# Convert gender to numeric: Male=0, Female=1
df['Gender'] = df['Gender'].map({'Male': 0, 'Female': 1})

# Features and label
X = df[['Gender', 'Height', 'Weight']]
y = df['BMI']

# Train the model
model = LinearRegression()
model.fit(X, y)

# Save model to file
joblib.dump(model, 'bmi_predictor.pkl')
print("✅ Model trained and saved successfully as bmi_predictor.pkl.")
