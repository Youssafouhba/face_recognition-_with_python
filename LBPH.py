from skimage import feature
import matplotlib.pyplot as plt
import numpy as np
import cv2
import glob

numPoints=8
radius=3

textures=['AI']
file_name_path ='./'+ '.jpg'
for texture in textures:
	print(">>>", f"{texture}.jpg")
	image=cv2.imread(f"{texture}.jpg", 0)
	if image is None:
		quit("Probleme image...")
	lbp=feature.local_binary_pattern(image, numPoints, radius, method='default')
	hist_ref, _=np.histogram(lbp, bins=2**numPoints, range=(0, 2**numPoints))

	cv2.imshow("Image", image)
	cv2.imshow("LBP", lbp)
	cv2.imwrite(file_name_path,image)
	cv2.imwrite(file_name_path, lbp)

	plt.plot(hist_ref)
	plt.show()

	key=cv2.waitKey(1)&0xFF
	if key==ord('q'):
		quit()