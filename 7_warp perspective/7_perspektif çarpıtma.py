# =============================================================================
#                           -Doğukan Karataş-                                 # 
# =============================================================================

import cv2
import numpy as np

# içe aktar resim
img = cv2.imread("kart.png")
cv2.imshow("Orijinal", img)

width = 400                                                       # resmimizin yüksekliği ve genişliğini belirliyoruz
height = 500    
                                                                  # paint açılarak oradan öğrenilebilir
pts1 = np.float32([[230,1],[1,472],[540,150],[338,617]])          # resmin 4 köşesinin piksel değerleri belirlenir
pts2 = np.float32([[0,0],[0, height],[width,0],[width,height]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)                  # perspektif dönüşüm matrisini elde ediyoruz 
print(matrix)

# nihai dönüştürülmüş resim
imgOutput = cv2.warpPerspective(img, matrix, (width,height))      # çevirmeyi gerçekleştiriyoruz
cv2.imshow("Nihai Resim", imgOutput)