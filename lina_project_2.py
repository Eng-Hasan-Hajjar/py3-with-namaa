# Öğrenci bilgileri için sözlük
ogrenciler = {
    "1001": {"isim": "Lina", "yas": 20, "bolum": "Bilgisayar Mühendisliği", "not_ortalamasi": 3.4},
    "1002": {"isim": "Ali", "yas": 22, "bolum": "Makine Mühendisliği", "not_ortalamasi": 2.8},
    "1003": {"isim": "Sara", "yas": 21, "bolum": "Matematik", "not_ortalamasi": 3.9},
}
def ogrenci_listele():
    print("\n📋 Öğrenci Listesi:")
    for id, bilgi in ogrenciler.items():
        print(f"ID: {id} | İsim: {bilgi['isim']} | Bölüm: {bilgi['bolum']} | Not Ortalaması: {bilgi['not_ortalamasi']}")
def ogrenci_ekle():
    id = input("Yeni öğrenci ID'si giriniz: ")
    isim = input("Öğrenci ismi: ")
    yas = int(input("Öğrenci yaşı: "))
    bolum = input("Öğrenci bölümü: ")
    not_ortalamasi = float(input("Not ortalaması: "))
    ogrenciler[id] = {"isim": isim, "yas": yas, "bolum": bolum, "not_ortalamasi": not_ortalamasi}
    print("✅ Öğrenci eklendi.")
def ogrenci_ara():
    id = input("Aranacak öğrenci ID'si: ")
    if id in ogrenciler:
        print(f"🔍 Öğrenci Bilgileri: {ogrenciler[id]}")
    else:
        print("❌ Öğrenci bulunamadı.")
def not_guncelle():
    id = input("Notu güncellenecek öğrenci ID'si: ")
    if id in ogrenciler:
        yeni_not = float(input("Yeni not ortalaması: "))
        ogrenciler[id]['not_ortalamasi'] = yeni_not
        print("✅ Not güncellendi.")
    else:
        print("❌ Öğrenci bulunamadı.")
def ogrenci_sil():
    id = input("Silinecek öğrenci ID'si: ")
    if id in ogrenciler:
        del ogrenciler[id]
        print("🗑️ Öğrenci silindi.")
    else:
        print("❌ Öğrenci bulunamadı.")
def menu():
    while True:
        print("\nLütfen bir işlem seçiniz:")
        print("1 - Öğrenci Listele")
        print("2 - Öğrenci Ekle")
        print("3 - Öğrenci Ara")
        print("4 - Not Güncelle")
        print("5 - Öğrenci Sil")
        print("6 - Çıkış")
        secim = input("Seçiminiz: ")
        if secim == "1":
            ogrenci_listele()
        elif secim == "2":
            ogrenci_ekle()
        elif secim == "3":
            ogrenci_ara()
        elif secim == "4":
            not_guncelle()
        elif secim == "5":
            ogrenci_sil()
        elif secim == "6":
            print("Programdan çıkılıyor, görüşürüz! 👋")
            break
        else:
            print("❌ Geçersiz seçim, lütfen tekrar deneyin.")
if __name__ == "_main_":
    menu()