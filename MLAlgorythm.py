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
sdata_matrix = sdata_matrix.astype(float)

num_samples = len(sdatamatrix)
num_dep_variables = 11

target_index = 2   # change this to the right one

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

def time_to_decimal(t):
    hours, minutes = t.split(":")
    return int(hours) + int(minutes)/60

print("Please input the following: ")

Age = float(input("Age: "))
Gender = float(input("Gender (for male enter 0 and for female enter 1): "))
Bedtime = float(time_to_decimal(input("Bedtime (in military standard time ex: 23:15): ")))
Daily_Steps = float(input("Daily_Steps: "))
Calories_Burned = float(input("Calories Burned: "))
Physical_Activity_Level = float(input("Physical Activity Level (High = 1, medium = 0.5, low = 0): "))
Dietary_Habits = float(input("Dietary Habits (healthy = 1, medium = 0.5, unhealthy = 0): "))
Sleep_Disorders = float(input("Sleep Disorders (for yes enter 1 and for no enter 0): "))
Medication_Usage = float(input("Medication_Usage (for yes enter 1 and for no enter 0): "))
Wake_up_time = 0

sleep_quality_list = []
times = []

start = (Bedtime + 7) % 24
end = (Bedtime + 10) % 24

for i in np.arange(start, start + 3, 0.25): 
    wake_time = i % 24
    times.append(wake_time)

    User_input_list = [Age, Gender, Bedtime, wake_time, Daily_Steps, Calories_Burned, Physical_Activity_Level, Dietary_Habits, Sleep_Disorders, Medication_Usage]

    sleep_quality = model.predict([User_input_list])[0]
    sleep_quality_list.append(sleep_quality)

best_index = np.argmax(sleep_quality_list)

Wake_up_time = times[best_index]

hours = int(Wake_up_time)
minutes = int((Wake_up_time - hours) * 60)

if minutes == 60:
    minutes = 0
    hours = (hours + 1) % 24

print(f"Your ideal wake up time is {hours}:{minutes:02d}")