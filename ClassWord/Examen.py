import xml.etree.ElementTree as ET
from os import walk

def count_words(filename):
    tree = ET.parse('./news/'+file)
    root = tree.getroot()
    tmp = root.findall('.//se')
    return(len(tmp))

def list_to_file(res,filename):
    res_file = open(filename, 'w')
    for item in res:
        res_file.write(item+'\n')

f = []
words = []
mypath = './news';
for (dirpath, dirnames, filenames) in walk(mypath):
    f.extend(filenames)
    break
for file in f:
    words.append(file+'\t'+str(count_words(file)))
list_to_file(words,'task1.txt')

import pandas as pd

def read_data(filename):
    tree = ET.parse('./news/'+file)
    root = tree.getroot()
    name = root.find(".//*[@name='author']")
    topic = root.find(".//*[@name='topic']")
    return(name.attrib['content']+":"+topic.attrib['content'])

f = []
data = []
mypath = './news';
for (dirpath, dirnames, filenames) in walk(mypath):
    f.extend(filenames)
    break
for file in f:
    tmp = read_data(file).split(':')
    tmp_arr = [file,tmp[0],tmp[1]]
    data.append(tmp_arr)
df = pd.DataFrame(data,columns=["file","author","topic"])
df.to_csv("task_2.csv", sep=';', encoding='windows-1251')
