from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import AgglomerativeClustering 
from sklearn import metrics
from scipy.cluster.hierarchy import dendrogram,linkage
import pandas as pd
from nltk import ngrams
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import time

class ClustersClass(object):
    def __init__(self):
        self.model=AgglomerativeClustering(distance_threshold=1.4,n_clusters=None)        
        
        
    def IsDataCSV(self,data):
        tic = time.perf_counter()
        if os.path.isfile('data.csv'):
            datacsv=pd.read_csv('data.csv',sep='\t',index_col=0)
            toc = time.perf_counter()
            print(f"Вычисление заняло {toc - tic:0.4f} секунд")
            data=pd.concat([data, datacsv])
            data=data.fillna(0)   
        data.to_csv('data.csv',sep='\t')
        toc = time.perf_counter()
        print(f"Вычисление заняло {toc - tic:0.4f} секунд")
        return data
      
    def OneCluster(self,X):            
        data=self.IsDataCSV(X)        
           
        print(data)        
        data.drop_duplicates(keep='last')
        
        print(data)
        labels=self.model.fit_predict(data)    
        print(labels)
        return labels
    
def TFidfVector(artext,index):#построение и вычисление частотности
        tfIdfVectorizer = TfidfVectorizer(ngram_range=(2,3),use_idf = True)
        tfIdf = tfIdfVectorizer.fit_transform(artext)
        tokens=(tfIdfVectorizer.get_feature_names_out())
        df_tfidf = pd.DataFrame(tfIdf.toarray(),index, columns = tokens)           
        return df_tfidf

