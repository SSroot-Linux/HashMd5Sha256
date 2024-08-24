#Öncelikle Gerekli Kütüphaneyi Ekleyelim Sonra Mesajı alalım ondan sonra şifreleyelim 2 tür olsun şifrelemek ve decode etmek başlayalım
import hashlib
import base64
import pyfiglet
import time
from Crypto.Cipher import AES
import os
from colorama import Fore, init
init(autoreset=True)


time.sleep(1)

yazi = pyfiglet.figlet_format("        ^HASHer^    ")

time.sleep(1)

print(Fore.LIGHTMAGENTA_EX + yazi)

time.sleep(1)

print(Fore.YELLOW, """

1-) Encode(sha1,sha256,md5,bs64, sha3_256, hexenc, aes256, obf,special(base64 + sha256))

2-) Decode(Base64,hexdec,decobf)

3-) Koddan çık
""")

def Bs64Encode():
    veri = input("Şifrelemek İstediğiniz Mesajı Yazınız: ")
    time.sleep(1)
    enc = base64.b64encode(veri.encode())
    time.sleep(1)
    print(Fore.BLUE, f"Şifrelenmiş Metin: {enc.decode()}")
    time.sleep(1)
    print("Bitti")
   
   

def obf():
    metin = input("Şifrelemek istediğin metni gir: ")
    sifre = 4
    sifrelenmis = ""
    for char in metin:
        sifrelenmis += chr(ord(char) + sifre)
    print("Obf ile şifrelenmiş metin:", sifrelenmis)
    return sifrelenmis

def decobf():
    metin = input("Decode etmek istediğin metni gir: ")
    sifre = 4
    kirilmis = ""
    for char in metin:
        kirilmis += chr(ord(char) - sifre)
    print("Decode edilmiş metin:", kirilmis)
    return kirilmis    
       
def Aes256():
    anahtar = os.urandom(32)
    iv = os.urandom(16)
    metin = input("Şifrelemek istediğiniz metni giriniz: ")
    veri = metin.encode('utf-8')
 
    sifreleyici = AES.new(anahtar, AES.MODE_CBC, iv)
    sifreli_veri = sifreleyici.encrypt(veri.ljust(32))
    
    print("Şifrelenmiş:", sifreli_veri)
    
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
    mesaj = input("Şifreli Mesajı gir: ")
    sifre = int(mesaj, 16)
    
    time.sleep(1)
    
    print(f"Orjinal Metin: {sifre}")

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
        
def Special():
    veri = input("Şifrelemek İstediğiniz Mesajı Yazınız: ")
    time.sleep(1)
    enc = base64.b64encode(veri.encode())
    sifre = hashlib.sha256(veri.encode()).hexdigest()        
    time.sleep(1)
    print(Fore.BLUE, "Şifrelenmiş Metin:",(enc.decode() + sifre))
    time.sleep(1)
    print("Bitti")
    
    
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
            soru = input("Şifre Türünü Seç (md5/sha256/sha1/bs64/sha3_256/hexenc/aes256/obf/special): ")
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
            elif soru == "aes256":
                time.sleep(1)
                Aes256()
                time.sleep(1)
            elif soru == "obf":
                time.sleep(1)
                obf()
                time.sleep(1)    
                
            elif soru == "special":
                time.sleep(1)
                Special()
                time.sleep(1)   
        elif secim == "2":
            time.sleep(1)
            henov = input("bs64,hexdec,decobf: ")
            time.sleep(1)
            if henov == "bs64":
                time.sleep(1)
                Bs64Decode()
                time.sleep(1)
            elif henov == "hexdec":
                time.sleep(1)
                hexdec() 
                time.sleep(1)
            elif henov == "decobf":
                time.sleep(1)
                decobf()
                time.sleep(1)                  
        elif secim == "3":
            print("Koddan çıkılıyor...")
            time.sleep(1)
            break            
    except Exception as e:
        print(f"Hata: {e}")
            
