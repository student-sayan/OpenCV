import cv2

image = cv2.imread("image1.jpg")

if image is None:
    print("Error image not found")
else:
    print("Image loaded successfully")