dna_template_strand = "TACGGCCTAATC"
print(f'DNA Template Strand : {dna_template_strand}')
coding_strand = str.maketrans({'A':'T', 'C':'G', 'G':'C' , 'T':'A'})
print('DNA Coding Strand : ' + dna_template_strand.translate(coding_strand))
mRNA_template_strand = str.maketrans({'T':'U'})
print('mRNA Transcript : ' + dna_template_strand.translate(coding_strand).translate(mRNA_template_strand))







