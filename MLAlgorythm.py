import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from Get_sleep_data import data

sdata = data.get_data()


num_samples = len(sdata)
num_dep_variables = 11


# 2. Split Data into Training and Testing Sets
data_train, data_test= train_test_split(sdata, test_size=0.1, random_state=42)


# 3. Create and Train the Linear Regression Model
model = LinearRegression()

model.fit(data_train[:5] + data_train[5 + 1:], data_train[5])

# 4. Make Predictions
y_pred = model.predict(data_test[:5]+ data_test[5 + 1:])


# 5. Evaluate the Model (Optional)
# You can check the R-squared score or other metrics
from sklearn.metrics import r2_score
r_squared = r2_score(data_test[5], y_pred)
print(f"R-squared score: {r_squared:.2f}")


# Print the learned coefficients
print(f"Intercept (b0): {model.intercept_[0]:.2f}")
print(f"Coefficient (b1): {model.coef_[0][0]:.2f}")