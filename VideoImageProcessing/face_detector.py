import sys
import numpy as numpy
import cv2
import os

start_time = time.time()


def extract_face(img_name, dir_name, scalef = 1.3, minN = 3, minsize = (30, 30)):
	img_raw = cv2.imread(filename)
	test_image = cv2.cvtColor(img_raw, cv2.COLOR_BGR2RGB)
	test_image_gray = cv2.cvtColor(img_raw, cv2.COLOR_BGR2GRAY)
	haar_cascade_face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
	faces_rects = haar_cascade_face.detectMultiScale(test_image_gray, scaleFactor = scalef, minNeighbors=minN, minSize=minsize)

	n = len(faces_rects)
	for (x, y, w, h) in faces_rects:
		cv2.rectangle(img_raw, (x,y), (x+w, y+h), (0,255,0),5)

	head, tail = os.path.split(img_name)
	
	new_img_name = head + "/" + dir_name + "/" + tail.split(".")[0] + "_fd_" + str(n) + ".jpeg"

	status = cv2.imwrite('new_img_name', img_raw)


if __name__ == "__main__":
	directory = sys.argv[1]
	for img in os.listdir(directory):
		img_name  = img
		path_img=os.path.join(directory, img)
		extract_face(path_img, 'test1')

print("--- %s seconds ---" % (time.time() - start_time))

