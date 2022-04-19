import sys
katsayılar = {"mat": 6, "edeb": 5, "ing": 4, "trafik": 1, "fizik": 3}
katsayılar.update(dict.fromkeys(["alm", "tarih", "din", "geo", "kimya", "astro",
                                 "bio", "bed", "müz", "comp"], 2))
puan = 0
ders_saati = 0
while True:
    try:
        ekle = int(input("Astronomi, beden ve müzik derslerinin notları eklensin mi? (1=Evet, 0=Hayır): "))
    except ValueError:
        print("Sadece 1 ya da 0 girilebilir!")
    else:
        break
for i in katsayılar:
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
        ders_saati += katsayılar[i]
        puan += x*katsayılar[i]
    elif ekle:
        ders_saati += katsayılar[i]
        puan += 100*katsayılar[i]
ortalama = round(puan/ders_saati, 4)
print(f"ortalaman: {ortalama}")