import cv2

image = cv2.imread("Image Resizing & Shaping\\image1.jpg")

if image is None:
    print("Could not load image")
else:
    flipped_horizontal = cv2.flip(image, 1)
    flipped_vartical = cv2.flip(image, 0)
    flipped_both = cv2.flip(image, -1)

    cv2.imshow("Original", image)
    cv2.imshow("horizontal",  flipped_horizontal)
    cv2.imshow("vartical", flipped_vartical)
    cv2.imshow("horizontal & vartical", flipped_both)
    cv2.waitKey(0)
    cv2.destroyAllWindows()