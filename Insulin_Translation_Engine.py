print('[SYSTEM] Parsing File For Translation : sample_insulin.fasta')
sequence = ''
with open('sample_insulin.fasta') as file:
    for line in file:
        if line.startswith('>'):
            continue
        sequence += line.replace('\n' , '')
translation_map = str.maketrans({'T':'U'})
mRNA_sequence = sequence.translate(translation_map)
print('mRNA Sequence : ' + mRNA_sequence)

start = mRNA_sequence.find('AUG')
coding_mRNA_sequence = mRNA_sequence[start:]
print('Coding mRNA Sequence : ' + coding_mRNA_sequence)

codon_table = {
    # U Block
    'UUU':'F', 'UUC':'F', 'UUA':'L', 'UUG':'L',
    'UCU':'S', 'UCC':'S', 'UCA':'S', 'UCG':'S',
    'UAU':'Y', 'UAC':'Y', 'UAA':'[STOP]', 'UAG':'[STOP]',
    'UGU':'C', 'UGC':'C', 'UGA':'[STOP]', 'UGG':'W',

    # C Block
    'CUU':'L', 'CUC':'L', 'CUA':'L', 'CUG':'L',
    'CCU':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P',
    'CAU':'H', 'CAC':'H', 'CAA':'Q', 'CAG':'Q',
    'CGU':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R',

    # A Block
    'AUU':'I', 'AUC':'I', 'AUA':'I', 'AUG':'M',
    'ACU':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T',
    'AAU':'N', 'AAC':'N', 'AAA':'K', 'AAG':'K',
    'AGU':'S', 'AGC':'S', 'AGA':'R', 'AGG':'R',

    # G Block
    'GUU':'V', 'GUC':'V', 'GUA':'V', 'GUG':'V',
    'GCU':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A',
    'GAU':'D', 'GAC':'D', 'GAA':'E', 'GAG':'E',
    'GGU':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G'
}
preproinsulin = ''
for i in range(0, len(coding_mRNA_sequence), 3):
    codon = coding_mRNA_sequence[i:i+3]
    amino_acid = codon_table.get(codon, '?')

    if amino_acid == '[STOP]':
        preproinsulin += amino_acid
        break

    preproinsulin += amino_acid
print('Preproinsulin Protein Sequence : ' + preproinsulin)
start = 24
proinsulin = preproinsulin[start:]
print('Proinsulin Protein Sequence : ' + proinsulin)
b_chain = proinsulin[0:30]
a_chain = proinsulin[65:]
print('Mature Insulin Protein Sequence : ')
print('Active B-Chain ( 30 AA ) : ' + b_chain)
print('/                    /')
print('Disulphide Bonds In Between Cysteines')
print('/                    /')
print('Active A-Chain ( 21 AA ) : ' + a_chain.strip('[STOP]'))












