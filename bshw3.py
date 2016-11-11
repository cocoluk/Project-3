# Use https://www.si.umich.edu/programs/bachelor-science-
# information/bsi-admissions as a template.
# STEPS 
# Create a similar HTML file but 
# 1) Replace every occurrence of the word “student” with “AMAZING
# student.”  
# 2) Replace the main picture with a picture of yourself.
# 3) Replace any local images with the image I provided in media.  (You
# must keep the image in a separate folder than your html code.

import requests
from bs4 import BeautifulSoup
import urllib
import re

base_url = 'http://collemc.people.si.umich.edu/data/bshw3StarterFile.html'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, 'html.parser')

soup = soup.prettify()


soup = soup.replace('https://testbed.files.wordpress.com/2012/09/bsi_exposition_041316_192.jpg','media/me.png')
soup = soup.replace('student','AMAZING student')
soup = soup.replace('logo2.png','media/logo.png')

#print(soup)

html = open('final_file','w')
html.write(soup)
html.close()

#add commit push


#htmldoc = open('BSI admissions _ University of Michigan School of Information.htm','r+')
#soup = BeautifulSoup(htmldoc, 'html.parser')
#nice_soup = soup.prettify
#print (soup)

#for text_chunk in nice_soup.find_all('div', {'class':'field-item even'}, {'propert':'content:encoded'}):
#	print (text_chunk.p)
	#if text_chunk.h3:
	#	print(text_chunk.h3)









# Deliverables
# Make sure the new page is uploaded to your GitHub account.
