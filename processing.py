import nltk
#nltk.download('stopwords')
#nltk.download('punkt')
#nltk.download('snowball_data')
#nltk.download('perluniprops')
#nltk.download('universal_tagset')
#nltk.download('stopwords')
#nltk.download('nonbreaking_prefixes')s
#nltk.download('wordnet')
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.stem import SnowballStemmer
import re
from pymorphy3 import MorphAnalyzer
#nltk.download('averaged_perceptron_tagger_ru')
import time


regex=re.compile("[А-Яа-я]+")

stopw=stopwords.words('russian')#стоп слова
stopw.extend(['сами','таких','иной','также','этим','этих','могут','которая','который','поэтому','само','которое','которыми'])
stopw.extend(['любой','например','пример','наша','которого','глава','этими','каждого','ними','такую','которой', 'свой','такое'])
stopw.extend(['которые','рисунок','таблица','которых','котором','какие','каком','какого','этому','либо','запятая', 'многом'])
stopw.extend(['одной','должны','однако','могли','очень','нужно','одного','должно','вашего','можете','разных','такие','вашем'])
stopw.extend(['стало','иначе','каждом','таким','каждый','такая','затем','причем','несколько','будем','будут','важными','важно'])
stopw.extend(['важных','одним','любом','двух','число','вторая','второго','первый','каждое','разной','','','','','',''])

def Steemm(text,stemmer=SnowballStemmer('russian')):#выделаение основы    
    return  [stemmer.stem(s) for s in text]

def LemmatizeMorphWord(token,morph=MorphAnalyzer()):
    return  morph.parse(token)[0].normal_form

def LemmatizeMorphText(text):#выделение схожих слов
    return  [LemmatizeMorphWord(w) for w in text]


def SumRe(text):#удаление символов и понижение регистров
    text= re.sub(r'[0123456789+]','',text)
    text= re.sub('-\n','',text)
    text= re.sub('-','',text)
    text= re.sub('\n',' ',text)
    text= text.lower()
    text= regex.findall(text)
    return text

def Token(text):
    if (text is not None):
        tic = time.perf_counter()
           
        text=' '.join(SumRe(text))
               
        #print(text)
         
        words = nltk.word_tokenize(text)
        functors_pos = {'CONJ', 'ADV-PRO', 'CONJ', 'PART'}  # function words

        text=[word for word, pos in nltk.pos_tag(words, lang='rus')if pos not in functors_pos]
        #print(text)
         
        text=[w for w in text if not w in stopw and len(w)>3]  

        text=LemmatizeMorphText(text)
        
        text=Steemm(text)
        
        token=' '.join(text)
        #print(text)
        toc = time.perf_counter()
        print(f"Вычисление заняло {toc - tic:0.4f} секунд")
        
    return token



    
