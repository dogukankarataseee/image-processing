# =============================================================================
#                            -Doğukan Karataş-                                # 
# =============================================================================

import cv2

img = cv2.imread("lenna.png")                      # resmi açıyoruz
print("Resim boyutu: ", img.shape)                 # resmimizin orijinal boyutunu oğreniyoruz.
cv2.imshow("Orijinal", img)

# resized
imgResized = cv2.resize(img, (800,800))            # resmimizi yeniden boyutlandırıyoruz.
print("yeni boyutlu resim: ", imgResized.shape)    # resmimizin yeni boyutunu öğreniyoruz.
cv2.imshow("Img Resized",imgResized)

# kırp
imgCropped = img[:500,300:600]                     # width height -> height width 
cv2.imshow("Kirpik Resim",imgCropped)


