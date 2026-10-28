import cv2

image = cv2.imread("Image Drowing Function\\white.jpg")

if image is None:
    print("Image is not found")
else:
    print("Image loaded successfully")
    pt1 = (100,90)
    pt2 = (300,90)

    pt3 = (100,90)
    pt4 = (100,200)

    pt5 = (300,90)
    pt6 = (300,200)

    pt7 = (100,200)
    pt8 = (300,200)

    color1 = (255,0,0)
    color2 = (0,255,0)
    color3 = (0,0,255)
    thickness = 4

    cv2.line(image, pt1, pt2, color1, thickness)
    cv2.line(image, pt3, pt4, color2, thickness)
    cv2.line(image, pt5, pt6, color3, thickness)
    cv2.line(image, pt7, pt8, color1, thickness)

    cv2.imshow("line drowing",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()