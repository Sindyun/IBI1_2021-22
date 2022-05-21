#create	a string variable seq
seq = "ATGCAATCGACTACGATCAATCGAGGGCC"
import re
#to find the number of restriction sites
x = re.findall("GAATTC",seq)
y = len(x)
#Output the result
print("The sequence would be cut into "+str(y+1)+" fragment if we applied the EcoRI enzyme to it.")
