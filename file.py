from read import ReadPdf,ReadDoc,ReadDocx
import pandas as pd
from IPython.display import display
<<<<<<< HEAD
from clusters import TFidfVector,OneCluster,TwoCluster
=======
<<<<<<< HEAD
from clusters import TFidfVector,Cluster
=======
from clusters import CountVector,token,TFidf,TFidfVector,Cluster
>>>>>>> 26b0df96911c86a4753907f449ddbbd36239bbdf
>>>>>>> 52f278f2ec19434b5f812d54137555a5599c3cb2
import os
import asyncio
import time

class FileClass(object):
    def __init__(self):
        self.clustersfile = []
        self.listfiles= []

<<<<<<< HEAD
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

def Exeption(p):
    if(p[1]=='.pdf'or p[1]=='.docx'or p[1]=='.doc'):   
=======
<<<<<<< HEAD
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
=======


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
>>>>>>> 26b0df96911c86a4753907f449ddbbd36239bbdf
>>>>>>> 52f278f2ec19434b5f812d54137555a5599c3cb2
        return True
    else:
        return False
    
<<<<<<< HEAD
def WalkDir(path):
    listfiles=[]
=======
<<<<<<< HEAD
def WalkDir(path):
    listfiles=[]
=======
def WalkDir(path,listfiles):
>>>>>>> 26b0df96911c86a4753907f449ddbbd36239bbdf
>>>>>>> 52f278f2ec19434b5f812d54137555a5599c3cb2
    for dirs,folden,files in os.walk(path):
        for file in files:          
            if Exeption(os.path.splitext(file)):
                listfiles.append(os.path.join(dirs,file))
    return  listfiles
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 52f278f2ec19434b5f812d54137555a5599c3cb2

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
<<<<<<< HEAD
    
=======

=======
    
def IsNone(listfiles):
    for i in listfiles:
        if i!=None
           

def WalkListFile(listfiles):
    smallfile=[]
    for i in listfiles:
        if os.stat(i).st_size>52428800:
            smallfile.append(i)
    return smallfile
>>>>>>> 26b0df96911c86a4753907f449ddbbd36239bbdf
    
def AbsolutePath(path):#обход по папкам
    number=1
    tic = time.perf_counter()
<<<<<<< HEAD
    listfiles=WalkDir(path)
    smallfile,bigfile=ChekingSize(listfiles)    
    artext=WalkList(smallfile)
    artext1=WalkList(bigfile)
    bigvector=TFidfVector(artext1)
    indexfile.append(smallfile)
    indexfile.append(bigfile)
    clustersfile=Cluster(TFidfVector(artext),bigvector)
=======
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
>>>>>>> 26b0df96911c86a4753907f449ddbbd36239bbdf
    
    Cluster(TFidfVector(smallfile))
    #print(klast)
    
    toc = time.perf_counter()
    print(f"Вычисление заняло {toc - tic:0.4f} секунд")

    
    
def CreateDirectory(twopath):
    twopath=os.path.join(twopath,'dir')
    os.mkdir(twopath)
<<<<<<< HEAD
    for cluster in clustersfile:
        pathcluster=twopath+"\\cluster_%i"%cluster     
        if(not os.path.isdir(pathcluster)):  
            os.mkdir(pathcluster)        
        for file in indexfile:
            os.rename(file,pathcluster)


=======
>>>>>>> 26b0df96911c86a4753907f449ddbbd36239bbdf
    

>>>>>>> 52f278f2ec19434b5f812d54137555a5599c3cb2
#path='F:/'
#twopath='C:/Users/Сергей/Desktop/reader/dir/dir'
#AbsolutePath(twopath)

