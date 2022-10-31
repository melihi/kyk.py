         __ __             __
        / //_/   __  __   / /__       ____    __  __
       / ,<     / / / /  / //_/      / __ \  / / / /
      / /| |   / /_/ /  / ,<    _   / /_/ / / /_/ /
     /_/ |_|   \__, /  /_/|_|  (_) / .___/  \__, /
              /____/              /_/      /____/
              
## Açıklama
Kyk giriş portalına yoğunluktan dolayı ulaşmak oldukça zor. Portala giriş yaptıktan sonra sayfayı belirli aralıklarla yenilenmediğiniz taktirde internet kesilmekte . Sayfayı yenilediğiniz anda internet geri gelmektedir . Bu sorunları aşmak için python + selenium ile geliştirilmiş bir araçtır .

## Özellikler
- Otomatik giriş yapma kabiliyeti
  - Zaten giriş yapılmışsa bunu algılar
- 5 saniyede bir sayfayı yeniler
- Herhangi bir hata sonucunda Chrome driver otomatik şekilde yeniden başlatılır
- Kullanıcı aracı sonlandırmak için ctrl+c kombinasyonuna bastığında Kyk portalında oturum sonlandırılır .


## Kurulum && Kullanım
- Chrome webdriver'ı indirin => https://chromedriver.chromium.org/


- Python bağımlılıklarını kurunuz
```bash
pip3 install selenium

```
- Kaynak kodun içerisine kullanıcı adı , parolayı girin
- python3 kyk.py
