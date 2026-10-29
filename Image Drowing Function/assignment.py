import cv2

m_fill = input("Enter your image location = ")
image = cv2.imread(m_fill)

pic = int(input("=====Take the chose=====\n|_>1.line Drowing\n|_>2.Rectangle Drowing\n|_>3.Circle Drowing\n|_>4.Text add\n->chose one option = "))

match pic:
    case 1:
        if image is None:
            print("oops!!!!! image not found")

        else:
            a1 = int(input("X1 axis = "))
            b1 = int(input("Y1 axis = "))
            a2 = int(input("X2 axis = "))
            b2 = int(input("Y2 axis = "))

            cv2.line(image, (a1,b1), (a2,b2), (255,0,0), 4)
            
            cos = input("Do you want to save(y/n) = ")

            if cos == "y":
                fill_name = input("Enter fill name with extention = ")
                cv2.imwrite(fill_name,image)

            elif cos == "n":
                print("Fill not save")

        cv2.imshow("Line Image",image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    case 2:
        if image is None:
           print("oops!!!!! image not found") 
        else:
            a1 = int(input("X1 axis = "))
            b1 = int(input("Y1 axis = "))
            a2 = int(input("X2 axis = "))
            b2 = int(input("Y2 axis = "))

            cv2.rectangle(image, (a1,b1), (a2,b2), (0,255,0), 2)

            cos = input("Do you want to save(y/n) = ")
            
            if cos == "y":
                fill_name = input("Enter fill name with extention = ")
                cv2.imwrite(fill_name,image)

            elif cos == "n":
                print("Fill not save")

            cv2.imshow("Rectangle Image",image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

    case 3:
        if image is None:
            print("oops!!!!! image not found") 

        else:
            a1 = int(input("X1 axis = "))
            b1 = int(input("Y1 axis = "))

            radius = int(input("Enter radius(r) = "))

            thikness = int(input("Enter Thikness(-1/0/1) = "))
        
            cv2.circle(image, (a1,b1), radius, (255,0,0), thikness)
            cv2.imshow("Circle Image",image)
            cos = input("Do you want to save(y/n) = ")
            
            if cos == "y":
                fill_name = input("Enter fill name with extention = ")
                cv2.imwrite(fill_name,image)

            elif cos == "n":
                print("Fill not save")

            cv2.waitKey(0)
            cv2.destroyAllWindows()
    case 4:
       if image is None:
             print("oops!!!!! image not found") 
       else:
            a1 = int(input("X1 axis = "))
            b1 = int(input("Y1 axis = "))

            text = input("Input Text = ")
            text_bolt = float(input("inpute float value above 1.0 = "))
        
            cv2.putText(image, text, (a1,b1), cv2.FONT_HERSHEY_SIMPLEX, text_bolt, (255,0,0), 1)

            cv2.imshow("Text Add",image)
            cos = input("Do you want to save(y/n) = ")
            
            if cos == "y":
                fill_name = input("Enter fill name with extention = ")
                cv2.imwrite(fill_name,image)

            elif cos == "n":
                print("Fill not save")

            cv2.waitKey(0)
            cv2.destroyAllWindows() 
    case _:
        print("Invalide Location")