mil = 1.609344

girdi = int(input("1) Kilometreyi Mil'e çevirme\n2) Mil'i kilometreye çevirme\n\nLütfen bir seçenek giriniz: "))

if girdi == 1:
    kilometreGir = int(input("Lütfen hesaplayacağınız kilometreyi giriniz: "))
    sonuc = kilometreGir / mil
    print("İşleminizin sonucu: {} Mil".format(sonuc))

if girdi == 2:
    milGir = int(input("Lütfen hesaplayacağınız mili giriniz: "))
    sonuc1 = milGir * mil
    print("İşleminizin sonucu: {} kilometre".format(sonuc1))

# python kilometer-to-mile.py
