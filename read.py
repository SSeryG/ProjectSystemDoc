import fitz
from docx import Document
import win32com.client
from processing import Token


def ReadPdf(extractpdf):#чтение PDF файла
    try:
        pdffile=fitz.open(extractpdf,)
        text=""
        for page in pdffile:
            text =text+' '+ page.get_text()
        return Token(text)
    except:
        print('ошибка документ зашифрован')

def ReadDoc(extractdoc):#чтение DOC файла
    try:
        word = win32com.client.Dispatch("Word.Application")
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
        print('ошибка документ зашифрован')    

def ReadDocx(extractdocx):#чтение DOCX файла
    try:
        docx=Document(extractdocx)  
        text=""  
        for str in docx.paragraphs:
            text=text+' '+str.text
        return Token(text)
    except:
        print('ошибка документ открыт')


   
    
    
    