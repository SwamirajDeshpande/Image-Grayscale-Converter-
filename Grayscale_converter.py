import cv2

# Taking path input from user
path = input("Enter the location of the image:")
img = cv2.imread(path)

if img is None:
    print("Error: Image is not loaded.")
else:
    print("Image loaded successfully.")

# Comverting image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
resize = cv2.resize(gray, (500, 650))

# Asking user to save or to display image
choice = int(input("Do you want to display the image or save the image\n1.display\n2.save\nEnter 1 or 2:"))

# displaying the image to user
if choice == 1:
    cv2.imshow("Grayscale image", resize)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
# saving the image by taking filename from user
elif choice == 2:
    name = input("Enter the filename with which you want to save image:")
    cv2.imwrite(name, resize)