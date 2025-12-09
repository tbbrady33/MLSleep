import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from Get_sleep_data import data
from sklearn.metrics import r2_score


data1 = data()
sdatamatrix = data1.get_data()
columns = list(sdatamatrix.keys())              # preserve consistent ordering
values = [sdatamatrix[col] for col in columns]  # list of lists (each column)
 
sdata_matrix = np.column_stack(values)
print(sdata_matrix)

num_samples = len(sdatamatrix)
num_dep_variables = 11


target_index = 5   # change this to the right one

X = np.delete(sdata_matrix, target_index, axis=1)   # all columns except target
y = sdata_matrix[:, target_index]                  # just the target column

# ---- Train / test split ----
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.1, random_state=42
)

# ---- Train model ----
model = LinearRegression()
model.fit(X_train, y_train)

# ---- Predict & evaluate ----
y_pred = model.predict(X_test)
r_squared = r2_score(y_test, y_pred)
print(f"R-squared score: {r_squared:.2f}")

print("Intercept:", model.intercept_)
print("Coefficients:", model.coef_)