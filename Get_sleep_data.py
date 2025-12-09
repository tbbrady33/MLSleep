import csv
import os
import sys

class data:
    def __init__(self):
        
        self.Sleep_data = {
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

    def get_data(self):

        def time_to_decimal(t):
            hours, minutes = t.split(":")
            return int(hours) + int(minutes)/60

        current_dir = os.getcwd()
        csv_path = os.path.join(current_dir, "Health_Sleep_Statistics.csv")

        with open(csv_path, newline="") as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                self.Sleep_data["Age"].append(row[1])
                
                #female = 1, male = 0
                if row[2] == "f":
                    self.Sleep_data["Gender"].append(1)
                elif row[2] == "m":
                    self.Sleep_data["Gender"].append(0)
                else:
                    raise ValueError

                self.Sleep_data["Sleep Quality"].append(row[3])
                self.Sleep_data["Bedtime"].append(time_to_decimal(row[4]))
                
                self.Sleep_data["Wake-up Time"].append(time_to_decimal(row[5]))
                
                self.Sleep_data["Daily Step"].append(row[6])
                self.Sleep_data["Calories Burned"].append(row[7])
                
                #high = 1, medium = 0.5, low = 0
                if row[8] == "high":
                    self.Sleep_data["Physical Activity Level"].append(1)
                elif row[8] == "medium":
                    self.Sleep_data["Physical Activity Level"].append(0.5)
                elif row[8] == "low":
                    self.Sleep_data["Physical Activity Level"].append(0)
                else:
                    raise ValueError

                #healthy = 1, medium = 0.5, unhealthy = 0
                if row[9] == "healthy":
                    self.Sleep_data["Dietary Habits"].append(1)
                elif row[9] == "medium":
                    self.Sleep_data["Dietary Habits"].append(0.5)
                elif row[9] == "unhealthy":
                    self.Sleep_data["Dietary Habits"].append(0)
                else:
                    raise ValueError

                #yes = 1, no = 0
                if row[10] == "yes":
                    self.Sleep_data["Sleep Disorders"].append(1)
                elif row[10] == "no":
                    self.Sleep_data["Sleep Disorders"].append(0)
                else:
                    raise ValueError
            
                if row[11] == "yes":
                    self.Sleep_data["Medication Usage"].append(1)
                elif row[11] == "no":
                    self.Sleep_data["Medication Usage"].append(0)
                else:
                    raise ValueError

        return self.Sleep_data





