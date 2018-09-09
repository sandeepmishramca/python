#import cv2
import os
import glob
from PIL import Image
import numpy as np
import csv
import pandas as pd
from matplotlib import pyplot as plt

#to write image to csv as a image string
img_dir = "D:\\training\\cat\\catimage" # Enter Directory of all images 
data_path = os.path.join(img_dir,'*g')
files = glob.glob(data_path)
print(files)
data = []
img_shape=[]
for f1 in files:
	img=Image.open(f1)
	print(f1)
	img=np.array(img)
	print(img.shape)
	to_string=' '.join([str(x) for x in img.flatten()])
	data.append(to_string)
print(len(data))
with open('test1.csv','w') as f:
	f.write("Eye,Image")
	for row in data:
		f.write('\n')
		f.write('45.0,'+row)
#to show image
'''file_path="D:\\training\\cat\\catimage\\car1.jpg"
img=Image.open(file_path)
img=np.array(img)
imgshape=img.shape
print(imgshape)
to_string=' '.join([str(x) for x in img.flatten()])
print(to_string)
x=np.fromstring(to_string, sep=' ')
X = np.vstack(x) / 255.
print(X.shape)
X = X.astype(np.float32)
plt.imshow(X.reshape(imgshape))
plt.show()
'''
