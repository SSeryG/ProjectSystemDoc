from read import ReadPdf,ReadDoc,ReadDocx,ReadOdf
from clusters import ClustersClass
import os
import asyncio



class FileClass(object):
    def __init__(self):
        self.clustersfile = []
        self.listfiles= []
        self.clusters=ClustersClass()
        self.progress=''        

    def AbsolutePath(self,path,progress):#обход по папкам      
        self.progress=progress
        self.listfiles=self.WalkDir(path)
        if(self.listfiles is not None):
            smalllist=self.WalkList()

            smallvector=self.clusters.TFidfVector(smalllist,self.listfiles)     
            self.listfiles=smallvector.index
            
            asyncio.run(self.clusters.LoadingFiles(smallvector))
            

    def CreateDirectory(self,twopath):
        self.clustersfile=asyncio.run(self.clusters.Clusterization())
        self.listfiles=asyncio.run(self.clusters.IndexCSV())
        newlistfiles=[]
        twopath=os.path.join(twopath,'dir')                
        
        if(not os.path.isdir(twopath)):
           os.mkdir(twopath)
        for cluster in range(len(self.clustersfile)):            
            newlistfiles.append(self.CreateClaster(cluster,twopath))
        print(newlistfiles)
        asyncio.run(self.clusters.ReWriteIndexCSV(newlistfiles))
    
    def CreateClaster(self,cluster,twopath):
        
        pathcluster=os.path.join(twopath,"cluster_%i"%(self.clustersfile[cluster]+1))     
        if(not os.path.isdir(pathcluster)):  
            os.mkdir(pathcluster)            
        doc=self.listfiles[cluster]            
        namedoc=doc.split('\\')
        namedoc=namedoc[len(namedoc)-1]
        newpathdoc=os.path.join(pathcluster,namedoc)            
        os.rename(self.listfiles[cluster],newpathdoc)
        return newpathdoc


    def Data(self,file,p):#прочтение документов
        if (p[1]=='.pdf'):
            return ReadPdf(file)#
        elif (p[1]=='.docx'):
            return ReadDocx(file)#
        elif (p[1]=='.doc'):        
            return ReadDoc(file)#
        elif (p[1]=='.odf'):        
            return ReadOdf(file)#


    def Exeption(self,p):
        if(p[1]=='.pdf'or p[1]=='.docx'or p[1]=='.doc' or p[1]=='.odf'):   
            return True
        else:
            return False


    def WalkDir(self,path):
        listfiles=[]
        for dirs,folden,files in os.walk(path):
            for file in files:          
                if self.Exeption(os.path.splitext(file)):
                    listfiles.append(os.path.join(dirs,file))
        return  listfiles


    def WalkList(self):  
        progrssfile=100/len(self.listfiles)
        progvalue=progrssfile
        artext=[]
        for file in self.listfiles:
            p=os.path.splitext(file)        
            predfile=self.Data(file,p)
            self.progress["value"]=progvalue
            if (self.ChekingNone(predfile,file)):
                self.progress["value"]=progvalue                            
                artext.append(predfile)
                predfile=None
            progvalue+=progrssfile
                
        return artext
    

    def ChekingNone(self,predfile,file):
        print(predfile)
        if (predfile is not None):
            return True
        else :
            self.listfiles.remove(file)
            return False

    
    



    
    


