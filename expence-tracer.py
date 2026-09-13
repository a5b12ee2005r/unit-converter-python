
# import requests

# API_KEY = "YOUR_API_KEY_HERE"  # Paste your key here
# BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


# def fetch_weather(city_name):
#     # Request parameters (metric gives Celsius)
#     params = {
#         'q': city_name,
#         'appid': API_KEY,
#         'units': 'metric'
#     }
#     try:
#         response = requests.get(BASE_URL, params=params)
#         data = response.json()

#         if response.status_code == 200:
#             temp = data['main']['temp']
#             desc = data['weather'][0]['description']
#             print(f"\nWeather in {city_name.title()}:")
#             print(f"- Temperature: {temp}°C")
#             print(f"- Condition: {desc.capitalize()}")
#         else:
#             print(f"City '{city_name}' not found.")
#     except Exception as e:
#         print(f"Error connecting to the weather service: {e}")


# def get_single_weather():
#     city = input("Enter city name: ")
#     fetch_weather(city)


# def get_multiple_weather():
#     cities_input = input("Enter cities separated by commas (e.g., London, Tokyo, New York): ")
#     # Split string by comma and remove extra spaces
#     cities_list = [city.strip() for city in cities_input.split(',')]

#     for city in cities_list:
#         if city:  # Check if name isn't empty
#             fetch_weather(city)


# def main_menu():
#     while True:
#         print("\n==== WEATHER APP: MAIN MENU ====")
#         print("1. Single City Weather")
#         print("2. Multiple City Weather")
#         print("3. Exit")

#         choice = input("Enter your choice (1-3): ")

#         if choice == '1':
#             get_single_weather()
#         elif choice == '2':
#             get_multiple_weather()
#         elif choice == '3':
#             print("Exiting application. Goodbye!")
#             break
#         else:
#             print("Invalid choice. Please try again.")


# if __name__ == "__main__":
#     main_menu()












































































