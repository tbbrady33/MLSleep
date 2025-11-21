class data:
    def get_data():

        sleep_data = {}
        with open("Health_Sleep_Statistics", "r") as file:
            for line in file:
                line = line.strip()
                user_id, age, gender, sleep_quality, bedtime, wakeup_time, daily_steps, calories_burned, physical_activity_level, dietary_habits, sleep_disorders, medication_usage = line.split(",")
                
                sleep_data[user_id] = {
                    "age": age,
                    "gender": gender,
                    "sleep quality": sleep_disorders,
                    "bedtime": bedtime,
                    "wake-up time": wakeup_time,
                    "daily steps": daily_steps,
                    "calories burned": calories_burned,
                    "physical activity level": physical_activity_level,
                    "dietary habits": dietary_habits,
                    "sleep disorders": sleep_disorders,
                    "medication usage": medication_usage
                }