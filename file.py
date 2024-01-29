from read import ReadPdf,ReadDoc,ReadDocx
import pandas as pd
from IPython.display import display
from clusters import TFidfVector,OneCluster,TwoCluster

import os
import asyncio
import time

class FileClass(object):
    def __init__(self):
        self.clustersfile = []
        self.listfiles= []


    def AbsolutePath(self,path):#обход по папкам
        tic = time.perf_counter()
        self.listfiles=WalkDir(path)
        smallfile,bigfile=ChekingSize(self.listfiles)                
        if len(WalkList(bigfile))>1:        
            smallvector=TFidfVector(WalkList(smallfile))
            bigvector=TFidfVector(WalkList(bigfile))
            self.clustersfile=TwoCluster(smallvector,bigvector)
        else:
            artext=WalkList(self.listfiles)       
            vector=TFidfVector(artext)               
            self.clustersfile=OneCluster(vector)        
        toc = time.perf_counter()
        print(f"Вычисление заняло {toc - tic:0.4f} секунд")
    
    def CreateDirectory(self,twopath):
        twopath=os.path.join(twopath,'dir')
        print(self.listfiles)
        print(self.clustersfile)
        print(''.split(twopath)[1])
        os.mkdir(twopath)
        for cluster in range(len(self.clustersfile)):
            pathcluster=os.path.join(twopath,"cluster_%i"%(self.clustersfile[cluster]))     
            if(not os.path.isdir(pathcluster)):  
                os.mkdir(pathcluster)            
            print(self.listfiles[cluster])
            print(pathcluster)    
            os.rename(self.listfiles[cluster],pathcluster)

def Data(file,p):#прочтение документов
    if (p[1]=='.pdf'):
        print(file)  
        return ReadPdf(file)#
    elif (p[1]=='.docx'):
        print(file)  
        return ReadDocx(file)#
    elif (p[1]=='.doc'):        
        print(file)  
        return ReadDoc(file)#



def Data(file,p):#прочтение документов
    if (p[1]=='.pdf'):
        print(file)  
        return ReadPdf(file)#
    elif (p[1]=='.docx'):
        print(file)  
        return ReadDocx(file)#
    elif (p[1]=='.doc'):        
        print(file)  
        return ReadDoc(file)#

def Exeption(p):
    if(p[1]=='.pdf'or p[1]=='.docx'or p[1]=='.doc'):   
        return True
    else:
        return False


def WalkDir(path):
    listfiles=[]
    for dirs,folden,files in os.walk(path):
        for file in files:          
            if Exeption(os.path.splitext(file)):
                listfiles.append(os.path.join(dirs,file))
    return  listfiles

def ChekingSize(listfile):
    smallfile=[]
    bigfile=[]
    for file in listfile:
        if os.stat(file).st_size<5242880:
            smallfile.append(file)
        else :
            bigfile.append(file)
    return (smallfile,bigfile)

def WalkList(List):    
    artext=[]
    for file in List:
        p=os.path.splitext(file)
        predfile=Data(file,p)
        if(ChekingNone(List,predfile,file)):
            artext.append(predfile)
            predfile=None
    return artext
    

def ChekingNone(List,predfile,file):
    if (predfile is not None):
        return True
    else :
        List.remove(file)
        return False

           

def WalkListFile(listfiles):
    smallfile=[]
    for i in listfiles:
        if os.stat(i).st_size>52428800:
            smallfile.append(i)
    return smallfile
    
    



    
    


