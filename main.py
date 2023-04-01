import random

print("Sayı Tahmin Oyununa Hoş Geldiniz!")

# Rastgele bir sayı oluşturma
sayi = random.randint(1, 20)

# Kullanıcının tahmin etmesi için 6 şansı var
for tahmin_hakki in range(1, 7):
  print("{}. tahmininiz: ".format(tahmin_hakki), end='')
  tahmin = int(input())

  # Tahminin doğruluğunu kontrol etme
  if tahmin < sayi:
    print("Daha yüksek bir sayı söyleyin.")
  elif tahmin > sayi:
    print("Daha düşük bir sayı söyleyin.")
  else:
    break

# Sonuçları kullanıcıya gösterme
if tahmin == sayi:
  print("Tebrikler! {} sayısını {} tahmininde buldunuz.".format(
    sayi, tahmin_hakki))
else:
  print("Maalesef, {} sayısını tahmin edemediniz. Sayı {} idi.".format(
    tahmin_hakki, sayi))
