# =============================================================================
#                            -Doğukan Karataş-                                # 
# =============================================================================


import cv2                              # computer vision library [-Opencv-]

# içe aktarma
img = cv2.imread("messi5.jpg", 0)       # resim kod dosyası ile aynı klasorde olmalıdır.
                                        # 0 parametresi resmi siyah beyaz açmaya yarar.
                                        # cv2.imread("dosya adı", ((0 or 1) siyah ve renkli) )

# görselleştirme
cv2.imshow("Result", img)               # pencere isimlendirirken türkçe karakter kullanılmaz.

k = cv2.waitKey(0) &0xFF                # klavyeden komut almayı bekliyor

if k == 27:                             # esc tuşunun karşılığı  kapatmak için
    
    cv2.destroyAllWindows()             # tüm pencereleri kapat

elif k == ord('s'):                     # klavyeden s tuşuna basılırsa kayıt yapar
    
    cv2.imwrite("messi_gray.png", img)  # dosya uzerine siyah beyaz kaydetmeye yarar 
    
    cv2.destroyAllWindows()             # tüm pencereleri kapat
    