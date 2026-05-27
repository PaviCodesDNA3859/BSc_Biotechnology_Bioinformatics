print('[SYSTEM] Parsing Target FASTA file : sample_insulin.fasta')

sequence = ''

with (open('sample_insulin.fasta' , 'r') as file ):
    for line in file:
      if line.startswith('>'):
                          continue
      sequence += line.replace('\n', '')

print('Isolated Sequence Length : ' + str(len(sequence)))
print('Normalized Sequence Data : ' + sequence)