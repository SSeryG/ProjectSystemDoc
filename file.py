from read import ReadPdf,ReadDoc,ReadDocx
import pandas as pd
from IPython.display import display
from clusters import CountVector,token,TFidf,TFidfVector,Cluster
import os
import asyncio
import time




def Data(dirs,file,p,number):#прочтение документов
    if (p[1]=='.pdf'):
        print('{}{}'.format(number,file))
        return ReadPdf(os.path.join(dirs,file))#
    elif (p[1]=='.docx'):
        print('{}{}'.format(number,file))
        return ReadDocx(os.path.join(dirs,file))#
    elif (p[1]=='.doc'):        
        print('{}{}'.format(number,file))        
        return ReadDoc(os.path.join(dirs,file))#

def Exeption(p):
    if(p[1]=='.pdf'or p[1]=='.docx'or p[1]=='.doc'):
        return True
    else:
        return False
    
def WalkDir(path,listfiles):
    for dirs,folden,files in os.walk(path):
        for file in files:          
            if Exeption(os.path.splitext(file)):
                listfiles.append(os.path.join(dirs,file))
    return  listfiles
    
def IsNone(listfiles):
    for i in listfiles:
        if i!=None
           

def WalkListFile(listfiles):
    smallfile=[]
    for i in listfiles:
        if os.stat(i).st_size>52428800:
            smallfile.append(i)
    return smallfile
    
def AbsolutePath(path):#обход по папкам
    number=1
    tic = time.perf_counter()
    listfiles=WalkDir(path,listfiles)
    bigfile=[]    
    smallfile=[]   
      
            if os.stat(os.path.join(dirs,file)).st_size>5242880:
               os.path.join(dirs,file)
            else:           
                p=os.path.splitext(file)
                predfile=Data(dirs,file,p,number)
                if ( predfile is not None):               
                    smallfile.append(predfile)
                    pathfile=os.path.join(dirs,file)
                    listfiles.append(pathfile)
                    number+=1
                    predfile=None
    
    Cluster(TFidfVector(smallfile))
    #print(klast)
    
    toc = time.perf_counter()
    print(f"Вычисление заняло {toc - tic:0.4f} секунд")

    
    
def DirectoreDoc(twopath):
    twopath=os.path.join(twopath,'dir')
    os.mkdir(twopath)
    

#path='F:/'
#twopath='C:/Users/Сергей/Desktop/reader/dir/dir'
#AbsolutePath(twopath)

