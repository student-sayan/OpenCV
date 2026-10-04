import cv2

image = cv2.imread("image1.jpg")

if image is not None:
    success = cv2.imwrite("Shinchan.jpg",image)
    if success:
        print("Image saved successfully saved as Shinchan.jpg")
    else:
        print("Failed to save an image")
else:
    print("Error: could note load image")