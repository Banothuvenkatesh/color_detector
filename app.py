import cv2
import numpy as np
import webcolors

# Load an image (replace with your image or webcam later)
img = cv2.imread("shirt.jpg")



# Mouse click event
def pick_color(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:  # left click
        b, g, r = img[y, x]
        rgb = (r, g, b)
        color_name = closest_color(rgb)
        print(f"Clicked at ({x}, {y}) → Color: {color_name}")

        # Draw line to box
        cv2.line(img, (x, y), (x+60, y-60), (0,0,0), 2)
        cv2.rectangle(img, (x+60, y-60), (x+100, y-20), (b,g,r), -1)
        cv2.putText(img, color_name, (x+60, y-25),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1)
        cv2.imshow("Image", img)

# Setup window and callback
cv2.namedWindow("Image")
cv2.setMouseCallback("Image", pick_color)

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
