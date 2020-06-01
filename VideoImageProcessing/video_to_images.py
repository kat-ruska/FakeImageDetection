#!/usr/bin/python

import cv2
import os
import sys
import time

start_time = time.time()

def getFrame(vidcap, sec, vidname):
	path = '/Users/ruska/Documents/UCU/ML/course_project/Face2Face_image/'
	vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
	hasFrames,image = vidcap.read()
	if hasFrames:
		cv2.imwrite(os.path.join(path, vidname+"_"+str(count)+".jpg"), image)     # save frame as JPG file
	return hasFrames



if __name__ == "__main__":
	directory = sys.argv[1]
	for video in os.listdir(directory):
		vidname  = video
		path_vid=os.path.join(directory, video)
		vidcap = cv2.VideoCapture(path_vid)
		sec = 0
		frameRate = 2
		count = 1
		success = getFrame(vidcap, sec, vidname)
		while success:
			count = count + 1
			sec = sec + frameRate
			sec = round(sec, 2)
			success = getFrame(vidcap, sec, vidname)

print("--- %s seconds ---" % (time.time() - start_time))
