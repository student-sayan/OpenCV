import cv2

location = input("write image location = ")
image = cv2.imread(location)


pic = int(input("Take the chose (1. image show /2. image save /3. image convart to black and white) = "))

match pic:
    case 1:
        cv2.imshow("image",image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    case 2:
        save_name = input("Enter your fill name = ")
        cv2.imwrite(f"{save_name}",image)
        print(f"Fill name {save_name} save successfully")

    case 3:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Gray_Image",gray)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        gray_image = input("Enter your fill name = ")
        cv2.imwrite(f"{gray_image}",gray)
        print(f"Gray image save successfully")

        
    case _:
        print("Invalid location")
