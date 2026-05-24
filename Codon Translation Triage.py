codons = ["ATG", "GTC", "TAA", "CCA", "TAG", "GTT", "TGA", "ACT"]
for index, codon in enumerate(codons):
    if codon == "ATG":
        print(f'Initiating Protein Synthesis [START] at {index}')
    elif codon in ["TAG", "TAA", "TGA"]:
        print(f'Termination Sequence Detected [STOP] at {index}')
    else :
        print(f'Elongating peptide chain at {index}')

