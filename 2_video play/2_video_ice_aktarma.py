# =============================================================================
#                            -Doğukan Karataş-                                # 
# =============================================================================

import cv2
import time                               # zaman kütüphanesi

# video ismi
video_name = "MOT17-04-DPM.mp4"           # video dosyasının üstüne gelip f2 ye basıp ordan seçebilirsin

# video içe aktar: capture, cap
cap = cv2.VideoCapture(video_name)

print("Genişlik: ",cap.get(3))            # 3. index ile genişlik öğreniriz
print("Yükseklik: ",cap.get(4))           # 4. index ile yükseklik öğreniriz

if cap.isOpened() == False:               # açılıp acılmadıgını kontrol ediyoruz.
    print("Hata")
    
while True:    
    ret, frame = cap.read()               # ret = return video başarılı ise true döner başarısız ize false döner.
                                          # frame = videodaki her kare
    if ret == True:
        
        time.sleep(0.01)                  # Uyarı!!! : kullanmazsak çok hızlı akar (resim kareleri)
        
        cv2.imshow("Video",frame)
    else: 
        break

    if cv2.waitKey(1) & 0xFF == ord("q"): # kendi isteğimizle çıkmak için.
        
        break
    
cap.release()                             # stop capture.
cv2.destroyAllWindows()                   # tüm pencereleri kapatıyoruz.
    
    
    
