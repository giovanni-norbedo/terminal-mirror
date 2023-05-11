import os
import sys
import time
import numpy as np
import cv2
from PIL import Image

nameNum = 0
rval = True
high = 200
capture = cv2.VideoCapture(0)

try:
    while rval:
        rval, frame = capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imwrite(f"img/frame{str(nameNum)}.png", gray)
        
        imgStr = np.asarray(
            Image.open(f"img/frame{str(nameNum)}.png")
            .resize(os.get_terminal_size(), resample=Image.BILINEAR)
        )

        imgStr = np.where(
            imgStr > high, "█",
            np.where(imgStr > 3/4 * high, "▓",
            np.where(imgStr > 2/4 * high, "▒",
            np.where(imgStr > 1/4 * high, "░",
            " "
        ))))

        imgStr = ''.join(map(str, imgStr.flatten()))

        time.sleep(0.05)
        os.system("clear")
        print(imgStr)

        nameNum += 1
        os.system("cd ./img && rm -rf frame*.png")


except KeyboardInterrupt:
    os.system("clear")
    os.system("cd ./img && rm -rf frame*.png")
    exit(0)
