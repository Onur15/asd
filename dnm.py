kat= {"mat": 6, "edebiyat": 5, "ing": 4, "sağlık ve trafik": 1, "fizik": 3}
katsayi = dict(sorted(kat.items(), key=lambda x: x[1], reverse=True))
katsayi.update(dict.fromkeys(["almanca", "tarih", "din", "coğrafya", "kimya", "astro",
                                 "biyoloji", "bed", "müz", "bilgisayar"], 2))
puan = 0
ders_saati = 0
while True:
    try:
        ekle = int(input("Astronomi, beden ve müzik derslerinin notları eklensin mi? (1=Evet, 0=Hayır): "))
    except ValueError:
        print("Sadece 1 ya da 0 girilebilir!")
        continue
    if ekle not in (1,0):
        print("Sadece 1 ya da 0 girilebilir!")
    else:
        if ekle == 1:
            while True:
                try:
                    ekle = int(input("Kaç tanesi eklensin? (1,2,3): "))
                except ValueError:
                    print("Sadece sayı girilebilir!")
                if ekle in (1,2,3):
                    break
                else:
                    print("Sadece 1, 2 veya 3 girilebilir!")
            break
        else:
            break
for i in katsayi:
    if i not in ("astro", "bed", "müz"):
        while True:
            try:
                x = input(f"{i} ortalaman: ")
                if x != "":
                    x = float(x)
            except ValueError:
                print("Sadece sayı girilebilir!")
                continue
            if x == "" or (x>=0 and x<=100):
                break
            if x>100 or x<0:
                print("Sadece 100 ile 0 arasında bir not girilebilir!")
        if x == "":
            continue
        ders_saati += katsayi[i]
        puan += x * katsayi[i]
    elif ekle:
        ekle -= 1
        ders_saati += katsayi[i]
        puan += 100 * katsayi[i]
ortalama = round(puan/ders_saati, 4)
print(f"ortalaman: {ortalama}")