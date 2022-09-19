import requests
import smtplib

ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = "your key"
your_email = ""
your_password = ""

parameters = {
    "lat": -25.09,
    "lon": -50.16,
    "appid": API_KEY
}

response = requests.get(url=ENDPOINT, params=parameters)
response.raise_for_status()
weather_data = response.json()["list"][:3]
it_rains = False
for data in weather_data:
    if data['weather'][0]["id"] < 700:
        it_rains = True

if it_rains:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=your_email, password=your_password)
        connection.sendmail(
            from_addr=your_email,
            to_addrs=your_email,
            msg="Subject:It'll rain today\n\nBetter have an umbrella")
