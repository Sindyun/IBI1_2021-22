import re
import numpy as np
#import the files and read them
seq1 = open("DLX5_human.fa")
seq2 = open("DLX5_mouse.fa")
seq3 = open("RandomSeq.fa")
human = seq1.read()
mouse = seq2.read()
random = seq3.read()
#extract amino acid sequences
human = re.sub(r'>(.+)\n','',human)
human = re.sub(r'\n','',human)
mouse = re.sub(r'>(.+)\n','', mouse)
mouse = re.sub(r'\n','',mouse)
random = re.sub(r'>(.+)\n','',random)
random = re.sub(r'\n','',random)
#create variables to store the number of differences
distance_human_mouse = 0
distance_human_random = 0
distance_mouse_random = 0
#calculate the number of different amino acids
for n in range(0, len(human)):  #compare the amino acids one by one
    if human[n] != mouse[n]:
        distance_human_mouse += 1 #if amino acids are different, add 1
#compare random and human
for i in range(len(human)):
    if random[i] != human[i]:
        distance_human_random += 1 #if amino acids are different, add 1
#compare random and mouse
for i in range(len(mouse)):
    if random[i] != mouse[i]:
        distance_mouse_random += 1 #if amino acids are different, add 1
#calculate the percentage of identical amino acids
human_mouse = (1-distance_human_mouse/len(human))*100
human_random = (1-distance_human_random/len(human))*100
mouse_random = (1-distance_mouse_random/len(random))*100
#print the outcomes
print('The number of different amino acids between human and mouse is ' + str(distance_human_mouse))
print('The percentage of identical amino acids between human and mouse is ' + str(human_mouse) + '%')
print('The number of different amino acids between human and random is ' + str(distance_human_random))
print('The percentage of identical amino acids between human and random is ' + str(human_random) + '%')
print('The number of different amino acids between mouse and random is ' + str(distance_mouse_random))
print('The percentage of identical amino acids between mouse and random is ' + str(mouse_random) + '%')

#Create a amino_acid dictionary and type in the amino acid list following the range of BLOSUM62 score matrix axis.
amino_acid = {'A':0,'R':1,'N':2,'D':3,'C':4,'Q':5,'E':6,'G':7,'H':8,'I':9,'L':10,'K':11,'M':12,'F':13,'P':14,'S':15,'T':16,'W':17,'Y':18,'V':19,'B':20,'Z':21,'X':22,'*':23}
BLOSUM62 = np.matrix([
            [4, -1, -2, -2,  0, -1, -1,  0, -2, -1, -1, -1, -1, -2, -1,  1,  0, -3, -2,  0, -2, -1,  0, -4],
            [-1,  5,  0, -2, -3,  1,  0, -2,  0, -3, -2,  2, -1, -3, -2, -1, -1, -3, -2, -3, -1,  0, -1, -4],
            [-2,  0,  6,  1, -3,  0,  0,  0,  1, -3, -3,  0, -2, -3, -2,  1,  0, -4, -2, -3,  3,  0, -1, -4],
            [-2, -2,  1,  6, -3,  0,  2, -1, -1, -3, -4, -1, -3, -3, -1,  0, -1, -4, -3, -3,  4,  1, -1, -4],
            [0, -3, -3, -3,  9, -3, -4, -3, -3, -1, -1, -3, -1, -2, -3, -1, -1, -2, -2, -1, -3, -3, -2, -4],
            [-1,  1,  0,  0, -3,  5,  2, -2,  0, -3, -2,  1,  0, -3, -1,  0, -1, -2, -1, -2,  0,  3, -1, -4],
            [-1,  0,  0,  2, -4,  2,  5, -2,  0, -3, -3,  1, -2, -3, -1,  0, -1, -3, -2, -2,  1,  4, -1, -4],
            [0, -2,  0, -1, -3, -2, -2,  6, -2, -4, -4, -2, -3, -3, -2,  0, -2, -2, -3, -3, -1, -2, -1, -4],
            [-2,  0,  1, -1, -3,  0,  0, -2,  8, -3, -3, -1, -2, -1, -2, -1, -2, -2,  2, -3,  0,  0, -1, -4],
            [-1, -3, -3, -3, -1, -3, -3, -4, -3,  4,  2, -3,  1,  0, -3, -2, -1, -3, -1,  3, -3, -3, -1, -4],
            [-1, -2, -3, -4, -1, -2, -3, -4, -3,  2,  4, -2,  2,  0, -3, -2, -1, -2, -1,  1, -4, -3, -1, -4],
            [-1,  2,  0, -1, -3,  1,  1, -2, -1, -3, -2,  5, -1, -3, -1,  0, -1, -3, -2, -2,  0,  1, -1, -4],
            [-1, -1, -2, -3, -1,  0, -2, -3, -2,  1,  2, -1,  5,  0, -2, -1, -1, -1, -1,  1, -3, -1, -1, -4],
            [-2, -3, -3, -3, -2, -3, -3, -3, -1,  0,  0, -3,  0,  6, -4, -2, -2,  1,  3, -1, -3, -3, -1, -4],
            [-1, -2, -2, -1, -3, -1, -1, -2, -2, -3, -3, -1, -2, -4,  7, -1, -1, -4, -3, -2, -2, -1, -2, -4],
            [1, -1,  1,  0, -1,  0,  0,  0, -1, -2, -2,  0, -1, -2, -1,  4,  1, -3, -2, -2,  0,  0,  0, -4],
            [0, -1,  0, -1, -1, -1, -1, -2, -2, -1, -1, -1, -1, -2, -1,  1,  5, -2, -2,  0, -1, -1,  0, -4],
            [-3, -3, -4, -4, -2, -2, -3, -2, -2, -3, -2, -3, -1,  1, -4, -3, -2, 11,  2, -3, -4, -3, -2, -4],
            [-2, -2, -2, -3, -2, -1, -2, -3,  2, -1, -1, -2, -1,  3, -3, -2, -2,  2,  7, -1, -3, -2, -1, -4],
            [0, -3, -3, -3, -1, -2, -2, -3, -3,  3,  1, -2,  1, -1, -2, -2,  0, -3, -1,  4, -3, -2, -1, -4],
            [-2, -1,  3,  4, -3,  0,  1, -1,  0, -3, -4,  0, -3, -3, -2,  0, -1, -4, -3, -3,  4,  1, -1, -4],
            [-1,  0,  0,  1, -3,  3,  4, -2,  0, -3, -3,  1, -1, -3, -1,  0, -1, -3, -2, -2,  1,  4, -1, -4],
            [0, -1, -1, -1, -2, -1, -1, -1, -1, -1, -1, -1, -1, -1, -2,  0,  0, -2, -1, -1, -1, -1, -1, -4],
            [-4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4,  1]])

# create a function to calculate the score
def BLOSUM62_score(seq1, seq2):
    score = 0
    seq1 = list(seq1)
    seq2 = list(seq2)
    for i in range(len(seq1)):
        score += BLOSUM62[amino_acid[seq1[i]], amino_acid[seq2[i]]]
    return score
#calculate the scores
score_human_mouse = BLOSUM62_score(mouse, human)
score_human_random = BLOSUM62_score(human, random)
score_mouse_random = BLOSUM62_score(mouse, random)
#print the outcomes
print('The BLOSUM score between human and mouse is ' + str(score_human_mouse))
print('The BLOSUM score between human and random is ' + str(score_human_random))
print('The BLOSUM score between mouse and random is ' + str(score_mouse_random))

#Here are the results:
#The number of different amino acids between human and mouse is 10
#The percentage of identical amino acids between human and mouse is 96.53979238754326%
#The number of different amino acids between human and random is 281
#The percentage of identical amino acids between human and random is 2.768166089965396%
#The number of different amino acids between mouse and random is 280
#The percentage of identical amino acids between mouse and random is 3.114186851211076%
#The BLOSUM score between human and mouse is 1490
#The BLOSUM score between human and random is -351
#The BLOSUM score between mouse and random is -348
#Compared with random sequences, the outcomes show a high similarity between human and mouse sequences.
#Such high genetic similarities suggest that humans and mice share a common ancestor in ancient times.
#(Virtually all species trace their roots back to a same ancestor.)
# Because of their genetic similarity to humans,mice have become good biological subjects when doing experiments.
