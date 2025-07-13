
import requests
import matplotlib.pyplot as plt
import seaborn as sns

# Constants
API_KEY = '8b0bbe4d7573d5160b06148bb45580c5'  # Replace with your actual API key
CITY = 'Chennai'
DAYS = 5  # Number of days of forecast
BASE_URL = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

# Fetching data from API
def fetch_weather_data():
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Failed to retrieve data")
        return None

# Parse and prepare data
def prepare_data(weather_data):
    forecast_list = weather_data['list']
    dates = []
    temps = []
    humidity = []

    for entry in forecast_list:
        dates.append(entry['dt_txt'])
        temps.append(entry['main']['temp'])
        humidity.append(entry['main']['humidity'])

    return dates, temps, humidity

# Visualization
def create_visualizations(dates, temps, humidity):
    sns.set(style="whitegrid")

    # Temperature Plot
    plt.figure(figsize=(12, 5))
    plt.plot(dates, temps, marker='o', color='orange')
    plt.xticks(rotation=45)
    plt.title(f"Temperature Forecast for {CITY}")
    plt.xlabel("Date and Time")
    plt.ylabel("Temperature (°C)")
    plt.tight_layout()
    plt.grid(True)
    plt.savefig("temperature_plot.png")
    plt.show()

    # Humidity Plot
    plt.figure(figsize=(12, 5))
    plt.plot(dates, humidity, marker='s', color='blue')
    plt.xticks(rotation=45)
    plt.title(f"Humidity Forecast for {CITY}")
    plt.xlabel("Date and Time")
    plt.ylabel("Humidity (%)")
    plt.tight_layout()
    plt.grid(True)
    plt.savefig("humidity_plot.png")
    plt.show()

# Main

if __name__ == "__main__":
    data = fetch_weather_data()
    if data:
        dates, temps, humidity = prepare_data(data)
        create_visualizations(dates[:15], temps[:15], humidity[:15])  # limiting to 15 for clarity
