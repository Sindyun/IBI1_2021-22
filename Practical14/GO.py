from xml.dom.minidom import parse
import xml.dom.minidom
DOMTree = xml.dom.minidom.parse("go_obo.xml") # Parse the XML file into a DOM document object
collection = DOMTree.documentElement # Get the root element of the document
terms = collection.getElementsByTagName("term") # collect a list of "term" elements
dic1 = {} # create a dictionary to store GO father and GO sons
dic2 = {} # create another dictionary to store GO sons and GO father
for term in terms:
    GO_father = term.getElementsByTagName("id")[0] # collect elements by "id"
    GO_father = GO_father.childNodes[0].data
    dic1[GO_father] = []
    dic2[GO_father] = []
    GO_sons = term.getElementsByTagName("is_a")
    for element in GO_sons:
        dic1[GO_father].append(element.childNodes[0].data) # In dic1, add the childNodes after the GO_father
for term in terms:
    GO_Father = term.getElementsByTagName("id")[0]
    GO_Father = GO_Father.childNodes[0].data
    GO_Sons = term.getElementsByTagName("is_a")
    for element in GO_Sons:
        dic2[element.childNodes[0].data].append(GO_Father) # In dic2, add the GO_father after the childNodes
childnodes_store = {}
class GO():
# define a series of function
    def __init__(self):
        self.son = []
        self.father = []
        self.all_fathers = []

    def getson(self,son): # Get sons and store them in a list
        list = []
        list.append(son)
        son = list
        self.son = son

    def getfather(self):
        for everyson in self.son:
            self.father.extend(dic2[everyson])  # Use dic2 to search the corresponding father.
        self.father = list(set(self.father))
        self.all_fathers.extend(self.father)
        return self.father

    def change(self): # let the father as sons to search "grandfather"
        self.son = self.father
        self.father = []

    def number(self):
        global childnodes
        self.all_fathers = list(set(self.all_fathers))
        childnodes = len(self.all_fathers) # count childnodes in the term

    def store(self, son):
        global childnodes_store
        global childnodes
        childnodes_store[son] = childnodes
        childnodes = 0 # Store the number of childnodes.

GO=GO()
q = 0
for sons in dic2:
    GO.getson(sons)
    i = [1]
    while i!=[]:
        GO.getfather()
        i = GO.getfather()
        GO.change()
    GO.number()
    GO.store(sons)
    q = q + 1
    print(f'{sons} GO work has been done to {q}/47340') # Get the total number of childnodes.

import numpy as np
import math
from matplotlib import pyplot as plt
#print the boxplot
def make_boxplot(dict,title):
    childnodes_count = []
    for keys in dict:
        value = dict[keys]
        value = math.log(value+1)
        childnodes_count.append(value)
    plt.boxplot(childnodes_count,
                vert=True,
                whis=3,
                patch_artist=True,
                meanline=False,
                showbox=True,
                showcaps=True,
                labels=['term'],
                showfliers=True)
    plt.title(title)
    plt.ylabel('log(Node+1)')
    plt.show()
title_all = 'The box plot of the number of childnodes for all terms'
make_boxplot(childnodes_store, title_all)


translation = []
for term in terms:
    GO = term.getElementsByTagName('id')[0]
    GO = GO.childNodes[0].data
    df = term.getElementsByTagName('def')[0]
    defstr = df.getElementsByTagName('defstr')[0]
    if 'translation' in defstr.childNodes[0].data or "Translation" in defstr.childNodes[0].data:
        translation.append(GO)

class translation_GO():
# define a series of function
    def __init__(self):
        self.son=[]
        self.father=[]
        self.all_fathers=[]

    def getson(self,son):
        list = []
        list.append(son)
        son = list
        self.son = son
        # Get all the sons and store them in a list

    def getfather(self):
        for everyson in self.son:
            self.father.extend(dic2[everyson])
# Use dic2 to find the corresponding father.
        self.father = list(set(self.father))
# Eliminate all the elements in the list of
        self.all_fathers.extend(self.father)
        return self.father

    def change(self):
        self.son = self.father
        self.father = [] # let the father as sons to search "grandfather"

    def number(self):
        global childnodes
        self.all_fathers = list(set(self.all_fathers))
        childnodes = len(self.all_fathers) # count all the childnodes in the term

    def store(self,son):
        global childnodes_store
        global childnodes
        childnodes_store[son] = childnodes
        childnodes = 0  # Store the number of childnodes in a list.

GO_translation = translation_GO()
q=0
for sons in translation:
    i=[1]
    while i != []:
# Give i an initial value to let the loop continue.
        GO_translation.getfather()
        i = GO_translation.getfather()
        GO_translation.change()
    GO_translation.number()
    GO_translation.store(sons)
    q = q + 1
    print(f'{sons} GO translation work has been done to {q}/301')
# Get the total number of childnodes for all the terms
title_translation = 'The number of childnodes for terms involving translation'
make_boxplot(childnodes_store, title_translation)
#Print the boxplot for the childnodes of translation

#Comment: More childNodes are shown in translation terms than the overall GO.
