#Başlıyoruz ..
import fig
import requests #verileri çekmek için gerekli olan kütüphanemiz. (sorgulayıcı)/#our library, which is necessary to extract data.
import gmaps #harita çıkarmak için gerekli olan kütüphanemiz. (google maps) /# our library that is necessary to map.

address = input("Aramak istediğiniz lokasyonu giriniz./ Enter the location you want to search.") #Öncelikle bir veri almalıyızki onu işleyelim.
#verimizi daha kolay işlemek için bir değişkene atıyoruz.

def get_lat_lng(apiKey, address): #2 farklı fonksiyon belirliyoruz.
    global output_address
    url = ('https://maps.googleapis.com/maps/api/geocode/json?address={}&key={}'
           .format(address.replace(' ', '+'), apiKey)) #Sonucu bir yere getirmek için json formatında bir url kullanıyoruz.
    try:
        response = requests.get(url) #url deki değerleri en baştaki requests kütüphanesi sayesinde sorguluyoruz./#We query values ​​in url with the requests library at the very beginning.
        resp_json_payload = response.json() #Hatırlarsanız URL miz json formatındaydı.önceki koddaki sorgudan çekdiğimiz değeri json olarak ayarlıyoruz. #If you remember, our URL was in json format. We set the value we got from the query in the previous code to json.
        output_address = resp_json_payload["results"][0]["formatted_address"]
        lat = resp_json_payload['results'][0]['geometry']['location']['lat'] #Burda lokasyonumuzun geometrik değerlerini lat türünden alıyoruz.
        lng = resp_json_payload['results'][0]['geometry']['location']['lng'] #Burda lokasyonumuzun geometrik değerlerini lng türünden alıyoruz.
        gmaps.configure(api_key=apiKey)
        location = (lat, lng) #lat ve lng değerlerini lokasyon değerine aktarıyoruz.
        fig = gmaps.figure(center=location, zoom_level=15) #orta merkezi lokasyon olarak seçiyoruz ve yakınlaştırmayı 15 yapıyoruz ki daha dinamik olsun.

    except: #Bir hatamız olursa diye bir dönüt yazıyoruz.
        print('HATA: Lokasyon bulunamadı.'.format(address))
        lat = 0
        lng = 0
    return lat, lng, output_address, fig


if __name__ == '__main__':
    apiKey = "AIzaSyCDZL2FgtBHUDJf-SVH9JvnUKqpyYuJNk8" #kendi apiKeyinizi buraya yapıştırın.

    lat, lng = get_lat_lng(apiKey, address)
    print('Coordinates:\nLatitude:  {}°\nLongitude: {}°\nAddress:{}'.format(lat, lng, output_address))
fig  # Show map