import cv2

image = cv2.imread("Image Drowing Function\\white.jpg")

if image is None:
    print("Image is not found")
else:
    print("Image loaded successfully")
    pt1 = (100,150)
    pt2 = (300,150)
    color = (255,0,0)
    thickness = 4

    cv2.line(image, pt1, pt2, color, thickness)

    cv2.imshow("line drowing",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()