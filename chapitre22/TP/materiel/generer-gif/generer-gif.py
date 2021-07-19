#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 22:57:58 2020

@author: junier
"""

import glob
import moviepy.editor as mpy

gif_name = 'KNN-Influence-de-k-nettoyage-1609407183'
fps = 0.2
file_list = glob.glob('nettoyage-1609407183*.png') # Get all the pngs in the current directory
list.sort(file_list, key=lambda x: int(x.split('=')[1].split('.png')[0])) # Sort the images by #, this may need to be tweaked for your use case
clip = mpy.ImageSequenceClip(file_list, fps=fps)
clip.write_gif('{}.gif'.format(gif_name), fps=fps)
