import cv2

image = cv2.imread("image1.jpg")

if image is not None:
    cv2.imshow("Anime image",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image Error")