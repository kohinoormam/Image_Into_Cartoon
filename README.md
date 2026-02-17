Image to Cartoon

Transform any image into a cartoon-style sketch with black outlines on a white background using Python and OpenCV.

Features
* Sharp edge detection with Canny
* Smooth edges using Gaussian Blur
* Adjustable line thickness with dilation
* Clean white background with black outlines

Requirements

```bash
pip install opencv-python numpy
```
Usage

1. Place your image in the `data/` folder (e.g., `data/diya.jpg`)
2. Run the script:

```bash
python code.py
```
The cartoon sketch will display in a window. Press any key to close.

Optional
Save the output automatically:

```python
cv2.imwrite("data/diya_cartoon.jpg", cartoon)
```
