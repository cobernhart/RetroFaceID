import cv2
import math
import numpy as np
from PIL import Image

#calculates angle to make eyes horizontal
def get_pivot(x, y):
    x1, x2 = x
    y1, y2 = y
    diffX = abs(x2 - x1)
    diffY = abs(y2 - y1)
    angle = math.tan(diffY / diffX)
    if y1 > y2:
        angle *= -1
    return (x1, y1, angle * 180 / np.pi)


#rotates image with pivot angle
def rotate_image(originalImage,landmark):
    cx, cy, angle = get_pivot(landmark[0:2, 0], landmark[0:2, 1])
    aligned_image = Image.fromarray(
        cv2.cvtColor(
            cv2.warpAffine(
                cv2.cvtColor(np.array(originalImage), cv2.COLOR_RGB2BGR),
                cv2.getRotationMatrix2D((cx, cy), angle, 1),
                (originalImage.width, originalImage.height)
            ),
            cv2.COLOR_BGR2RGB
        )
    )
    return aligned_image