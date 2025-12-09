import csv

class data:
    def get_data():

        sleep_data = []
        with open("/Users/kmbrady/Desktop/cs111/MLSleep/Health_Sleep_Statistics.csv", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                sleep_data.append(row)
        return sleep_data

Sleep_data = {
    "Age": [],
    "Gender": [],
    "Sleep Quality": [],
    "Bedtime": [],
    "Wake-up Time": [],
    "Daily Step": [],
    "Calories Burned": [],
    "Physical Activity Level": [],
    "Dietary Habits": [],
    "Sleep Disorders": [],
    "Medication Usage": []

}
with open("/Users/kmbrady/Desktop/cs111/MLSleep/Health_Sleep_Statistics.csv", newline="") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        Sleep_data["Age"].append(row[1])
        Sleep_data["Gender"].append(row[2])
        Sleep_data["Sleep Quality"].append(row[3])
        Sleep_data["Bedtime"].append(row[4])
        Sleep_data["Wake-up Time"].append(row[5])
        Sleep_data["Daily Step"].append(row[6])
        Sleep_data["Calories Burned"].append(row[7])
        Sleep_data["Physical Activity Level"].append(row[8])
        Sleep_data["Dietary Habits"].append(row[9])
        Sleep_data["Sleep Disorders"].append(row[10])
        Sleep_data["Medication Usage"].append(row[11])



