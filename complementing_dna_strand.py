# Determine the reverse complement of DNA string by reversing the string and replacing each symbol in the reversed
# string.
# A and T complement of each other
# G and T complement of each other

class DnaStrand:

    def __init__(self, s: str) -> object:
        self.s = s

    def reverse_dna(self):
        a = ''
        print('reversed string:',self.s[::-1])
        for i in self.s[::-1]:
            if i == 'A':
                a = a+'T'
            elif i == 'T':
                a = a+'A'
            elif i == 'G':
                a = a+'C'
            else:
                a = a+'G'
        print('complement_dna_strand:',a)
                

if __name__ == '__main__':
    d = DnaStrand('GTCAG')
    d.reverse_dna()




