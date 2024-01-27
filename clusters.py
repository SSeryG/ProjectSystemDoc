from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import AgglomerativeClustering 
from sklearn import metrics
from scipy.cluster.hierarchy import dendrogram,linkage
import pandas as pd
from nltk import ngrams
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
model=AgglomerativeClustering(distance_threshold=1.5,n_clusters=None)


def TFidfVector(artext):#построение и вычисление частотности
    tfIdfVectorizer = TfidfVectorizer(ngram_range=(2,3),use_idf = True)
    tfIdf = tfIdfVectorizer.fit_transform(artext)
    tokens=(tfIdfVectorizer.get_feature_names_out())
    df_tfidf = pd.DataFrame(tfIdf.toarray(), columns = tokens)
    print(df_tfidf)
    tokens=None
    tokens=[]
    return df_tfidf

def Cluster(X):    
    labels=model.fit_predict(X)
    return labels

def Cluster(X,x_predict):    
    labels=model.fit_predict(X)
    print(labels)

    labels = model.fit_predict(x_predict)
    return labels

