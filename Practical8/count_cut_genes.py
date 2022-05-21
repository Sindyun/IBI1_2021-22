import re
#ask the user to input a filename as the new fasta file
fname=input('Type the file name here: ')
file = open(fname)
inp = file.read()
#use the same method to select genes
inp = re.sub(r'\n','',inp)
genes = re.split(r'>',inp)
EcoRI_cut_genes = []
for x in range(0,len(genes)):
    if re.search("GAATTC", genes[x]):
        EcoRI_cut_genes.append(genes[x])
#create lists to store gene name and sequence
gene_name = re.findall('gene:(......)',str(EcoRI_cut_genes))
sequence = re.findall('[A-T]{20,}',str(EcoRI_cut_genes))
#create a list to store the number of fragments
fragments=[]
for a in range(0,len(EcoRI_cut_genes)):
    x = re.findall("GAATTC",EcoRI_cut_genes[a])
    y = len(x)+1
    fragments.append(y)
#create a list to combine them together
cut_genes_list = []
for n in range(0,len(EcoRI_cut_genes)):
    cut_genes_list.append('>'+str(gene_name[n])+' '+str(fragments[n]) + '\n' + str(sequence[n]) + '\n')
#output the result in a fa file
cut_genes_list = "".join(cut_genes_list)
cut_genes2 = open('cut_genes2.fa','w')
cut_genes2.write(cut_genes_list)
cut_genes2.close()
