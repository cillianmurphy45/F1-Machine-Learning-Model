import fastf1
import pandas as pd
fastf1.Cache.enable_cache("cache")


schedule_2024 = fastf1.get_event_schedule(2024, include_testing=False)

schedule_2025 = fastf1.get_event_schedule(2025, include_testing=False)

schedule_2024 = schedule_2024[["RoundNumber", "EventDate", "EventName"]]

schedule_2025 = schedule_2025[["RoundNumber", "EventDate", "EventName"]]


# Getting 2024, 2025 Qualifying Data
# Creating empty list to store all results from qualidying from 2024 data
qualifying_results_2024 = []
qualifying_weather_2024 = []


# Looping throggh schedule to get each round's qualifying data
for x in range(1, len(schedule_2024) + 1):
    try:
        qualy_session_2024 = fastf1.get_session(2024, x, "Q")
        qualy_session_2024.load(telemetry=False, laps=False)

        qualy_results_2024 = qualy_session_2024.results
        qualy_results_2024["RoundNumber"] = x

        qualy_weather_data_2024 = qualy_session_2024.weather_data
        qualy_weather_data_2024["RoundNumber"] = x

        qualifying_results_2024.append(qualy_results_2024)
        qualifying_weather_2024.append(qualy_weather_data_2024)


    except Exception as e:
        print(f"Could not get data for Round {x}, because: {e}")


qualifying_results_data_2024 = pd.concat(qualifying_results_2024, ignore_index=True)
qualifying_weather_data_2024 = pd.concat(qualifying_weather_2024, ignore_index=True)

qualifying_results_data_2024.to_csv("2024_Qualifying_Results.csv", index=False)
qualifying_weather_data_2024.to_csv("2024_Qualifying_Weather.csv",index=False)

qualifying_results_2025 = []
qualifying_weather_2025 = []

# Looping throggh schedule to get each round's qualifying data
for y in range(1, len(schedule_2025 ) + 1):
    try:
        qualy_session_2025 = fastf1.get_session(2025, y, "Q")
        qualy_session_2025.load(telemetry=False, laps=False)

        qualy_results_2025 = qualy_session_2025.results
        qualy_results_2025["RoundNumber"] = y

        qualy_weather_data_2025 = qualy_session_2025.weather_data
        qualy_weather_data_2025["RoundNumber"] = y


        qualifying_results_2025.append(qualy_results_2025)
        qualifying_weather_2025.append(qualy_weather_data_2025)

    except Exception as e:
        print(f"Could not get data for Round {y}, because: {e}")


qualifying_results_data_2025 = pd.concat(qualifying_results_2025, ignore_index=True)
qualifying_weather_data_2025 = pd.concat(qualifying_weather_2025, ignore_index=True)

qualifying_results_data_2025.to_csv("2025_Qualifying_Results.csv", index=False)
qualifying_weather_data_2025.to_csv("2025_Qualifying_Weather.csv", index=False)