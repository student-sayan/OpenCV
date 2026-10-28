import cv2

image = cv2.imread("OpenCV\\image1.jpg")

h,w,c = image.shape
print(f"Height = {h}\nWidth = {w}\nChannels = {c}")