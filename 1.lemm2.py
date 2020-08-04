import nltk
import codecs
import glob
import sys
from nltk.metrics import BigramAssocMeasures,TrigramAssocMeasures
from nltk.collocations import BigramCollocationFinder,TrigramCollocationFinder
import re

def lemm2(filename):
    
    file=codecs.open(filename,'r','utf8')
    #fout=codecs.open(filename.strip('.txt')+'-lemm2.txt','w','utf8')
    fh=file.read()

    ftext=nltk.tokenize.word_tokenize(fh)
    for i in ftext:
        if i==',':
            ftext.remove(i)
    ftext[0]=ftext[0].strip('\ufeff')
    print(ftext)
    
    rtex={}
    for i in range(0,len(ftext)):
        rtex[ftext[i]]=[]
    for i in range(0,len(ftext)):
        l=[]
        for k in range(0,len(ftext[i])):
            l.append(ftext[i][k])
            
            if ''.join(l) in ftext:
                #print(ftext[i],'->',''.join(l))
                if ''.join(l)!=ftext[i]:
                    rtex[ftext[i]].append(''.join(l))
                    
    print(rtex)


def file_lemm():
    
    path='C:/Users/durga/AppData/Local/Programs/Python/Python37/my programs/corpus/lemmatiser/*.txt'
    files=glob.glob(path)
    
    for i in files:
        print('FILE NAME',i.strip('C:/Users/durga/AppData/Local/Programs/Python/Python37/my programs/corpus/pseudo-word method/method-form-working/rough/'))
        lemm2(i)
#outputs
'''
file_lemm()
FILE NAME \KEY.tx
['ఇంటి', 'నుండి', 'బయటకు', 'వెళ్ళేటప్పుడు', 'తాళం', 'వెయ్యాలి', '.', 'ఇంటి', 'నుండి', 'బయటకు', 'వెళ్ళేటప్పుడు', 'తాళంలు', 'వెయ్యాలి', '.', 'బండికి', 'తాళంచే', 'వేయక', 'పోతే', 'దొంగిలుచుకు', 'పోతారు', '.', 'తాళంకి', 'చెవి', 'పోతె', 'దాన్ని', 'పగల', 'కొట్టాలి', '.', 'వాహనం', 'తాళంతో', 'పోయింది', '.']
{'ఇంటి': [], 'నుండి': [], 'బయటకు': [], 'వెళ్ళేటప్పుడు': [], 'తాళం': [], 'వెయ్యాలి': [], '.': [], 'తాళంలు': ['తాళం'], 'బండికి': [],
'తాళంచే': ['తాళం'], 'వేయక': [], 'పోతే': [], 'దొంగిలుచుకు': [], 'పోతారు': [], 'తాళంకి': ['తాళం'], 'చెవి': [], 'పోతె': [], 'దాన్ని': [], 'పగల': [], 'కొట్టాలి': [], 'వాహనం': [], 'తాళంతో': ['తాళం'], 'పోయింది': []}

FILE NAME \RUNBOOK.tx
['I', 'AM', 'A', 'RUNNER', '.', 'I', 'RUN', 'DAILY', '.', 'I', 'LIKE', 'RUNNING', '.', 'I', 'HAVE', 'BOOKED', 'A', 'TICKET', '.', 'TO', 'BOOK', 'TICKET', 'GO', 'TOCOUNTER', '.', 'IF', 'THE', 'BOOKING', 'IS', 'OPEN', 'BOOK', 'TICKETS', '.']
{'I': [], 'AM': ['A'], 'A': [], 'RUNNER': ['RUN'], '.': [], 'RUN': [], 'DAILY': [], 'LIKE': [], 'RUNNING': ['RUN'], 'HAVE': [],

'BOOKED': ['BOOK'], 'TICKET': [], 'TO': [], 'BOOK': [], 'GO': [], 'TOCOUNTER': ['TO'], 'IF': ['I'], 'THE': [], 'BOOKING': ['BOOK'], 'IS': ['I'], 'OPEN': [], 'TICKETS': ['TICKET']}
FILE NAME \ఊరు.tx
['ఊరు', 'ఊరులో', 'ఊరుకు', 'ఊరును', 'ఊరుపై', 'ఊరుకై', 'ఊరుకే', 'ఊరుతో', 'ఊరుతోటి']
{'ఊరు': [], 'ఊరులో': ['ఊరు'], 'ఊరుకు': ['ఊరు'], 'ఊరును': ['ఊరు'], 'ఊరుపై': ['ఊరు'], 'ఊరుకై': ['ఊరు'], 'ఊరుకే': ['ఊరు'], 'ఊరుతో': ['ఊరు'],

'ఊరుతోటి': ['ఊరు', 'ఊరుతో']}

FILE NAME \ప్రయోగం.tx
['ప్రయోగం', 'ప్రయోగంతో', 'ప్రయోగంలోకి', 'ప్రయోగంను', 'ప్రయోగాన్ని', 'ప్రయోగంకు', 'ప్రయోగానికి', 'ప్రయోగంలో', 'ప్రయోగానికి']

{'ప్రయోగం': [], 'ప్రయోగంతో': ['ప్రయోగం'], 'ప్రయోగంలోకి': ['ప్రయోగం', 'ప్రయోగంలో'], 'ప్రయోగంను': ['ప్రయోగం'], 'ప్రయోగాన్ని': [],
'ప్రయోగంకు': ['ప్రయోగం'], 'ప్రయోగానికి': [], 'ప్రయోగంలో': ['ప్రయోగం']}
>>>
'''


lex={'ప్రయోగం': [], 'ప్రయోగంతో': ['ప్రయోగం'], 'ప్రయోగంలోకి': ['ప్రయోగం', 'ప్రయోగంలో'], 'ప్రయోగంను': ['ప్రయోగం'], 'ప్రయోగాన్ని': [],'ప్రయోగంకు': ['ప్రయోగం'], 'ప్రయోగానికి': [], 'ప్రయోగంలో': ['ప్రయోగం']}

sen='దేశంలో ప్రయోగం రాకెట్ ప్రయోగంతో ఊరులో'

ftext=nltk.tokenize.word_tokenize(sen)
for i in ftext:
        if i==',':
            ftext.remove(i)
    
print(ftext)
    
rtex={}
for i in range(0,len(ftext)):
    rtex[ftext[i]]=[]
for i in range(0,len(ftext)):
    l=[]
    for k in range(0,len(ftext[i])):
        l.append(ftext[i][k])
            
        if ''.join(l) in ftext:
            #print(ftext[i],'->',''.join(l))
            if ''.join(l)!=ftext[i]:
                rtex[ftext[i]].append(''.join(l))
                    
print(rtex)
'''
['దేశంలో', 'ప్రయోగం', 'రాకెట్', 'ప్రయోగంతో', 'ఊరులో']
{'దేశంలో': [], 'ప్రయోగం': [], 'రాకెట్': [], 'ప్రయోగంతో': ['ప్రయోగం'], 'ఊరులో': []}
>>>
'''
