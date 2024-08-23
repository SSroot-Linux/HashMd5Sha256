#Öncelikle Gerekli Kütüphaneyi Ekleyelim Sonra Mesajı alalım ondan sonra şifreleyelim 2 tür olsun şifrelemek ve decode etmek başlayalım
import hashlib
import base64
import pyfiglet
import time

time.sleep(1)

yazi = pyfiglet.figlet_format("  ^HASHer^ ")

time.sleep(1)

print(yazi)

time.sleep(1)

print("""

1-) Encode(sha1,sha256,md5,bs64, sha3_256, hexdenc)

2-) Decode(Base64,)

3-) Koddan çık
""")

def Bs64Encode():
    veri = input("Şifrelemek İstediğiniz Mesajı Yazınız: ")
    time.sleep(1)
    enc = base64.b64encode(veri.encode())
    time.sleep(1)
    print(f"Şifrelenmiş Metin: {enc.decode()}")
    time.sleep(1)
    print("Bitti")
    
def Bs64Decode():
    veri2 = input("Şifresini Decode Etmek istediğiniz mesajı giriniz:  ")
    time.sleep(1)
    dec = base64.b64decode(veri2)
    time.sleep(1)
    print(f"Orjinal Şifre:{dec.decode()}")


def hexenc():
    time.sleep(1)
    mesaj = input("Şifrelemek İstediğin Mesajı gir: ")
    sifre = hex(mesaj)
    
    time.sleep(1)
    
    print(f"Şifrelenmiş Metin: {sifre}")

def hexdec():
    time.sleep(1)
    mesaj = input("Şifrelemek İstediğin Mesajı gir: ")
    sifre = int(mesaj, 16)
    
    time.sleep(1)
    
    print(f"Şifrelenmiş Metin: {sifre}")

def sha3_256():
    time.sleep(1)
    mesaj = input("Şifrelemek İstediğin Mesajı gir: ")
    sifre = hashlib.sha3_256(mesaj.encode()).hexdigest()
    
    time.sleep(1)
    
    print(f"Şifrelenmiş Metin: {sifre}")


def Md5():
        time.sleep(1)
        mesaj = input("Şifrelemek İstediğin Mesajı gir:  ")
        sifre = hashlib.md5(mesaj.encode()).hexdigest()
        time.sleep(1)
        print(f"Şifrelenmiş Metin:{sifre}")
        
        
def Sha1():
    time.sleep(1)
    mesaj = input("Şifrelemek İstediğin Mesajı gir: ")
    sifre = hashlib.sha1(mesaj.encode()).hexdigest()
    
    time.sleep(1)
    
    print(f"Şifrelenmiş Metin: {sifre}")
        

def Sha256():
    time.sleep(1)
    mesaj = input("Şifrelemek İstediğin Mesajı gir: ")
    sifre = hashlib.sha256(mesaj.encode()).hexdigest()
    
    time.sleep(1)
    
    print(f"Şifrelenmiş Metin: {sifre}")    

while True:
    try:
        time.sleep(1)
        secim = input("Seçimin: ")
        if secim == "1":
            time.sleep(1)
            soru = input("Şifre Türünü Seç (md5/sha256/sha1/bs64/sha3_256): ")
            time.sleep(1)
            if soru == "md5":
                time.sleep(1)
                Md5()
                time.sleep(1)
            elif soru == "sha1":
                time.sleep(1)
                Sha1()
                time.sleep(1)
            elif soru == "sha256":
                time.sleep(1)
                Sha256()
                time.sleep(1)
            elif soru == "sha3_256":
                time.sleep(1)
                sha3_256()
                time.sleep(1)
            elif soru == "bs64":
                time.sleep(1)
                Bs64Encode()
                time.sleep(1)
                
        elif secim == "2":
            time.sleep(1)
            henov = input("bs64 veya hexdec: ")
            time.sleep(1)
            if henov == "bs64":
                time.sleep(1)
                Bs64Decode()
                time.sleep(1)
            elif henov == "hexdec":
                time.sleep(1)
                hexdec() 
                time.sleep(1)                  
        elif secim == "3":
            print("Koddan çıkılıyor...")
            time.sleep(1)
            break            
    except Exception as e:
        print(f"Hata: {e}")
            
