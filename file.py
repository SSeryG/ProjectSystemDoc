from read import ReadPdf,ReadDoc,ReadDocx
import pandas as pd
from IPython.display import display
from clusters import CountVector,token,TFidf,TFdfVector,ClusterBirch
import os
import asyncio
import time




def Data(dirs,file,p):#прочтение документов
    if (p[1]=='.pdf'):
        print(file)
        return ReadPdf(os.path.join(dirs,file))#
    elif (p[1]=='.docx'):
        print(file)
        return ReadDocx(os.path.join(dirs,file))#
    elif (p[1]=='.doc'):
        print(file)
        return ReadDoc(os.path.join(dirs,file))#
    
def AbsolutePath(path):#обход по папкам
    tic = time.perf_counter()
    indexfile=[]
    artext=[]   
    for dirs,folden,files in os.walk(path):
        for file in files:                    
            p=os.path.splitext(file)        
            artext.append(Data(dirs,file,p))
            indexfile.append(file)
    #
    #bow_cv=CountVector(artext)
    #bow_cv_df = pd.DataFrame(data = bow_cv.toarray(),    # таблица
    #                    index= indexfile,                #
    #                    columns = token())    
    #            #
    #print(indexfile)
    bow_tf=TFdfVector(artext)

    
    #print(klast)
    
    #print(klast)
    
    toc = time.perf_counter()
    print(f"Вычисление заняло {toc - tic:0.4f} секунд")

    
    
def DirectoreDoc(twopath):
    twopath=os.path.join(twopath,'dir')
    os.mkdir(twopath)

#path='F:/'
#twopath='C:/Users/Сергей/Desktop/reader/dir/dir'
#AbsolutePath(twopath)

