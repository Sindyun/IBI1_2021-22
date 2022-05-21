#define the nucleotide content calculator as function "calculate()".
def calculate():
        sequence = input('input your string: ') #input a sequence first
        #use n to store numbers
        n1 = 0
        n2 = 0
        n3 = 0
        n4 = 0
        #calculate how many A or a in this sequence
        for i in range(0, len(sequence)):
            if sequence[i] == 'A' or sequence[i] == 'a':
                n1 += 1
        #calculate percentage
        pera = n1 / len(sequence)
        #print the result
        print("The percentage of 'A' or 'a' in this sequence is " + str(pera) + ".")
        #use the same way to print G T and C.
        for i in range(0, len(sequence)):
            if sequence[i] == 'T' or sequence[i] == 't':
                n2 += 1
        pert = n2 / len(sequence)
        print("The percentage of 'T' or 't' in this sequence is " + str(pert) + ".")
        for i in range(0, len(sequence)):
            if sequence[i] == 'G' or sequence[i] == 'g':
                n3 += 1
        perg = n3 / len(sequence)
        print("The percentage of 'G' or 'g' in this sequence is " + str(perg) + ".")
        for i in range(0, len(sequence)):
            if sequence[i] == 'C' or sequence[i] == 'c':
                n4 += 1
        perc = n4 / len(sequence)
        print("The percentage of 'C' or 'c' in this sequence is " + str(perc) + ".")

#Example:
#calculate()
#input your string: >? atgccgtacgtcgtcagcattgatc
#The percentage of 'A' or 'a' in this sequence is 0.2.
#The percentage of 'T' or 't' in this sequence is 0.28.
#The percentage of 'G' or 'g' in this sequence is 0.24.
#The percentage of 'C' or 'c' in this sequence is 0.28.
