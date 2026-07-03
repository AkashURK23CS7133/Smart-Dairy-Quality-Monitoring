import joblib
import numpy as np
from sklearn.ensemble import RandomForestClassifier

# Sample training data (replace with real dataset)
X_train = np.array([[5, 60, 3], [10, 70, 5], [0, 90, 1], [20, 40, 7]])  # Example: Temperature, Humidity, Storage Time
y_train = np.array([1, 1, 1, 0])  # 1 = Spoiled, 0 = Not Spoiled

# Train the model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save the model
joblib.dump(model, r"C:\Users\akash\OneDrive\Desktop\Data_Analytics_for_dairy_product\spoilage_model.pkl")

print("✅ Model trained and saved successfully!")
