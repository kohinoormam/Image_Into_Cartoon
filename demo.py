import cv2
import numpy as np

def show_image(img, title="Sketch Outline"):
    cv2.imshow(title, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

path = "data/diya.jpg"
img = cv2.imread(path)

if img is None:
    print("Image not found. Check path.")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Reduce noise while keeping edges sharp
gray = cv2.GaussianBlur(gray, (5, 5), 0)

# Detect sharp edges
edges = cv2.Canny(gray, 80, 150)

# Make lines thicker
kernel = np.ones((2,2), np.uint8)
edges = cv2.dilate(edges, kernel, iterations=1)

# Create white background
sketch = np.ones_like(gray) * 255

# Draw black edges
sketch[edges != 0] = 0

show_image(sketch)
quit()