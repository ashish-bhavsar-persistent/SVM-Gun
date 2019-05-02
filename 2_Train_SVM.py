#!/usr/bin/env python2  
# -*- coding: utf-8 -*-  
""" 
Created on Thu Jun 15 16:38:03 2017 
 
@author: hans 
"""  
import sklearn.svm as ssv  
from sklearn.externals import joblib  
import glob  
import os  
import time  
  
if __name__ == "__main__":
    # 1. Use Initially
    model_path = './models/svm.model'
    # 2. Use NextTime
    # model_path = './models/svm_pso.model'
    train_feat_path = './features/train'  
    fds = []  
    labels = []  
    num=0  
    for feat_path in glob.glob(os.path.join(train_feat_path, '*.feat')):  
        num += 1  
        data = joblib.load(feat_path)  
        fds.append(data[:-1])  
        labels.append(data[-1])  
        print ("%d Dealing with %s" %(num,feat_path))
    t0 = time.time()  
#------------------------SVM--------------------------------------------------
    # 1. Use Initially
    clf = ssv.SVC(kernel='rbf')
    #2. Use NextTime
    # clf = ssv.SVC(C=, kernel=='rbf', gamma=)
    print ("Training a SVM Classifier.")
    clf.fit(fds, labels)  
    joblib.dump(clf, model_path)
#------------------------SVM--------------------------------------------------  
    t1 = time.time()  
    print ("Classifier saved to {}".format(model_path))
    print ('The cast of time is :%f seconds' % (t1-t0))
