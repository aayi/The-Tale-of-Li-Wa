# -*- coding: utf-8 -*-
import logging
import os.path
import sys
import multiprocessing
from gensim.models import Word2Vec
from gensim.models import word2vec
from gensim.models.word2vec import LineSentence

def main():
    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s',level=logging.INFO)
    #sentences = word2vec.LineSentence('changan_seg_stopwords_out.txt')
    #sentences = word2vec.LineSentence('changan_seg_stopwords_out_1_blank.txt')
    sentences = word2vec.LineSentence('0test_unigram_nonpunc.txt')
    #model = Word2Vec(sentences,sg=0,size=50, window=8, min_count=2,iter=20, workers=multiprocessing.cpu_count()) cbow 模型9，相对准确
    #model = Word2Vec(sentences,sg=1,size=50, window=8, min_count=4,iter=20, workers=multiprocessing.cpu_count()) skip-gram相对准确
    model = Word2Vec(sentences,sg=0,size=50, window=5, min_count=1,iter=20, workers=multiprocessing.cpu_count())
    model.save('2word2vec.model')
if __name__ == '__main__':
    main()
print ('success')