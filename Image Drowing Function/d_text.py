import cv2

image = cv2.imread("Image Drowing Function\\white.jpg")

if image is None:
    print("Oops...! image not found")
else:
    print("Image loaded successfully")
    cv2.putText(image, "Hello Python Programmers", (25,150), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255,255,0), 1)

    cv2.imshow("Text add", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()