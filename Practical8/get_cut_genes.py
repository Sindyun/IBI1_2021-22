import re
#read the file
xfile = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
inp = xfile.read()
#To extract all genes from the file
inp = re.sub(r'\n','',inp)
genes = re.split(r'>',inp)
#create list to store the genes which can be cut by the EcoRI enzyme
EcoRI_cut_genes = []
for x in range(0,len(genes)):
    if re.search("GAATTC", genes[x]):
        EcoRI_cut_genes.append(genes[x])
#create a list to store gene names
gene_name = re.findall('gene:(......)',str(EcoRI_cut_genes))
#create a list to store sequence
sequence = re.findall('[A-T]{20,}',str(EcoRI_cut_genes))
#create a list to count gene lenth
gene_lenth = []
for i in range (0,len(sequence)):
    gene_lenth.append(len(sequence[i]))
#create a list to combine those elements together
cut_genes_list = []
for a in range(0,len(sequence)):
    cut_genes_list.append('>'+str(gene_name[a])+' '+str(gene_lenth[a]) + '\n' + str(sequence[a]) + '\n')
#Convert list to a string
cut_genes_list="".join(cut_genes_list)
#store them in a file and save.
cut_genes = open('cut_genes.fa','w')
cut_genes.write(cut_genes_list)
cut_genes.close()
