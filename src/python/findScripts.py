import requests
from collections import Counter 
from bs4 import BeautifulSoup
from tqdm import tqdm
import operator
import re
import sys
import numpy as np

class MovieScript(object):
    def __init__(self, url):
        self.movie = url
        self.url = url

    def get_movie(self):
        return self.movie

    def get_text(self):
        r = requests.get(self.url)
        soup = BeautifulSoup(r.text)
        return soup

    def parse_text(self):
        
        try:
            text = self.get_text().findAll('div', {"class":"scrolling-script-container"})[0].text.lower()
            text = text.replace("'",'')
            text = re.sub(r'[^a-zA-Z0-9.]', ' ',text)
        except:
            text = ''
        return text 

    def find_all_occurences(self):
        return Counter(self.parse_text())

    def get_all_occurences(self):
        sorted_occurences = sorted(self.find_all_occurences().items(), key=operator.itemgetter(1))
        return sorted_occurences


if __name__ == "__main__":

    #Load Shows
    episodes = []
    skip = int(sys.argv[1])
    indices = np.arange(116602)
    indices = indices[skip::8]
    
    with open('data/episodes.txt','r') as f:
        for line in f:
            episodes.append(line.rstrip())
    
    with open('data/scripts' + str(skip) + '.txt','a') as f:
        for i in range(len(indices)):
            index = indices[i]
            print(index,116602)
            episode = episodes[index]
            db = MovieScript(episode)
            soup = db.get_text()
            text = db.parse_text()
            text = text.replace('  ',' ')
            text = text.replace('  ',' ')
            text = text.replace('  ',' ')
            f.write(text + '\n')



