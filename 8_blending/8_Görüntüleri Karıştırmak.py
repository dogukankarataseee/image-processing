# =============================================================================
#                           -Doğukan Karataş-                                 # 
# =============================================================================

import cv2 
import matplotlib.pyplot as plt  # matplotlib kütüphanesini kullanacağız

# karıştırma

img1 = cv2.imread("img1.JPG") # resimleri yüklüyoruz
img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB) # Resmi BGR dan RGB ye çeviriyoruz.   
img2 = cv2.imread("img1.JPG") # resimleri yüklüyoruz
img1 = cv2.cvtColor(img2,cv2.COLOR_BGR2RGB) # Resmi BGR dan RGB ye çeviriyoruz.

plt.figure()
plt.imshow(img1)    # resmi(1) çizdiriyoruz ekrana

plt.figure()
plt.imshow(img2)    # resmi(2) çizdiriyoruz ekrana

print(img1.shape)   # resimlerin boyutlarını öğreniyoruz.
print(img2.shape)

img1 =cv2.resize(img1, (600,600)) # resimleri yeniden boyutlandırıyoruz
print(img1.shape)

img1 =cv2.resize(img2, (600,600)) # resimleri yeniden boyutlandırıyoruz
print(img1.shape)

plt.figure()
plt.imshow(img1)    # resmi çizdiriyoruz ekrana

plt.figure()
plt.imshow(img2)    # resmi çizdiriyoruz ekrana

# karıştırılmış resim = alpha*img1+ beta*img2 

blended = cv2.addWeighted(src1 = img1, alpha = 0.5, src2 = img2, beta=0.5, gamma=0)
plt.figure()
plt.imshow(blended)
