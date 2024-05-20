import fitz
from docx import Document
from win32com import client
from processing import Token
from odf.opendocument import load
import errorbox
import asyncio



def ReadPdf(extractpdf):#чтение PDF файла
    #try:
    pdffile=fitz.open(extractpdf,)
    text=""
    for page in pdffile:
        text =text+' '+ page.get_text()   
    return Token(text)
    #except:
        #print('ошибка документ зашифрован')

def ReadDoc(extractdoc):#чтение DOC файла
    try:
        word = client.Dispatch("Word.Application")
        word.visible = False
        wb=word.Documents.Open(extractdoc)
        doc = word.ActiveDocument
        text =""
        for str in doc.Paragraphs:
            text=text+' '+str.Range.Text
        doc.Close()
        word.Quit()
        return Token(text)
    except:
        errorbox.ErrorOpenFileDoc(extractdoc)
        return None

def ReadDocx(extractdocx):#чтение DOCX файла
    try:
        docx=Document(extractdocx)  
        text=""  
        for str in docx.paragraphs:
            text=text+' '+str.text
        return Token(text)
    except:
       errorbox.ErrorOpenFileDoc(extractdocx)
       return None

def ReadOdf(extractodf):
    try:
        odf=load(extractodf)  
        text=""  
        for str in odf.text.getElementsByType(odf.text.P):
            text=text+' '+str.text
        return Token(text)
    except:
       errorbox.ErrorOpenFileDoc(extractodf)
       return None   
   
    
    
    