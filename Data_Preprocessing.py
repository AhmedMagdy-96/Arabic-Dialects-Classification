#!/usr/bin/env python
# coding: utf-8

# In[101]:


import pandas as pd
import numpy as np
import regex as re
from nltk.corpus import stopwords


# In[102]:


def normalization(text):
    text = re.sub("[إأآا]", "ا", text)
    text = re.sub("ى", "ي", text)
    text = re.sub("ة", "ه", text)
    return text


# In[103]:


def hashtag(text):
    word_list = []
    for word in text.split():
        if word[0] == '#':
            word = word[1:]
            word = word.split('_')
            word = ' '.join(word)
        word_list.append(word)
    return ' '.join(word_list)


# In[104]:


def stop_words_removal(text):
    word_list=[]
    stopwords_list = stopwords.words('arabic')
    stopwords_list=[i for i in stopwords_list if i not in ['لك','ها','ما','لأ','هلا','إذا','إذن','أقل','إلى','إما','آه']]
    for word in text.split():
        if word not in stopwords_list:
            word_list.append(word)
    return ' '.join(word_list)


# In[105]:


def remove_emoji(text):
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               u"\U00002500-\U00002BEF"  # chinese char
                               u"\U00002702-\U000027B0"
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               u"\U0001f926-\U0001f937"
                               u"\U00010000-\U0010ffff"
                               u"\u2640-\u2642"
                               u"\u2600-\u2B55"
                               u"\u200d"
                               u"\u23cf"
                               u"\u23e9"
                               u"\u231a"
                               u"\ufe0f"  # dingbats
                               u"\u3030"
                               "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', text)


# In[108]:


def preprocesss(text):
    text = stop_words_removal(text)
    text = re.sub('@[^\s]+', ' ',text) #remove username
    text = re.sub('((www\.[^\s]+)|(https?:\/\/[^\s]+))',' ',text) #remove websites
    text = normalization(text)
    text = re.sub(r'(.)\1+', r'\1', text) #remove elongation
    text = re.sub("\d+", " ", text) #remove digits
    text = hashtag(text)
    trans = str.maketrans('','','''`÷×؛<>_()*&^%][ـ،/:"؟.,'{}~¦+|!”…“–ـ''') #punctuation
    text = text.translate(trans)
    text = remove_emoji(text)
    text = re.sub('[A-Za-z]+',' ',text) #remove english characters
    
    return text

