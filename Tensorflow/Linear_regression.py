# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 11:32:23 2023

@author: maidu
"""
    
import tensorflow as tf
import numpy as np 
import sys
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import os
    
if __name__=='__main__':
    file_name = 'test.csv'
    df = pd.read_csv(file_name)
    df.head()
    x = tf.compat.v1.train.GradientDescentOptimizer