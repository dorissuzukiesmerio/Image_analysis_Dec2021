# Pictures from pixelbay

import imageio # 
import os 
import glob
import pandas
import numpy

import matplotlib.pyplot as pyplot

def getrb(filepath):
	imageio.imread(filepath, pilmode="RGB")