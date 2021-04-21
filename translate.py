#! /usr/bin/env python3

import sys

def translate_sequence(rna_sequence, genetic_code):
    """Translates a sequence of RNA into a sequence of amino acids.

    Translates `rna_sequence` into string of amino acids, according to the
    `genetic_code` given as a dict. Translation begins at the first position of
    the `rna_sequence` and continues until the first stop codon is encountered
    or the end of `rna_sequence` is reached.

    If `rna_sequence` is less than 3 bases long, or starts with a stop codon,
    an empty string is returned.
    """
    if rna_sequence:
        seq=rna_sequence.upper()
        if len(seq)>=3:
            if seq[0:3]=='UAA' or seq[0:3]=='UAG' or seq[0:3]=='UGA':
                return ''
            else:
                trans=''
                remain=len(seq)%3
                for i in range(0, (len(seq)-remain),3):
                    codon=genetic_code[seq[i:i+3]]
                    if codon == '*':
                        break
                    trans += codon 
            return trans
        else:
            return ''
    else:
        return ''                

import re

def get_all_translations(rna_sequence, genetic_code):
    """Get a list of all amino acid sequences encoded by an RNA sequence.

    All three reading frames of `rna_sequence` are scanned from 'left' to
    'right', and the generation of a sequence of amino acids is started
    whenever the start codon 'AUG' is found. The `rna_sequence` is assumed to
    be in the correct orientation (i.e., no reverse and/or complement of the
    sequence is explored).

    The function returns a list of all possible amino acid sequences that
    are encoded by `rna_sequence`.

    If no amino acids can be translated from `rna_sequence`, an empty list is
    returned.
    """
    if rna_sequence:
        seq=rna_sequence.upper()
        trans=[]
        remain=len(seq)%3
        start_code='AUG'   
        start_sit=re.search(start_code, rna_sequence)
        for sit in range(0,(len(seq)-remain),3):
            if sit=='AUG':
                for i in range (sit.end(),(len(seq)-remain),3):     
                    codon=genetic_code[seq[i:i+3]]
                    trans.append(coden)     
            else:
                return [] 
        return trans

def get_reverse(sequence):
    """Reverse orientation of `sequence`.

    Returns a string with `sequence` in the reverse order.

    If `sequence` is empty, an empty string is returned.
    """
    if sequence:
        seq=sequence.upper()
        reverse_seq=seq[::-1]
        return reverse_seq
    else:
        return''

def get_complement(sequence):
    """Get the complement of `sequence`.

    Returns a string with the complementary sequence of `sequence`.

    If `sequence` is empty, an empty string is returned.
    """
    complementary={"A":"U","U":"A","G":"C","C":"G"}
    if sequence:
        seq=list(sequence.upper())
        seq=[complementary[base] for base in seq]
        return ''.join(seq)
    else:
        return''
def reverse_and_complement(sequence):
    """Get the reversed and complemented form of `sequence`.

    Returns a string that is the reversed and complemented sequence
    of `sequence`.

    If `sequence` is empty, an empty string is returned.
    """
    if sequence:
        revseq=get_reverse(sequence)
        revcompseq=get_complement(revseq)
        return revcompseq
    else:
        return''

def get_longest_peptide(rna_sequence, genetic_code):
    """Get the longest peptide encoded by an RNA sequence.

    Explore six reading frames of `rna_sequence` (the three reading frames of
    `rna_sequence`, and the three reading frames of the reverse and complement
    of `rna_sequence`) and return (as a string) the longest sequence of amino
    acids that it encodes, according to the `genetic_code`.

    If no amino acids can be translated from `rna_sequence` nor its reverse and
    complement, an empty string is returned1.
    """
    pass 
    peptides = get_all_translations(rna_sequence = rna_sequence,
            genetic_code = genetic_code)
    rev_comp_seq = reverse_and_complement(rna_sequence)
    rev_comp_peptides = get_all_translations(rna_sequence = rev_comp_seq,
            genetic_code = genetic_code)
    peptides += rev_comp_peptides
    if not peptides:
        return ""
    if len(peptides) < 2:
        return peptides[0]
    most_number_of_bases = -1
    longest_peptide_index = -1
    for peptide_index, aa_seq in enumerate(peptides):
        if len(aa_seq) > most_number_of_bases:
            longest_peptide_index = peptide_index
            most_number_of_bases = len(aa_seq)
    return peptides[longest_peptide_index]

if __name__ == '__main__':
    genetic_code = {'GUC': 'V', 'ACC': 'T', 'GUA': 'V', 'GUG': 'V', 'ACU': 'T', 'AAC': 'N', 'CCU': 'P', 'UGG': 'W', 'AGC': 'S', 'AUC': 'I', 'CAU': 'H', 'AAU': 'N', 'AGU': 'S', 'GUU': 'V', 'CAC': 'H', 'ACG': 'T', 'CCG': 'P', 'CCA': 'P', 'ACA': 'T', 'CCC': 'P', 'UGU': 'C', 'GGU': 'G', 'UCU': 'S', 'GCG': 'A', 'UGC': 'C', 'CAG': 'Q', 'GAU': 'D', 'UAU': 'Y', 'CGG': 'R', 'UCG': 'S', 'AGG': 'R', 'GGG': 'G', 'UCC': 'S', 'UCA': 'S', 'UAA': '*', 'GGA': 'G', 'UAC': 'Y', 'GAC': 'D', 'UAG': '*', 'AUA': 'I', 'GCA': 'A', 'CUU': 'L', 'GGC': 'G', 'AUG': 'M', 'CUG': 'L', 'GAG': 'E', 'CUC': 'L', 'AGA': 'R', 'CUA': 'L', 'GCC': 'A', 'AAA': 'K', 'AAG': 'K', 'CAA': 'Q', 'UUU': 'F', 'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'GCU': 'A', 'GAA': 'E', 'AUU': 'I', 'UUG': 'L', 'UUA': 'L', 'UGA': '*', 'UUC': 'F'}
    rna_seq = ("AUG"
            "UAC"
            "UGG"
            "CAC"
            "GCU"
            "ACU"
            "GCU"
            "CCA"
            "UAU"
            "ACU"
            "CAC"
            "CAG"
            "AAU"
            "AUC"
            "AGU"
            "ACA"
            "GCG")
    longest_peptide = get_longest_peptide(rna_sequence = rna_seq,
            genetic_code = genetic_code)
    assert isinstance(longest_peptide, str), "Oops: the longest peptide is {0}, not a string".format(longest_peptide)
    message = "The longest peptide encoded by\n\t'{0}'\nis\n\t'{1}'\n".format(
            rna_seq,
            longest_peptide)
    sys.stdout.write(message)
    if longest_peptide == "MYWHATAPYTHQNISTA":
        sys.stdout.write("Indeed.\n")
