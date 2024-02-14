# Oppgave 4
# Velger i denne oppgaven å bruke foreslått API (LocationForecast) til å beregene gjennomsnittstemperaturen for forekommende uke

from collections import defaultdict
import matplotlib.pyplot as plt
from datetime import datetime
import requests

# Definerer Api og parametere:
url = "https://api.met.no/weatherapi/locationforecast/2.0/compact"
latitude = "20"
longitude = "60"
user_header = {'User-Agent': 'Oppgave4/1.0 (dennisyeboah@live.no)'}

complete_url = f"{url}?lat={latitude}&lon={longitude}"

# Utfører Get-request:
response = requests.get(complete_url, headers=user_header)

if response.status_code == 200:
    data = response.json()
else:
    print(f"Error: {response.status_code}, {response.text}")

temp_data_per_day = defaultdict(list)
current_date = datetime.now()

# Itererer gjennom timeseries i responsdataen for å finne temperaturmålinger:
for time_series in data['properties']['timeseries']:
    forecast_date = datetime.fromisoformat(time_series['time'])
    days_difference = (forecast_date.date() - current_date.date()).days
    if 0 <= days_difference < 7:
        if 'air_temperature' in time_series['data']['instant']['details']:
            temp = time_series['data']['instant']['details']['air_temperature']
            temp_data_per_day[forecast_date.date()].append(temp)

# Beregner gjennomsnittstemperaturen for hver dag basert på temoeraturmålingene:
# (Dette gjør jeg for å få en finere graf med èn måling for hver dag)
avg_temps = []
dates = []
for date, temps in sorted(temp_data_per_day.items()):
    avg_temp = sum(temps) / len(temps)
    avg_temps.append(avg_temp)
    dates.append(date.strftime("%Y-%m-%d"))

overall_avg_temp = sum(avg_temps) / len(avg_temps)

# Bygger plot for grafisk fremstilling:
plt.figure(figsize=(6, 4))
plt.title('Langtidsvarsling av gjennomsnittstemperatur (7 dager)')
plt.ylabel('Temperatur (°C)')
plt.plot(dates, avg_temps, marker='o', linestyle='-', alpha=0.7)
plt.axhline(y=overall_avg_temp, color='r', linestyle='-', label=f'Overall Avg: {round(overall_avg_temp, 1)}°C')
plt.xticks(rotation=45)
plt.grid(True)

# Resultat:
print(f"Gjennomsnittstemperaturen for forekommende uke: {round(avg_temp, 1)}°C")
plt.show()
