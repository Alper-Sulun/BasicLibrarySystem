📝 Metin Manipülasyonu ve Yazma Hızı Uygulaması
📚 Proje Tanımı
Bu proje, kullanıcıların bir metin üzerinde çeşitli manipülasyon işlemleri yapabilmesini ve yazı yazma hızını ölçebilmesini sağlayan arayüzlü bir uygulamadır.

📑 İçindekiler
🎯 Proje Amacı

🛠️ Gereksinim Analizi

🎨 Tasarım

🧩 Uygulama

▶️ Kullanım Adımları

🎯 Proje Amacı
🖊️ Metin üzerinde çeşitli manipülasyonlar yapmak.

⏱️ Yazı yazma hızını hesaplamak.

🖥️ Tüm işlemleri kullanıcı dostu bir görsel arayüz üzerinden gerçekleştirmek.

🛠️ Gereksinim Analizi
🖼️ Arayüz Gereksinimleri
Metin Girişi: Kullanıcı metin girebilmeli.

Fonksiyon Seçimi: Kullanıcı listeden bir fonksiyon seçebilmeli.

Zamanlayıcı: Yazma hızını ölçmek için zamanlayıcı başlatılıp durdurulabilmeli.

⚙️ Fonksiyonel Gereksinimler
🔤 Alta Alta Yazdırma: Metni harf harf alt alta yazdırır.

🔁 Orijinal ve Ters: Metnin hem orijinal hem de ters halini gösterir.

🅰️ Büyük A: Küçük "a" harflerini büyük "A" harfine dönüştürür.

📋 Ayrı Ayrı Yazma: Kelimeleri liste halinde ayırır.

🔗 Birleştirme: Metindeki boşlukları kaldırarak kelimeleri birleştirir.

🔢 Ünlü Sayma: Metindeki ünlü harflerin sayısını hesaplar.

🎨 Tasarım
🏛️ Mimari Tasarım
Proje, Model-View-Controller (MVC) mimarisiyle geliştirilmiştir:

Model: 📜 Metin işleme ve çıktı üretme işlemlerini içerir.

View: 🎨 Tkinter ile oluşturulmuş kullanıcı arayüzü.

Controller: 🎛️ Kullanıcı etkileşimlerini yönetir ve ilgili modeli tetikler.

🧰 Kullanılan Teknolojiler
🐍 Python

🖼️ Tkinter (GUI oluşturmak için)

🖌️ Kullanıcı Arayüzü Tasarımı
Arayüz sade ve işlevseldir:

✍️ Metin girişi yapılır.

✅ Fonksiyon seçimi yapılır.

📋 Sonuçlar çıktı alanında görüntülenir.

⏱️ Yazı hızı zamanlayıcısı kullanılabilir.

🧩 Uygulama
📦 Kod Yapısı
MyGUI sınıfı: Tkinter bileşenleri ve uygulama mantığını içerir.

applyFunction: Seçilen fonksiyonu uygular ve sonucu gösterir.

deleteFunction: Metin giriş ve çıktı alanlarını temizler.

altAltaYazdirma: Her harfi alt alta yazdırır.

orjinalTers: Metnin orijinal ve ters versiyonlarını yazdırır.

buyukA: Küçük "a" harflerini büyük "A" harfine dönüştürür.

ayriAyri: Kelimeleri liste haline getirir.

birlestirme: Metindeki boşlukları kaldırır.

kacUnlu: Ünlü harflerin sayısını hesaplar.

yaziHizi: Yazı yazma hızını ölçer.

keyPressed: Enter tuşu ile zamanı kaydeder ve hızı hesaplar.

⚡ Karşılaşılan Zorluklar ve Çözüm Yöntemleri
🔧 Tkinter grid yöntemi ile yerleşimde problemler yaşanmıştır. Bu sorun frame yapıları kullanılarak çözülmüştür.

✅ Proje İsterlerine Göre Durum
Proje isterlerinin tamamı başarıyla gerçekleştirilmiştir.

▶️ Kullanım Adımları
🚀 Uygulamayı çalıştırın.

🎯 "Choose Function" kısmından bir fonksiyon seçin.

✍️ "Enter your text" kısmına metninizi girin.

🔨 "Apply Function" butonuna basın.

📋 Sonuçları çıktı alanında görüntüleyin.

⏱️ Yazı hızını ölçmek için "Start Timer" butonuna basın ve yazmayı bitirdiğinizde Enter tuşuna basın.

