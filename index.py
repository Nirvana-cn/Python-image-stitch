from __future__ import print_function

import datetime
import cv2 as cv
import sys

output = './result.jpg'

files = ["./images/left.jpg", "./images/right.jpg"]

startTime = datetime.datetime.now()
print(startTime)

images = []
for img_name in files:
    img = cv.imread(img_name)
    if img is None:
        print("Can't read image " + img_name)
        sys.exit(-1)

    images.append(img)

# openCV 3
# stitcher = cv.createStitcher(cv.Stitcher_PANORAMA)
# openCV 4
stitcher = cv.Stitcher_create(cv.Stitcher_PANORAMA)

status, pano = stitcher.stitch(images)
if status != cv.Stitcher_OK:
    print("Can't stitch images, error code = %d" % status)
    sys.exit(-1)

cv.imwrite(output, pano)
print("Stitching completed successfully.")

endTime = datetime.datetime.now()
print(endTime)
