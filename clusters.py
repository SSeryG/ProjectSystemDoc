from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import AgglomerativeClustering 
from sklearn import metrics
from scipy.cluster.hierarchy import dendrogram,linkage
import pandas as pd
from nltk import ngrams
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class ClustersClass(object):
    def __init__(self):
        self.model=AgglomerativeClustering(distance_threshold=1.5,n_clusters=None)        
        self.data=pd.DataFrame()
      
    def OneCluster(self,X):            
        self.data=pd.concat([self.data, X])
        labels=self.model.fit_predict(self.data)    
        print(labels)
        return labels
    
def TFidfVector(artext):#построение и вычисление частотности
        tfIdfVectorizer = TfidfVectorizer(ngram_range=(2,3),use_idf = True)
        tfIdf = tfIdfVectorizer.fit_transform(artext)
        tokens=(tfIdfVectorizer.get_feature_names_out())
        df_tfidf = pd.DataFrame(tfIdf.toarray(), columns = tokens)
        print(df_tfidf)        
        return df_tfidf

