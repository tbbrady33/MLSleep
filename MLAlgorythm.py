import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from Get_sleep_data import data

data = data.getdata()


num_samples = len(data)
num_variables = 11
# 2. Split Data into Training and Testing Sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Create and Train the Linear Regression Model
model = LinearRegression()
model.fit(X_train, y_train)

# 4. Make Predictions
y_pred = model.predict(X_test)

# 5. Evaluate the Model (Optional)
# You can check the R-squared score or other metrics
from sklearn.metrics import r2_score
r_squared = r2_score(y_test, y_pred)
print(f"R-squared score: {r_squared:.2f}")

# 6. Visualize the Results
plt.scatter(X_test, y_test, color='blue', label='Actual data')
plt.plot(X_test, y_pred, color='red', linewidth=2, label='Regression line')
plt.xlabel("Independent Variable (X)")
plt.ylabel("Dependent Variable (y)")
plt.title("Simple Linear Regression")
plt.legend()
plt.show()

# Print the learned coefficients
print(f"Intercept (b0): {model.intercept_[0]:.2f}")
print(f"Coefficient (b1): {model.coef_[0][0]:.2f}")