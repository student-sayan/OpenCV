import cv2

image = cv2.imread("Image Resizing & Shaping\\image1.jpg")

if image is not None:
    cropped = image[100:900, 50:500]

    cv2.imshow("Originam image",image)
    cv2.imshow("cropped image",cropped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()