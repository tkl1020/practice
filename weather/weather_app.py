import tkinter as tk
from tkinter import messagebox
import requests

def get_weather(city_name, api_key):
    base_url = "http://api.weatherstack.com/current"
    params = {
        "access_key": api_key,
        "query": city_name
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        if "error" in data:
            return f"API Error: {data['error']['info']}"
        return (
            f"Weather in {data['location']['name']}, {data['location']['country']}:\n"
            f"Temperature: {data['current']['temperature']}°C\n"
            f"Condition: {data['current']['weather_descriptions'][0]}\n"
            f"Humidity: {data['current']['humidity']}%\n"
            f"Wind Speed: {data['current']['wind_speed']} km/h"
        )
    else:
        return f"Error fetching data: {response.status_code} - {response.text}"

def show_weather():
    city = city_entry.get()
    if not city:
        messagebox.showerror("Input Error", "Please enter a city name.")
        return
    api_key = '83e8f1d205047ef21026c3c9fd67056b'
    if not api_key:
        messagebox.showerror("Input Error", "Please enter your API key.")
        return
    result = get_weather(city, api_key)
    messagebox.showinfo("Weather Info", result)

# Create the GUI application
app = tk.Tk()
app.title("Weather App")

tk.Label(app, text="Enter City Name:").pack(pady=5)
city_entry = tk.Entry(app, width=30)
city_entry.pack(pady=5)

tk.Label(app, text="Enter API Key:").pack(pady=5)
api_key_entry = tk.Entry(app, width=30, show="*")
api_key_entry.pack(pady=5)

tk.Button(app, text="Get Weather", command=show_weather).pack(pady=20)

app.mainloop()
