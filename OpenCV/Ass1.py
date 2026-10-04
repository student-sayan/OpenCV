import cv2

location = input("write image location = ")
image = cv2.imread(location)


pic = int(input("Take the chose (1. image show /2. image save) = "))

match pic:
    case 1:
        cv2.imshow("image",image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    case 2:
        save_name = input("Plece enter save name = ")
        cv2.imwrite(f"{save_name}",image)
        print("Fill name save successfully")

    case _:
        print("Invalid location")