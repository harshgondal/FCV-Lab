import cv2
img=cv2.imread("Picture1.jpeg")
cv2.imwrite('Picture2.jpeg',img)
cv2.imshow("My First CV Program",img)
cv2.waitKey(0)
