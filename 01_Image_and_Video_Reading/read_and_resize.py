import cv2 
img = cv2.imread("cat.jpg") # This Method takes path of image and returns that image as matrix of pixels

print(img)


cv2.imshow("Cat", img) # This method display the image in new window, and needs 2 Parameters is Name of Window e.g 'Cat' and Actual matrix of pixels to display e.g 'img'.

cv2.waitKey(0) # Infinite Time until a key is pressed.