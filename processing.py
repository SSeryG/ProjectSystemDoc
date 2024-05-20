import nltk
#nltk.download('stopwords')
#nltk.download('punkt')
#nltk.download('snowball_data')
#nltk.download('perluniprops')
#nltk.download('universal_tagset')
#nltk.download('stopwords')
#nltk.download('nonbreaking_prefixes')
#nltk.download('wordnet')
#nltk.download('names')
from nltk.corpus import stopwords
import re
from pymorphy3 import MorphAnalyzer
#nltk.download('averaged_perceptron_tagger_ru')



regex=re.compile("[А-Яа-я]+")
male_names = nltk.corpus.names.words('male.txt')
female_names = nltk.corpus.names.words('female.txt')
stopw=stopwords.words('russian')#стоп слова
stopw.extend(male_names)
stopw.extend(female_names)
#stopw.extend(['сами','таких','иной','также','этим','этих','могут','которая','который','поэтому','само','которое','которыми'])
#stopw.extend(['любой','например','пример','наша','которого','глава','этими','каждого','ними','такую','которой', 'свой','такое'])
#stopw.extend(['которые','рисунок','таблица','которых','котором','какие','каком','какого','этому','либо','запятая', 'многом'])
#stopw.extend(['одной','должны','однако','могли','очень','нужно','одного','должно','вашего','можете','разных','такие','вашем'])
#stopw.extend(['стало','иначе','каждом','таким','каждый','такая','затем','причем','несколько','будем','будут','важными','важно'])
#stopw.extend(['важных','одним','любом','двух','число','вторая','второго','первый','каждое','разной','каким','какието','каких'])
#stopw.extend(['никаких','какиелибо','какиминибудь','какихто','никакие','какихлибо','изза','какую','какими','какова','никакой'])
#stopw.extend(['какойлибо','какому','своему','каких','каково','какомто','какое','никакого','каковы','какаято','какимто'])
#stopw.extend(['какоето','каков','каждой','вами','всем','свои','ваши','своих','вашей','самые','кроме','должен','попытаться'])
#stopw.extend(['некоторый','один','aaaaaaaaaa','самый','вопрос','таковой','вообще','смочь','мочь','решение','сложный'])
#stopw.extend(['сразу','возможно','десять','первый','большинство','должный','хотеть','иметь','номер','нужный','большой'])


def LemmatizeMorphWord(token,morph=MorphAnalyzer()):
    return  morph.parse(token)[0].normal_form

def LemmatizeMorphText(text):#выделение схожих слов
    return [LemmatizeMorphWord(w) for w in text]


def SumRe(text):#удаление символов и понижение регистров
    text= re.sub(r'[0123456789+]','',text)
    text= re.sub('-\n','',text)
    text= re.sub('-',' ',text)
    text= re.sub('\n',' ',text)
    text= text.lower()
    text= regex.findall(text)
    return text

def Token(text):
    if (text is not None):
        #tic = time.perf_counter()
           
        text=' '.join(SumRe(text))
               
        #print(text)
         
        words =nltk.word_tokenize(text)
        functors_pos = {'CONJ','PR','S-PRO','ADV-PRO','A-PRO','ADV','A-PRO=f','A-PRO=n','A-PRO=m','NUM'
                ,'NUM=acc','NUM=m','A=m','PRAEDIC','PART','ANUM=m','PARENT','ADV-PRO=abbr','A-PRO=pl'
                ,'ANUM=f','A-PRO=m','ADV=comp','A=pl','A=f','A=n','S-PRO=acc'}  # function words

        
        
        text=[words for words, pos in nltk.pos_tag(words, lang='rus')if pos not in functors_pos]

        lemma=LemmatizeMorphText(text)
        #data={
         #   'body':text
        #}
        #response=requests.post('https://functions.yandexcloud.net/d4ehhjs4n15v9t63q5tj',data)
        #lemma = response.json()
        #print(lemma)
      

        token=[w for w in lemma if not w in stopw and len(w)>3]  
        
        token=' '.join(token)       
        #print(text)
        #toc = time.perf_counter()
        #print(f"Вычисление заняло {toc - tic:0.4f} секунд")
        
    return token



    
