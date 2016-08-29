#!/usr/bin/env python
# coding: utf-8
import bs4
import codecs
import re

def getWordsFromXML(xml_filename):
    try:
        with open(xml_filename, 'r') as f:
            xml = f.read()
        f.close()
    except Exception as e:
        print('Unable to read ', xml_filename, ':', e)
        raise

    soup = bs4.BeautifulSoup(xml)

    #words = [repr(s) for s in soup.strings]
    words = soup.text.split('\n')

    p = re.compile(r'[a-z]+')
    words = [word for word in words if p.match(word) and ',' not in word]

    return list(set(words))

favorites_filename = 'doc/MDict_Favorites.xml'
history_filename = 'doc/MDict_History.xml'

favorites_words = getWordsFromXML(favorites_filename)
history_words = getWordsFromXML(history_filename)

#print favorites_words
#print type(favorites_words)

'''
from bs4 import UnicodeDammit
dammit = UnicodeDammit(favorites_words[1])
print dammit.original_encoding
'''

def writeText(words, filename):
    print type(words)
    try:
        with codecs.open(filename, 'w', 'utf8') as f:
            for word in words:
                f.write("%s\n" % word)
        f.close()
    except Exception as e:
        print('Unable to write words to', filename, ':', e)
        raise

favorites_text_filename = 'favorites.txt'
history_text_filename = 'history.txt'

writeText(favorites_words, favorites_text_filename)
writeText(history_words, history_text_filename)
