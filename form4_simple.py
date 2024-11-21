import cv2          

# Membaca citra input
img1 = cv2.imread('picture1.jpeg') 
img2 = cv2.imread('picture2.jpeg')

# Operasi Bitwise AND
dest_and = cv2.bitwise_and(img1, img2, mask=None)
cv2.imshow('Bitwise AND', dest_and)
cv2.waitKey(0)

# Operasi Bitwise OR
dest_or = cv2.bitwise_or(img1, img2, mask=None)
cv2.imshow('Bitwise OR', dest_or)
cv2.waitKey(0)

# Operasi Bitwise XOR
dest_xor = cv2.bitwise_xor(img1, img2, mask=None)
cv2.imshow('Bitwise XOR', dest_xor)
cv2.waitKey(0)

# Tutup semua jendela
cv2.destroyAllWindows()