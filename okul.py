kat= {"mat": 6, "edebiyat": 5, "ing": 4, "sağlık ve trafik": 1, "fizik": 3}
katsayi = dict(sorted(kat.items(), key=lambda x: x[1], reverse=True))
katsayi.update(dict.fromkeys(["almanca", "tarih", "din", "coğrafya", "kimya", "astro",
                                 "biyoloji", "bed", "müz", "bilgisayar"], 2))
puan = 0
ders_saati = 0
onezero = "Sadece 1 ya da 0 girilebilir!"
onlynumb = "Sadece sayı girilebilir!"
while True:
    try:
        sec = int(input("Varsayılan dersler(0) veya katsayıları kendin yaz(1): "))
    except ValueError:
        print(onlynumb)
        continue
    if sec not in (1,0):
        print(onezero)
        continue
    break
if not sec:
    while True:
        try:
            ekle1 = int(input("Astronomi, beden ve müzik derslerinin notları eklensin mi? (1=Evet, 0=Hayır): "))
        except ValueError:
            print(onezero)
            continue
        if ekle1 not in (1,0):
            print(onezero)
        else:
            if ekle1 == 1:
                while True:
                    try:
                        ekle = int(input("Kaç tanesi eklensin? (1,2,3): "))
                    except ValueError:
                        print(onlynumb)
                        continue
                    if ekle in (1,2,3):
                        break
                    else:
                        print("Sadece 1, 2 veya 3 girilebilir!")
                break
            else:
                break
    for i in katsayi:
        if i not in ("astro", "bed", "müz"):
            print("Derslerin hesaba katılmaması için boş bırakınız.")
            while True:
                try:
                    x = input(f"{i} ortalaması: ")
                    if x != "":
                        x = float(x)
                except ValueError:
                    print(onlynumb)
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
if sec:
    while True:
        try:    
            ders_sayisi = int(input("Kaç ders gireceksin?: "))
        except ValueError:
            print(onlynumb)
            continue
        break
    for i in range(ders_sayisi):
        while True:    
            try:
                katsayi = int(input(f"\n{i+1}. Dersin katsayısı(saati): "))
                x = float(input(f"{i+1}. Dersin ortalaması: "))
            except ValueError:
                print(onlynumb)
                continue
            if x < 0 or x > 100:
                print("Sadece 0 ile 100 arasında bir not girilebilir!")
            else:
                break
        ders_saati += katsayi
        puan += x * katsayi
ortalama = round(puan/ders_saati, 4)
print(f"\nOrtalaman: {ortalama}")