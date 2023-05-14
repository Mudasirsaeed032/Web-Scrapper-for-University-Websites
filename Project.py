import networkx as nx
import spacy
from spacy import displacy
from collections import Counter
import pandas as pd
from dframcy import DframCy
import pandas as pd
import matplotlib.pyplot as plt
import re
from IPython.display import Markdown, display
import pandas as pd
import requests
import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup
# import regex

# pd.set_option('max_rows', 400)
pd.options.display.max_rows = 600
pd.options.display.max_colwidth = 400


def dataall(url):
    url = requests.get(url)
    html = url.text
    text1 = BeautifulSoup(html, 'html.parser')
    h2_headers = []
    for header in text1:
        for paragraph in text1:
            header_contents = header.text
            # header_contents=header_contents.replace("\n","")
            # header_contents = header_contents.replace("\t", "")
            # header_contents = header_contents.replace("\r", "")
            # header_contents = header_contents.replace("/", " ")
            # header_contents = header_contents.replace(" ", "")
            h2_headers.append(header_contents)
            # print(h2_headers)
    return h2_headers

if __name__ == '_main_':

    urluaar1=[]
    urluaar1=("http://www.uaar.edu.pk/about-us.php?content_id=100")
    urluaar1=dataall(urluaar1)

    urluet=[]
    urluet = ("https://uet.edu.pk/aboutuet/aboutinfo/index.html?RID=about_uet_future_vision")
    urluet = dataall(urluet)

    urlcomsats1=[]
    urlcomsats1 = ("http://islamabad.comsats.edu.pk/")
    urlcomsats1 = dataall(urlcomsats1)

    urlcomsats2=[]
    urlcomsats2=("https://admissions.comsats.edu.pk/")
    urlcomsats2=dataall(urlcomsats2)

    # WRITING DATA IN A FILE
    #http://islamabad.comsats.edu.pk/

    Fast_data = [urluaar1]
    Giki_data = [urluet]
    Comsats_data = [urlcomsats1,urlcomsats2]

    File_object = open(r"Uaar.txt", "w+")


    try:
        File_object.writelines(urluaar1)
    finally:
        File_object.close()

    File_object2 = open(r"Uet.txt", "w+")

    try:
        File_object2.writelines(urluet)
    finally:
        File_object2.close()

    File_object3 = open(r"Comsats.txt", "w+")

    try:
        File_object3.writelines(urlcomsats1)
        File_object3.writelines(urlcomsats2)
    finally:
        File_object3.close()


# spacy.cli.download("en_core_web_sm")
nlp = spacy.load("en_core_web_sm")
print()
ans=True
while ans:
    print ("""
    1.Arid University
    2.Uet University
    3.Comsat University
    4.Exit/Quit
    """)
    ans=input("Choice University Website to read : ")
    if ans=="1":
        filepath = "Uaar.txt"
        break
    elif ans=="2":
        filepath = "uet.txt"
        break
    elif ans=="3":
        filepath = "comsats.txt"
        break
    elif ans=="4":
        exit()
    elif ans !="":
      print("\n Not Valid Choice Try again")


text = open(filepath, encoding='utf-8', errors='ignore').read()
#print (text)
document = nlp(text)

nouns = []
adjectives = []
verbs = []

for token in document:
    if (token.pos_ == "NOUN"):
        if(token.text!="%"):
            nouns.append(token.text)
    if token.pos_ == "ADJ":
         adjectives.append(token.text)
    if token.pos_ == "VERB":
         verbs.append(token.text)


nouns_tally = Counter(nouns)
adjectives_tally = Counter(adjectives)
verbs_tally = Counter(verbs)

print("---------------NOUNS---------------")
NounsData = pd.DataFrame(nouns_tally.most_common(), columns=['character', 'count'])
print(NounsData)

print("---------------Adjectives---------------")
AdjectiveData = pd.DataFrame(adjectives_tally.most_common(), columns=['character', 'count'])
print(AdjectiveData)

print("---------------Verbs---------------")
VerbsData = pd.DataFrame(verbs_tally.most_common(), columns=['character', 'count'])
print(VerbsData)

#Make a list of tokens and POS labels from document if the token is a word


Nouns_edges = []

for sent_i,sent in enumerate(document.sents):
    nouns=[]
    for token in sent:
        if (token.pos_ == "NOUN"):
            if(token.text!="%"):
                nouns.append(token.text)
    Nouns_edges.append(nouns)

for i in Nouns_edges:
    if not i:
        Nouns_edges.remove(i)
# for i in Nouns_edges:
#     print(i)

g=nx.DiGraph()
g.add_nodes_from(nouns)
#([('Girl','Symbolism')])
edge = []
for i in Nouns_edges:
    for j in i[1:]:
        edge.append([i[0],j])

g.add_edges_from(edge)



#nx.draw(g)


print("-----5 words near \"Quality\"------")
num=0
for sent_i,sent in enumerate(document.sents):
    nouns=[]
    for token in sent:
        if (token.pos_ == "NOUN"):
            if(token.text!="%"):
                num=num-1
            if(token.text=='quality'):
                num=6
                print("\n")
            elif(num>0):
                print(token.text)

print("-----Weighted of Nodes------")
nx.degree(g, weight='Weight')
weighted_degrees = dict(nx.degree(g, weight='Weight'))
nx.set_node_attributes(g, name='weighted_degree', values=weighted_degrees)

weighted_degree_df = pd.DataFrame(g.nodes(data='weighted_degree'), columns=['node', 'weighted_degree'])
weighted_degree_df = weighted_degree_df.sort_values(by='weighted_degree', ascending=False)
print(weighted_degree_df[:10])

print("Number of connected edges : ",g.number_of_edges())
print("Number of total nodes  : ",g.number_of_nodes())

plt.figure(figsize=(8,8))
nx.draw(g, with_labels=True, node_color='skyblue', width=.3, font_size=8)

plt.draw()
plt.show()