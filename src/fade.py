import cv2, time
import numpy as np

def fade(img1, img2):

	img1 = cv2.imread(img1)
	img2 = cv2.imread(img2)

	alturaB, larguraB, _ = img2.shape
	img1 = cv2.resize(img1, (larguraB, alturaB))

	for c in range(1, 41):

		fade = cv2.addWeighted(img1, 0.025*c, img2, 0.025*(40-c), 0)
		cv2.imshow("Fade", fade)
		if c == 2:
			time.sleep(0.3)
		if c == 40:
			cv2.waitKey(0)
			cv2.imwrite("output/fade{}.png".format(c), fade)
		else:
			cv2.waitKey(1)
			time.sleep(0.04)
			cv2.imwrite("output/fade{}.png".format(c), fade)

fade("input/imagem1.jpg", "input/imagem2.jpg")
