import nltk
import codecs
import re


def lemm2(filename,root,plural):                   
    file=codecs.open(filename,'r','utf8')
    fout=codecs.open(filename.strip('.txt')+'_lemm2.txt','w','utf8')
    fh=file.read()

    ftext=nltk.tokenize.word_tokenize(fh)

    

    for i in range(0,len(ftext)):
        if len(ftext[i])>=len(root):
            for j in range(0,len(root)):
                if ftext[i][j]==root[j]:
                    if j==len(root)-1:
                        ftext[i]=root
        if ftext[i]==plural:                
            ftext[i]=root
    fout.write(' '.join(ftext))
    #print(fout.getname())
    fout.close()
    file.close()

