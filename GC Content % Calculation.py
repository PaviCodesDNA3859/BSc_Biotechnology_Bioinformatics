DNA_Sequence = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGT"
print('DNA Sequence: '+ DNA_Sequence)
print('Total Number Of Bases = ' + str(len(DNA_Sequence)))
print('Total Number Of Guanine Base = ' + str(DNA_Sequence.count('G')))
print('Total Number Of Cytosine Base = ' + str(DNA_Sequence.count('C')))
Total_Bases_Count = len(DNA_Sequence)
Guanine_Base_Count = DNA_Sequence.count('G')
Cytosine_Base_Count = DNA_Sequence.count('C')
GC_Content_Percentage = ((Guanine_Base_Count + Cytosine_Base_Count) / Total_Bases_Count) * 100
print('GC Content Percentage = ' + str(GC_Content_Percentage))
