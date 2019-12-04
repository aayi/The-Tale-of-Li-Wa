# -*- coding: utf-8 -*-
import os, sys

file1path = '4unigrams_sentiment.txt'
file2path = '5unigrams_cosine_similarity.txt'

file_1 = open(file1path,'r',encoding='utf-8')
file_2 = open(file2path,'r',encoding='utf-8')

list1 = []
for line in file_1.readlines():
    ss = line.strip()
    list1.append(ss)
file_1.close()

list2 = []
for line in file_2.readlines():
    ss = line.strip()
    list2.append(ss)
file_2.close()

file_new = open('7word2vec_cosine_similarity.csv','w',encoding='utf-8')
for i in range(len(list1)):
    sline = list1[i] + ',' + list2[i]
    file_new.write(sline+'\n')
file_new.close()
print ('success')




按列合并
#add many .txt info into a .txt
#get many .txt to a listfile, and read this listfile to add all .txt into a .txt
import os
import sys
import shutil

rectroipath = '/ssd/wangmaorui/data/RectRoi'

if __name__=="__main__":

    rectroioldpath = os.path.join(rectroipath,'rectroi.txt')
    rectroinewpath = os.path.join(rectroipath,'rectroiall.txt')
    lblFile = open(rectroioldpath,'r')
    frect = open(rectroinewpath,'w')

    lblSrcFLines = lblFile.readlines()
    for line in lblSrcFLines:
        srcLine = line.strip().split()  # space split
        sline = srcLine[0].strip()
        froi = open(sline,'r')
        roilines = froi.readlines()
        for rline in roilines:
            frect.write(rline)
        froi.close()

    frect.close()
lblFile.close()