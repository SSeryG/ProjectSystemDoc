from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.cluster.hierarchy import ward, dendrogram, fcluster,linkage
from scipy.cluster.hierarchy import complete, average, single,weighted
from scipy.cluster.hierarchy import centroid, median
from scipy.spatial.distance import pdist
import pandas as pd
from nltk import ngrams
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


tokens=[]

def CountVector(artext):#построенние вектора
    vec=CountVectorizer(ngram_range=(2,3))
    bow=vec.fit_transform(artext)
    print(bow.toarray())
    print(bow.shape)
    tokens.append(vec.get_feature_names_out())
    return TFidf(bow)

def TFidf(bow_cv):#вычисление слова из всего документа
    tfidf_trans = TfidfTransformer(smooth_idf = True, use_idf = True)
    tfidf_trans.fit(bow_cv)
    df_idf = pd.DataFrame(tfidf_trans.idf_, index = tokens, columns = ["idf_weights"])
    tf_idf_vec = tfidf_trans.transform(bow_cv)
    df_tfidf = pd.DataFrame(tf_idf_vec.toarray(), columns = tokens)
    print(df_tfidf.T)
    return tf_idf_vec

def TFdfVector(artext):#построение и вычисление частотности
    tfIdfVectorizer = TfidfVectorizer(ngram_range=(2,3),use_idf = True)
    tfIdf = tfIdfVectorizer.fit_transform(artext)
    tokens.append(tfIdfVectorizer.get_feature_names_out())
    df_tfidf = pd.DataFrame(tfIdf.toarray(), columns = tokens)
    print(df_tfidf)
    return df_tfidf
    
def Cluster(X):
    #samples = X.value
    y=pdist(X)
    y_ward=ward(y)
    Z = linkage(y_ward, 'ward')  
    
    plt.figure(figsize=(25, 10))    
    
    dn = dendrogram(Z)
    
    plt.show()

    y_average=average(y)
    Z = linkage(y_average, 'average')  
    
    plt.figure(figsize=(25, 10))    
    
    dn = dendrogram(Z)
    
    plt.show()

    y_complete=complete(y)
    
    Z = linkage(y_complete, 'complete')  
    
    plt.figure(figsize=(25, 10))    
    
    dn = dendrogram(Z)
    
    plt.show()
    y_single=single(y)
    Z = linkage(y_single, 'single')  
    
    plt.figure(figsize=(25, 10))    
    
    dn = dendrogram(Z)
    
    plt.show()

    y_weighted=weighted(y)

    Z = linkage(y_weighted, 'weighted')  
    
    plt.figure(figsize=(25, 10))    
    
    dn = dendrogram(Z)
    
    plt.show()
    y_centroid=centroid(y)
    Z = linkage(y_centroid, 'centroid')  
    
    plt.figure(figsize=(25, 10))    
    
    dn = dendrogram(Z)
    
    plt.show()
    y_median=median(y)    
    
    
    
    Z = linkage(X, 'median')  
    
    plt.figure(figsize=(25, 10))    
    
    dn = dendrogram(Z)
    
    

    print(fcluster(y_ward,1.5,criterion='distance'))
    print()
    print(fcluster(y_average,1.5,criterion='distance'))
    print()
    print(fcluster(y_complete,1.5,criterion='distance'))
    print()
    print(fcluster(y_single,1.5,criterion='distance'))
    print()
    print(fcluster(y_weighted,1.5,criterion='distance'))
    print()
    print(fcluster( y_centroid,1.5,criterion='distance'))
    print()
    print(fcluster( y_centroid,1.5,criterion='distance'))
    print()


    #samples['cluster']=fcluster(mergings,1.5,criterion='distance')
    #samples['cluster']=fcluster(mergings,3,criterion='distance')
    
    
    

def token():#возвращение токена
    return tokens
    
