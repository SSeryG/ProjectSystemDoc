from read import ReadPdf,ReadDoc,ReadDocx
from clusters import ClustersClass,TFidfVector
import os
import asyncio



class FileClass(object):
    def __init__(self):
        self.clustersfile = []
        self.listfiles= []
        self.clusters=ClustersClass()        

    async def AbsolutePath(self,path):#обход по папкам       
        self.listfiles=WalkDir(path)
        if(self.listfiles is not None):
            smalllist=await WalkList(self.listfiles)            
            smallvector=TFidfVector(smalllist,self.listfiles)     
            self.listfiles=smallvector.index
            
            self.clusters.LoadingFiles(smallvector)
            

    def CreateDirectory(self,twopath):
        self.clustersfile=self.clusters.Clusterization()
        self.clustersfile=self.clustersfile[len(self.clustersfile)-1-(len(self.listfiles)-1):]
        twopath=os.path.join(twopath,'dir')                
        
        if(not os.path.isdir(twopath)):
            os.mkdir(twopath)
        for cluster in range(len(self.clustersfile)):
            pathcluster=os.path.join(twopath,"cluster_%i"%(self.clustersfile[cluster]))     
            if(not os.path.isdir(pathcluster)):  
                os.mkdir(pathcluster)            
            doc=self.listfiles[cluster]            
            namedoc=doc.split('\\')
            namedoc=namedoc[len(namedoc)-1]
            newpathdoc=os.path.join(pathcluster,namedoc)
            os.rename(self.listfiles[cluster],newpathdoc)


async def Data(file,p):#прочтение документов
    if (p[1]=='.pdf'):
        return await ReadPdf(file)#
    elif (p[1]=='.docx'):
        return await ReadDocx(file)#
    elif (p[1]=='.doc'):        
        return await ReadDoc(file)#


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


async def WalkList(List):    
    artext=[]
    for file in List:
        p=os.path.splitext(file)
        predfile=await Data(file,p)
        if (ChekingNone(List,predfile,file)):
            artext.append(predfile)
            predfile=None
    return artext
    

def ChekingNone(List,predfile,file):
    if (predfile is not None):
        return True
    else :
        List.remove(file)
        return False

    
    



    
    


