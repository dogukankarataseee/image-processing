# =============================================================================
#                           -Doğukan Karataş-
# =============================================================================

import cv2
import numpy as np 

# resmi içe aktar 
img = cv2.imread("barbara.jpg")
cv2.imshow("Orijinal", img)

# yatay horizontal
hor = np.hstack((img,img))  # yatay olarak resmi birleştirmemize yarar
cv2.imshow("Yatay",hor)

# dikey vertical
ver = np.vstack((img,img))  # dikey olarak resmi birleştirmemize yarar
cv2.imshow("Dikey",ver)    