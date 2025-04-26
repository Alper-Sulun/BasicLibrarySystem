# 📚 Kütüphane Sistemi Projesi

## 1️⃣ GİRİŞ

### 1.1 Projenin Amacı
Bu proje, **nesne yönelimli programlama (OOP)** prensiplerini pekiştirmek amacıyla bir **kütüphane sistemi** oluşturulmasını hedefler. 🎯

## 2️⃣ GEREKSİNİM ANALİZİ

### 2.1 Arayüz Gereksinimleri
Kullanıcı, kullandığı IDE'nin terminalinde gerekli işlemleri yapabilmesini sağlayan basit bir **menü arayüzü** sağlanacaktır. 🖥️

### 2.2 Fonksiyonel Gereksinimler
- ➕ **Kütüphaneye kitap eklemek**
- ➖ **Kütüphaneden kitap silmek**
- 🔍 **Kütüphanede isme göre kitap aramak**
- ✒️ **Kütüphanede yazara göre kitap aramak**
- 📜 **Kütüphanedeki kitapları listelemek**
- ❌ **Uygulamadan kolayca çıkış yapabilmek**

### 2.3 Use-Case Diyagramı
*(Buraya proje ile ilgili bir Use-Case diyagramı ekleyebilirsiniz.)*

## 3️⃣ TASARIM

### 3.1 Mimari Tasarım
Proje, **Nesneye Yönelik Programlama (OOP)** prensiplerine uygun olarak yazılmıştır. İçinde bilgi (isim, yazar, tarih) tutabilen `Book` sınıfı ve bu sınıfın nesnelerini tutabilen `Library` sınıfı bulunmaktadır. 🏛️

### 3.2 Kullanılacak Teknolojiler
- **Python 3** 🐍

### 3.3 Veri Tabanı Tasarımı
*(Buraya veri tabanı tasarımı ve yapısı hakkında bilgi ekleyebilirsiniz.)*

### 3.4 Kullanıcı Arayüzü Tasarımı
Proje, basit bir **konsol arayüzü** üzerinden çalışmaktadır. Kullanıcı, kitap ekleme, silme, sıralama ve listeleme gibi işlemleri bu arayüz üzerinden gerçekleştirebilir. 🎮

### 3.5 Çalıştırma
Python 3 yüklü bir bilgisayarda, uygun bir kod editörü kullanarak veya dosyayı çift tıklayarak program çalıştırılabilir. 🚀

## 4️⃣ UYGULAMA

### 4.1 Kodlanan Bileşenlerin Açıklamaları

#### `Book` Sınıfı 📖
- `__init__(self, name, author, year)`: Kitap bilgilerini (isim, yazar, yıl) alır.
- `getName()`: Kitap ismini döndürür.
- `getAuthor()`: Kitap yazarını döndürür.
- `getYear()`: Kitap basım yılını döndürür.
- `setName()`: Kitap ismini değiştirir.
- `setAuthor()`: Kitap yazarını değiştirir.
- `setYear()`: Kitap basım yılını değiştirir.
- `__str__()`: Kitap bilgilerini (isim, yazar, yıl) konsola yazdırır.

#### `Library` Sınıfı 🏫
- `__init__(self)`: Kitapların listesini başlatır.
- `add_book(book)`: Kitap ekler.
- `remove_book(book_name)`: Kitap siler.
- `search_by_name(name)`: İsimle kitap arar.
- `search_by_author(author)`: Yazara göre kitap arar.
- `list_books()`: Kitap listesini yazdırır.
- `autoTests()`: Otomatik testleri çalıştırır.
- `manualTest()`: Manuel testlere olanak sağlar.

### 4.2 Görev Dağılımı 📊
Projede görevler, eşit iş yükü oluşturacak şekilde dağıtılmış olup her birey kendine düşen görevleri yerine getirmiştir. 💪

### 4.3 Karşılaşılan Zorluklar ve Çözüm Yöntemleri 🤔
Geliştirme sürecinde herhangi bir zorluk yaşanmamıştır. 🚀

### 4.4 Proje İsterlerine Göre Eksik Yönler ⚠️
Projede, belirtilen tüm gereksinimler eksiksiz bir şekilde gerçekleştirilmiştir. ✅

## 5️⃣ TEST VE DOĞRULAMA

### 5.1 Yazılımın Test Süreci 🧪
- `autoTests()` fonksiyonu ile `Library` sınıfının tüm fonksiyonları otomatik olarak test edilmektedir. Testler, konsola yazdırılan çıktılarla doğrulanır. 🖨️
- `manualTest()` fonksiyonu ile `Library` ve `Book` sınıfının tüm özellikleri manuel olarak test edilebilir. 🔧
- Bu iki test arasında istenilen zaman diliminde geçiş yapılabilir. 🔄

### 5.2 Yazılımın Doğrulanması ✔️
Tüm testler yapılmış olup, hiçbir hataya rastlanmamış ve istenilen sonuçlar başarıyla elde edilmiştir. 🎉


