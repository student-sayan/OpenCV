import cv2

image = cv2.imread("Image Drowing Function\\white.jpg")

if image is None:
    print("Image is not found")
else:
    print("Image loaded successfully")
    pt1 = (200,150)
    

    color = (255,0,0)
    thickness = -1

    cv2.circle(image, pt1, 100, color, thickness)
    
    cv2.imshow("circle drowing",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()