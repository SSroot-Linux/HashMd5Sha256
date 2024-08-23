import hashlib
import time
import pyfiglet

foto = pyfiglet.figlet_format("Mr Gestalt")

time.sleep(1)

print("Büyük ve küçük harfe Duyarlıdır!!!")

print(foto)
def sifre():
    tur = input("Şifreleme Türünü Seçiniz (md5/sha256):  ")
    metin = input("Şifrelemek İstediğin Metni Giriniz:  ")
    
    if tur == "sha256":
        sifrelenmis = hashlib.sha256(metin.encode()).hexdigest()
        print(f"Ana Metin: {metin}")
        time.sleep(1)
        print(f"Şifrelenmiş Mesaj: {sifrelenmis}")
        time.sleep(1)                 
    elif tur == "md5":
        sifrelenmis = hashlib.md5(metin.encode()).hexdigest()
        print(f"Ana Metin: {metin}")
        time.sleep(1)
        print(f"Şifrelenmiş Mesaj: {sifrelenmis}")
while True:
    try:
        time.sleep(1)
        evha = input("Metin Şifrelemek istiyormusunuz (e/h):  ")
        if evha == "e":
            time.sleep(1)
            sifre()
            time.sleep(1)    
        elif evha == "h":
            print("Koddan Çıkılıyor...")  
            time.sleep(1)
            break                        
    except:
        print("Hata")
