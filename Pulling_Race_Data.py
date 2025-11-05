import fastf1
import pandas as pd
fastf1.Cache.enable_cache("cache")


schedule_2024 = fastf1.get_event_schedule(2024, include_testing=False)

schedule_2025 = fastf1.get_event_schedule(2025, include_testing=False)

schedule_2024 = schedule_2024[["RoundNumber", "EventDate", "EventName"]]

schedule_2025 = schedule_2025[["RoundNumber", "EventDate", "EventName"]]


# Getting 2024 Race Data
# Creating empty list to store all results from Race from 2024 data
race_results_2024 = []
race_laps_2024 = []
race_weather_2024 = []

# Looping throggh schedule to get each round's qualifying data
for x in range(1, len(schedule_2024) + 1):
    try:
        race_session_2024 = fastf1.get_session(2024, x, "R")
        race_session_2024.load(telemetry=False)

        race_data_2024 = race_session_2024.results
        race_data_2024["RoundNumber"] = x

        race_laps_2024_data = race_session_2024.laps
        race_laps_2024_data["RoundNumber"] = x

        race_weather_2024_data = race_session_2024.weather_data
        race_weather_2024_data["RoundNumber"] = x

        race_results_2024.append(race_data_2024)
        race_laps_2024.append(race_laps_2024_data)
        race_weather_2024.append(race_weather_2024_data)

    except Exception as e:
        print(f"Could not get data for Round {x}, because: {e}")


race_results_data_2024 = pd.concat(race_results_2024, ignore_index=True)
race_laps_data_2024 = pd.concat(race_laps_2024, ignore_index=True)
race_weather_data_2024 = pd.concat(race_weather_2024, ignore_index=True)

race_results_data_2024.to_csv("2024_Race_Results.csv", index=False)
race_laps_data_2024.to_csv("2024_Race_Laps.csv", index=False)
race_weather_data_2024.to_csv("2024_Race_Weather.csv", index=False)
# Getting Race 2025 Data
race_results_2025 = []
race_laps_2025 = []
race_weather_2025 = []

# Looping throggh schedule to get each round's qualifying data
for y in range(1, len(schedule_2025)+ 1):
    try:
        race_session_2025 = fastf1.get_session(2025, y, "R")
        race_session_2025.load(telemetry=False)

        race_data_2025 = race_session_2025.results
        race_data_2025["RoundNumber"] = y

        race_laps_2025_data = race_session_2025.laps
        race_laps_2025_data["RoundNumber"] = y

        race_weather_2025_data = race_session_2025.weather_data
        race_weather_2025_data["RoundNumber"] = y

        race_results_2025.append(race_data_2025)
        race_laps_2025.append(race_laps_2025_data)
        race_weather_2025.append(race_weather_2025_data)

    except Exception as e:
        print(f"Could not get data for Round {y}, because: {e}")


race_results_data_2025 = pd.concat(race_results_2025, ignore_index=True)
race_laps_data_2025 = pd.concat(race_laps_2025, ignore_index=True)
race_weather_data_2025 = pd.concat(race_weather_2025, ignore_index=True)

race_results_data_2025.to_csv("2025_Race_Results.csv",index=False)
race_laps_data_2025.to_csv("2025_Race_Laps.csv", index=False)
race_weather_data_2025.to_csv("2025_Race_Weather.csv",index=False)
