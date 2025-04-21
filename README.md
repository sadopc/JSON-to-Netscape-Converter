# JSON Cookie to Netscape Converter

Bu küçük araç, JSON formatındaki çerezleri **Netscape HTTP Cookie** formatına dönüştürmek için yapılmıştır. Özellikle `yt-dlp` gibi araçlar için kullanışlı olabilir.

### ✨ Özellikler

- JSON çerezlerini yapıştırın ve dönüştürün  
- Netscape formatında çıktıyı alın  
- Çıktıyı kolayca panoya kopyalayın  
- Basit ve kullanımı kolay grafik arayüz (Tkinter)

### 🖥️ Nasıl Kullanılır?

1. Python 3 yüklü olduğundan emin olun.
2. Bu dosyayı çalıştırın:

```bash
python json_convert.py
```

3. Açılan pencereye JSON formatındaki çerezleri yapıştırın.
4. `Convert` butonuna basın.
5. Netscape formatındaki çıktıyı göreceksiniz. İsterseniz kopyalayabilirsiniz.

### 📝 Örnek Kullanım

JSON olarak aldığınız çerezleri `input` kısmına yapıştırın:

```json
[
  {
    "domain": "example.com",
    "hostOnly": false,
    "path": "/",
    "secure": true,
    "expirationDate": 1893456000,
    "name": "sessionid",
    "value": "abc123"
  }
]
```

Ve çıktı şöyle olur:

```
# Netscape HTTP Cookie File
# http://curl.haxx.se/rfc/cookie_spec.html
# This is a generated file! Do not edit.

.example.com	TRUE	/	TRUE	1893456000	sessionid	abc123
```

### 💬 Not

Bu proje büyük iddialar taşımaz, ama umarım birilerinin işine yarar.  
