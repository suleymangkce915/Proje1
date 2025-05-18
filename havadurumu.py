import requests



def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&lang=tr&units=metric"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        print(f"📍 Şehir: {data['name']}, {data['sys']['country']}")
        print(f"🌡️ Sıcaklık: {data['main']['temp']}°C")
        print(f"🌥️ Durum: {data['weather'][0]['description'].capitalize()}")
        print(f"💨 Rüzgar: {data['wind']['speed']} m/s")
        print(f"🌡️ Hissedilen: {data['main']['feels_like']}°C")
    else:
        print("❌ Hava durumu alınamadı. Şehir adını kontrol edin.")

if __name__ == "__main__":
    API_KEY = "BURAYA_KENDİ_API_ANAHTARINIZI_YAZIN"  # API anahtarını buraya yapıştır
    sehir = input("Hava durumunu öğrenmek istediğiniz şehir: ")
    get_weather(sehir, API_KEY)
