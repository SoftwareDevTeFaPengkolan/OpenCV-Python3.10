#import cv2, numpy and matplotlib libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread("DCM1.jpg")
#Displaying image using plt.imshow() method
plt.imshow(img)

#hold the window
plt.waitforbuttonpress()
plt.close('all')

