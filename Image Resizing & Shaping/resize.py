import cv2

image = cv2.imread("Image Resizing & Shaping\\image1.jpg")

if image is None:
    print("Image not found")
else:
    print("Image Loaded")
    resize = cv2.resize(image,(300, 300))
    cv2.imshow("Anime1",image)
    cv2.imshow("Anime2",resize)
    cv2.imwrite("Resize_Image.jpg",resize)
    cv2.waitKey(0)
    cv2.destroyAllWindows()