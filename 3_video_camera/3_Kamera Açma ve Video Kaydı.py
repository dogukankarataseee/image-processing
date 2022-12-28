# =============================================================================
#                            -Doğukan Karataş-                                # 
# =============================================================================

import cv2

# capture
cap = cv2.VideoCapture(0)                           # Laptop kamerası kullanıyorsak (0) Harici kamera (1) kullanıyoruz
                              
    
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))      # resim genişliğini al
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))    # resim yüksekliğini al
print(width, height)                                # ekrana boyutları çıktı veriyoruz

# video kaydet                                                        # video akış hızı
writer = cv2.VideoWriter("video_kaydi.mp4", cv2.VideoWriter_fourcc(*"DIVX"),20,(width, height))
                                                    # fourcc videoları sıkıştırma için kullanırız kodek kodu
while True:
      
    ret, frame = cap.read() 
    cv2.imshow("Video",frame)
    
    # save
    writer.write(frame)
    
    if cv2.waitKey(1) & 0xFF == ord("q"): break

cap.release()                                       # kamerayı durduruyoruz
writer.release()                                    # yazmayı durduruyoruz
cv2.destroyAllWindows()                             # pencereleri kapatıyoruz

