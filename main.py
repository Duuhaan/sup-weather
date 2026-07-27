import requests

url = (
    "https://api.open-meteo.com/v1/forecast"
    "?latitude=36.8969"
    "&longitude=30.7133"
    "&current=temperature_2m,weather_code,wind_speed_10m"
)

response = requests.get(url)
data = response.json()

print("📍 Antalya")
print(f"🌡️ Sıcaklık: {data['current']['temperature_2m']} °C")
print(f"💨 Rüzgar: {data['current']['wind_speed_10m']} km/s")
print(f"🌤️ Hava Kodu: {data['current']['weather_code']}")
