import requests

def get_weather(city):
    API_KEY = "2e51e07c599ea6b194a039e92020dfbe"

    URL = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(URL)

        if response.status_code == 200:
            data = response.json()

            print(f"\nWeather in {data['name']}, {data['sys']['country']}")
            print(f"Temperature : {data['main']['temp']} °C")
            print(f"Humidity    : {data['main']['humidity']} %")
            print(f"Weather     : {data['weather'][0]['description']}")
            print(f"Wind Speed  : {data['wind']['speed']} m/s")

        else:
            print(f"City '{city}' not found. Please try again.")

    except Exception as e:
        print("Something went wrong:", e)


if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)