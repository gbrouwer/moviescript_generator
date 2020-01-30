import os
import sys
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup

#--------------------------------------------------------------------------------
if __name__ == '__main__':

	#for i in range(275):
	url = 'https://www.springfieldspringfield.co.uk/tv_show_episode_scripts.php?page=4'
	r = requests.get(url)
	soup = BeautifulSoup(r.text)
	#text = soup.get_text().findAll('div', {"class":"script-list-item"})[0].text.lower()

	print(soup)
