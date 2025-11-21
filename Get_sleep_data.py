class data:
    def get_data():

        sleep_data = {}
        with open("Sleep_health_and_lifestyle_dataset.csv", "r") as file:
            for line in file:
                line = line.strip()
                person_id, gender, age, occupation, sleep_duration, quality_of_sleep, physical_activity_level, stress_level, bmi_category, blood_pressure, heart_rate, daily_steps, sleep_disorder = line.split(",")
                    
                sleep_data[person_id] = {
                    "gender": gender,
                    "age": int(age),
                    "occupation": occupation,
                    "sleep duration": sleep_duration,
                    "quality of sleep": quality_of_sleep, 
                    "physical activity level": physical_activity_level, 
                    "stress level": stress_level, 
                    "bmi category": bmi_category, 
                    "blood pressure": blood_pressure, 
                    "heart rate": heart_rate, 
                    "daily steps": daily_steps, 
                    "sleep disorder": sleep_disorder
                    }