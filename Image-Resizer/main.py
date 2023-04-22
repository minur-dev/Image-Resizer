import cv2
print("program is executing...")
source = "flag.jpeg"
destination = 'newimage.jpeg'

image = cv2.imread(source,cv2.IMREAD_UNCHANGED)
#cv2.imshow("Title",image)
#cv2.waitKey(0)


scale_percent = 50

new_width = int(image.shape[1] * scale_percent / 100)
new_height = int(image.shape[0]*scale_percent/100)

output = cv2.resize(image,(new_width,new_height))

cv2.imwrite(destination, output)
cv2.waitKey(0)
print("program ended")
