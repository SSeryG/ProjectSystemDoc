import fitz
from docx import Document
from win32com import client
from processing import Token
import asyncio


async def ReadPdf(extractpdf):#чтение PDF файла
    #try:
    pdffile=fitz.open(extractpdf,)
    text=""
    for page in pdffile:
        text =text+' '+ page.get_text()
    return await Token(text)
    #except:
        #print('ошибка документ зашифрован')

async def ReadDoc(extractdoc):#чтение DOC файла
    #try:
    word = client.Dispatch("Word.Application")
    word.visible = False
    wb=word.Documents.Open(extractdoc)
    doc = word.ActiveDocument
    text =""
    for str in doc.Paragraphs:
        text=text+' '+str.Range.Text
    doc.Close()
    word.Quit()
    return await Token(text)
    #except:
     #   print('ошибка документ зашифрован')    

async def ReadDocx(extractdocx):#чтение DOCX файла
   # try:
        docx=Document(extractdocx)  
        text=""  
        for str in docx.paragraphs:
            text=text+' '+str.text
        return await Token(text)
   # except:
    #    print('ошибка документ открыт')


   
    
    
    