from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.cluster.hierarchy import ward, dendrogram, fcluster,linkage
from scipy.spatial.distance import pdist
import pandas as pd
from nltk import ngrams
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


tokens=[]

def CountVector(artext):#построенние вектора
    vec=CountVectorizer(ngram_range=(2,3),lowercase=False)
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
    
def ClusterBirch(X,indexfile):
    #samples = X.value
    y=pdist(X)
    y_ward=ward(y)
    print(fcluster(y_ward,1.25,criterion='distance'))
    print()
    print(fcluster(y_ward,1.3,criterion='distance'))
    print()
    print(fcluster(y_ward,1.35,criterion='distance'))
    print()
    print(fcluster(y_ward,1.4,criterion='distance'))
    print()
    print(fcluster(y_ward,1.45,criterion='distance'))
    print()
    print(fcluster(y_ward,1.5,criterion='distance'))
    
    
    Z = linkage(y, 'ward')  
    
    plt.figure(figsize=(25, 10))    
    plt.xlabel(indexfile)
    dn = dendrogram(Z)
    
    plt.show()


    #samples['cluster']=fcluster(mergings,1.5,criterion='distance')
    #samples['cluster']=fcluster(mergings,3,criterion='distance')
    
    
    

def token():#возвращение токена
    return tokens
    
