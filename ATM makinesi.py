print("""*******
ATM Makinesine Hoşgeldiniz.
İşlemler;
1. Bakiye Sorgulama
2. Para Yatırma
3. Para Çekme
Programdan çıkmak için 'q'ya basın.
*******
""")

sifre=3467
tekrar_hakki=3
bakiye=1000


while True:
    girilen_sifre = int(input("Şifrenizi giriniz:"))
    if girilen_sifre==sifre:
        print("**Giriş Başarılı, Ana Menüye Yönlendiriliyorsunuz**")
        break
    elif (tekrar_hakki>=1 and girilen_sifre!=sifre):
        tekrar_hakki-=1
        if tekrar_hakki!=0:
            print("Şifreniz Yanlış Lütfen Tekrar Giriniz.")
            print("{} Giriş Hakkınız Kalmıştır".format(tekrar_hakki))

    if tekrar_hakki==0:
         print("3 Kere yanlış şifre girdiniz. Kartınız Bloke Edilmiştir.")
         break

if girilen_sifre==sifre:

    while True:
        islem=input("Yapmak İstediğiniz İşlemi Giriniz:")
        if islem=="Para Yatırma":
            yatirma=int(input("Yatırmak İstediğiniz Değeri Giriniz:"))
            print("Para Yatırma İşlemi Başarılı\nYeni Bakiyeniz:{}".format(yatirma+bakiye))
            print("Çıkmak için q'ya basın.")
            bakiye=yatirma+bakiye
        elif islem=="Para Çekme":
            cekme=int(input("Çekmek İstediğiniz Değeri Giriniz:"))
            if cekme<=bakiye:
                print("Para Çekme İşlemi Başarılı, Çekilen Tutar:{}tl\nHesapta Kalan Tutar:{}tl".format(cekme,bakiye-cekme))
                print("Çıkmak için q'ya basın.")
                bakiye=bakiye-cekme
            else:
                print("***Lütfen {}TL'den düşük bir tutar girin.***".format(bakiye))
                print("Çıkmak için q'ya basın.")
        elif islem=="Bakiye Sorgulama":
            print("Bakiyeniz {}TL'dir.".format(bakiye))
            print("Çıkmak için q'ya basın.")
        elif islem=="q":
            print("Kartınız İade Ediliyor...\nİyi Günler Dileriz...")
            break
