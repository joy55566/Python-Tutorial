import tkinter as tk
from tkinter import messagebox
import requests
import json

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather App")
        self.root.geometry("400x300")
        
        # API key (you'll need to get your own from OpenWeatherMap)
        self.api_key = "YOUR_API_KEY"
        
        # Create GUI elements
        self.city_label = tk.Label(root, text="Enter City Name:")
        self.city_label.pack(pady=10)
        
        self.city_entry = tk.Entry(root, width=30)
        self.city_entry.pack(pady=5)
        
        self.search_button = tk.Button(root, text="Search", command=self.get_weather)
        self.search_button.pack(pady=10)
        
        self.result_label = tk.Label(root, text="", wraplength=350)
        self.result_label.pack(pady=20)
    
    def get_weather(self):
        city = self.city_entry.get()
        if not city:
            messagebox.showwarning("Warning", "Please enter a city name!")
            return
        
        if self.api_key == "YOUR_API_KEY":
            self.result_label.config(text="Please add your OpenWeatherMap API key in the code!")
            return
            
        try:
            # Make API request
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}&units=metric"
            response = requests.get(url)
            data = json.loads(response.text)
            
            if response.status_code == 200:
                # Extract weather information
                temp = data['main']['temp']
                humidity = data['main']['humidity']
                desc = data['weather'][0]['description']
                
                # Update result label
                result = f"Temperature: {temp}°C\nHumidity: {humidity}%\nConditions: {desc.capitalize()}"
                self.result_label.config(text=result)
            else:
                self.result_label.config(text="City not found!")
                
        except Exception as e:
            self.result_label.config(text="Error fetching weather data!")

def main():
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
