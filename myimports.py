# imports
from __future__ import print_function
from __future__ import division


import numpy as np
import pandas as pd

import os
import re

#from gi.repository import GObject
#import matplotlib
#matplotlib.use('Agg')
from matplotlib import pyplot as plt
import cv2
import seaborn as sns
import scipy.stats as stats
from constants import * 


import tensorflow as tf
import tflearn
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.estimator import regression
from tflearn.layers.normalization import local_response_normalization

import random
from timeit import default_timer as timer

import tsahelper_whole as tsa
from tsahelper_whole import read_data

import shutil

