# Pictures from pixelbay

import imageio # 
import os 
import glob
import pandas
import numpy

import matplotlib.pyplot as pyplot

def getrb(filepath):
	imageio.imread(filepath, pilmode="RGB")
	image = imimage/255
	imimage.sum(axis=0).sum(axis=0).sum(axis=0)/

# Interpretation:
# Bigger numbers : mix of the three

filepath = "data/pic01.jpeg"

print(getrb(filepath))

