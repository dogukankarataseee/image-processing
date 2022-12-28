# =============================================================================
#                           -Doğukan Karataş-                                 # 
# =============================================================================

import cv2
import matplotlib.pyplot as plt               # görselleştirme(grafik) kütüphanesi

# resmi içe aktar
img = cv2.imread("img1.jpg")                  # resmi içeri aktar 
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)   # resmi grileştir

plt.figure()
plt.imshow(img, cmap = "gray")                # resmi siyahlaştır
plt.axis("off")
plt.show()


# eşikleme                      alt sınır   üst sınır          60-255 arasını sildi inverse seçilirse tam tersi  
_, thresh_img = cv2.threshold(img, thresh = 60, maxval = 255, type = cv2.THRESH_BINARY)

plt.figure()
plt.imshow(thresh_img, cmap = "gray")
plt.axis("off")
plt.show()

# uyarlamalı eşik değeri           üst sınır       yöntem
thresh_img2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11,8)
plt.figure()
plt.imshow(thresh_img2, cmap = "gray")
plt.axis("off")
plt.show()

























