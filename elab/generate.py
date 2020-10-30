
#!/usr/bin/env python
# coding=utf-8
# ****************************************************
#
#      Filename: generate.py
#
#        Author: ly - liyang.ok@outlook.com
#        Create: 2020-10-29 09:39:52
# Last Modified: 2020-10-29 15:57:35
#   Description: ---
#
# ***************************************************

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import sys

import glob



def generate_train_and_val(imagePath,txt_file):
    with open(txt_file,'w') as tf:
        for jpg_file in glob.glob(imagePath+"*.jpeg"):
            print(jpg_file)
            tf.write(jpg_file+"\n")



#imagePath=input("please input image dir path: ")

#print("image path : ",imagePath)

#txtOutPath=input("please input txt out path: ")

#print("txt output path : "+txtOutPath)


imagePath='/home/leo/liyang/train_data/elab/image/train/'

txtOutPath='/home/leo/liyang/train_data/elab/image/train.txt'

generate_train_and_val(imagePath,txtOutPath)



val_imagePath='/home/leo/liyang/train_data/elab/image/val/'

val_txtOutPath='/home/leo/liyang/train_data/elab/image/val.txt'

generate_train_and_val(val_imagePath,val_txtOutPath)

