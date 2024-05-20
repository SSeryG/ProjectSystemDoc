from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import AgglomerativeClustering
import pandas as pd
from nltk import ngrams
import os
import io
from scipy.sparse import csr_matrix
from analizationmetrics import AnalysisMetrics
import aiofiles

from threading import Thread


class ClustersClass(object):
    def __init__(self):        
        self.model=AgglomerativeClustering(distance_threshold=1.41,n_clusters=None,linkage='ward')  
        self.tfIdfVectorizer = TfidfVectorizer(ngram_range=(2,2),use_idf = True,sublinear_tf=True)
        self.data=pd.DataFrame()
    
    
    async def ReWriteIndexCSV(self,index):
        
        self.data.index=index
        self.ReWriteCSV(self.data)
        print(self.data)

    async def IndexCSV(self):
        if self.data.empty:
            self.data=await self.ReadCSV()
        return self.data.index

    async def ReWriteCSV(self,data):
        async with aiofiles.open('data/data.csv', mode='w',newline='\n',encoding='utf-8') as file:
            data = data.to_csv(index=True, header=True,)
            await file.write(data) 
    
    async def ReadCSV(self):
        async with aiofiles.open('data/data.csv', mode='r',newline='\n',encoding='utf-8') as file:
            data = await file.read()    
            data = pd.read_csv(io.StringIO(data), index_col=0, header=0)            
        return data
    
    def JoinData(self,data):
        self.data=pd.concat([self.data, data])
                  
        self.data=self.data.fillna(0)          
        self.data=self.data.drop_duplicates(ignore_index=True,keep='last')
        self.RemoveFirstversionFile
        
    def RemoveFirstversionFile(self):
        index=self.IndexCSV()
        for p in index:
            p=p.split('\\')
        for k in range(len(index)):
            for dup in range(k+1, len(index)):
                if index[k][len(index[k])]==index[dup][len(index[dup])] :
                    index[k].remove()
                    self.data=self.data.drop(index=k)


    async def LoadingFiles(self,data):         
        if self.data.empty:
            if not os.path.isdir('data'):
                os.mkdir('data')                              
            if os.path.isfile('data/data.csv'):
                self.data= await self.ReadCSV()
                await self.ReWriteCSV(data)  
                data=await self.ReadCSV()                      
                self.JoinData(data)
                print(self.data)
            await self.ReWriteCSV(data)             
        else:
            await self.ReWriteCSV(data)  
            data=await self.ReadCSV() 
            self.JoinData(data)
            print(self.data)
            await self.ReWriteCSV(data)
              

    async def Clusterization(self):        
        #try:            
            if self.data.empty:
                self.data=await self.ReadCSV()            
            labels=self.model.fit_predict(self.data)            
            print(labels)
            #AnalysisMetrics(self.data)
            return labels
        #except:
         #   errorbox.ErrorData()
        
    def TFidfVector(self,artext,index):#построение и вычисление частотности
        tfIdf = self.tfIdfVectorizer.fit_transform(artext)
        tokens=(self.tfIdfVectorizer.get_feature_names_out())
        df_tfidf =pd.DataFrame(tfIdf.toarray(),index, columns = tokens)             
        return df_tfidf
    
   

