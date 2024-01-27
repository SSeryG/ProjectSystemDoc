import nltk
#nltk.download('stopwords')
#nltk.download('punkt')
#nltk.download('snowball_data')
#nltk.download('perluniprops')
#nltk.download('universal_tagset')
#nltk.download('stopwords')
#nltk.download('nonbreaking_prefixes')
#nltk.download('wordnet')
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.stem import SnowballStemmer
import re
from pymystem3 import Mystem
from pymorphy3 import MorphAnalyzer

import time


regex=re.compile("[А-Яа-я]+")

stopw=stopwords.words('russian')#стоп слова
stopw.extend(['сами','таких','иной','также','этим','этих','могут','которая','который','поэтому','само','которое','которыми'])
stopw.extend(['любой','например','пример','наша','которого','глава','этими','каждого','ними','такую','которой', 'свой','такое'])
stopw.extend(['которые','рисунок','таблица','которых','котором','какие','каком','какого','этому','либо','запятая', 'многом'])
stopw.extend(['одной','должны','однако','могли','очень','нужно','одного','должно','вашего','можете','разных','такие','вашем'])
stopw.extend(['стало','иначе','каждом','таким','каждый','такая','затем','','','','','',''])

def Steemm(text,stemmer=SnowballStemmer('russian')):#выделаение основы
    return [stemmer.stem(s) for s in text]
    
def LemmatizeMystem(text,mys=Mystem()):#выделение схожих слов
    text= mys.lemmatize(' '.join(text)) 
    text =[w for w in text if w.strip()]
    return text

def LemmatizeMorphWord(token,morph=MorphAnalyzer()):
    return morph.parse(token)[0].normal_form

def LemmatizeMorphText(text):#выделение схожих слов
    return [LemmatizeMorphWord(w) for w in text]


def SumRe(text):#удаление символов и понижение регистров
    text=re.sub(r'[0123456789+]','',text)
    text=re.sub('-\n','',text)
    text=re.sub('-','',text)
    text=re.sub('\n',' ',text)
    text=text.lower()
    text=regex.findall(text)
    return text


def Token(text):#выделение токенов
    #print(stopw)
    
    if (text is not None):
        tic = time.perf_counter()
        text=SumRe(text)
               
        text=[w for w in text if not w in stopw and len(w)>3]
<<<<<<< HEAD
        #print(text) 
=======
        print(text) 
>>>>>>> 26b0df96911c86a4753907f449ddbbd36239bbdf
        text=LemmatizeMorphText(text)
        
    
        text=Steemm(text)
    
        text=' '.join(text)
        #print(text)
        toc = time.perf_counter()
        print(f"Вычисление заняло {toc - tic:0.4f} секунд")
    return text
    
    