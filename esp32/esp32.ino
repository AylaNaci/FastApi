#include <WiFi.h> // WiFi kütüphanesini dahil et
#include <HTTPClient.h> // HTTP istemci kütüphanesini dahil et

const char* ssid = "calisma_salonu2"; // WiFi ağ adı (SSID)
const char* password = "12345678"; // WiFi şifresi

void setup() {
  Serial.begin(115200); // Seri iletişimi 115200 baud hızında başlat
  WiFi.begin(ssid, password); // WiFi'ye bağlanmayı başlat

  while (WiFi.status() != WL_CONNECTED) { // WiFi bağlantısı kurulana kadar bekle
    delay(1000); // 1 saniye bekle
    Serial.println("Connecting to WiFi..."); // WiFi'ye bağlanılıyor mesajı yazdır
  }

  Serial.println("Connected to WiFi"); // WiFi'ye bağlanıldı mesajı yazdır
  sendRequest(); // HTTP isteği gönder
}

void sendRequest() {
  if (WiFi.status() == WL_CONNECTED) { // WiFi'ye bağlıysa
    HTTPClient http; // HTTP istemci nesnesi oluştur
    http.begin("http://192.168.1.130:8000/kayit"); // HTTP isteği için URL belirle
    int httpResponseCode = http.GET(); // GET isteği gönder ve yanıt kodunu al

    if (httpResponseCode > 0) { // Yanıt kodu pozitifse (başarılı)
      String response = http.getString(); // Yanıtı string olarak al
      Serial.println(httpResponseCode); // Yanıt kodunu yazdır
      Serial.println(response); // Yanıt içeriğini yazdır
    } else {
      Serial.print("Error on sending GET request: "); // GET isteği gönderme hatası mesajı yazdır
      Serial.println(httpResponseCode); // Hata kodunu yazdır
    }

    http.end(); // HTTP bağlantısını sonlandır
  } else {
    Serial.println("WiFi not connected"); // WiFi bağlı değil mesajı yazdır
  }
}

void loop() {
  // Ana kodunuzu buraya yazın, tekrar tekrar çalışacak
}