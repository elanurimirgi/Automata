import time

# Fonksiyon amacı iki şifreyi karşılaştırmak
def turing_simulator(user_pin, system_pin):
    # Alfabe: {'0'-'9', '#', 'X', 'Y', 'B'}
    tape = list('#' + user_pin + '#' + system_pin + '#')  # Bant oluşturuldu
    head = 1  # Başlangıç pozisyonu (#'dan sonraki ilk karakter) 0. pozisyonda # karakteri var o yüzden 1' den başlaatıldı

    print("\n--- Turing Makinesi Simülasyonu Başladı ---\n")
    print("Başlangıç Bandı: ", ''.join(tape))
    
    # Turing Makinesi döngüsü
    while True:
        time.sleep(0.5)  # Görsellik için yavaşltama
        
        if tape[head] in '0123456789':  # Kullanıcı PIN'i kısmında sayıya geldik
            current_digit = tape[head]
            # Karşılık gelen sistem PIN karakterini bulur
            # Sistem PIN başlangıcı: '#' + user_pin + '#' ==> len(user_pin) + 2
            system_head = len(user_pin) + 2 + (head - 1)
            if system_head >= len(tape) or tape[system_head] == '#':  # Eğer system_head pozisyonu bandın dışına çıkarsa veya # karakterine denk gelirse, hatalı durum olur.
                print("Karşılaştırma sırasında bant bitti, RED")
                return False
            if tape[system_head] == current_digit: # Karakterler aynı ise Kullanıcının PIN’indeki karakter 'X' ile işaretlenir (işaret konulmuş demek). Sistem PIN’indeki karakter 'Y' ile işaretlenir. head bir sonraki basamağa geçer.
                tape[head] = 'X'  # Eşleşen kullanıcı PIN basamağını işaretle
                tape[system_head] = 'Y'  # Eşleşen sistem PIN basamağını işaretle
                head += 1
            else:
                print("PIN basamakları eşleşmiyor, RED")
                print("Bant Durumu: ", ''.join(tape))
                return False
        elif tape[head] == '#':  # PIN bitimi   # Kullanıcı PIN’indeki tüm basamaklar kontrol edilmiş ve hepsi eşleşmişse, ACCEPT (kabul) edilir ve True döndürülür.
            print("Tüm basamaklar kontrol edildi, ACCEPT")
            print("Bant Durumu: ", ''.join(tape))
            return True
        else:
            # Daha önce işaretlenmiş karakter
            head += 1

        print("Bant Durumu: ", ''.join(tape))
    
# Ana program:
if __name__ == "__main__":
    system_pin = "1234"  # Sabit sistem PIN'i
    
    print("PIN doğrulama sistemine hoş geldiniz.")
    user_pin = input("Lütfen 4 haneli PIN'inizi girin: ")

    # Basit validasyon yapıldı
    if not user_pin.isdigit() or len(user_pin) != 4:
        print("Geçersiz PIN. Lütfen sadece 4 haneli sayı girin.")
    else:
        result = turing_simulator(user_pin, system_pin)
        print("\nSonuç:")
        if result:
            print("Şifre doğru")
        else:
            print("Şifre hatalı")
