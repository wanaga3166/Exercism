#!/usr/bin/env python3

"""
    Exercism Python Exercice: Protein Translation
    URL: https://exercism.io/
"""

# Codon dictionary

Codon = {
    "AUG": "Methionine",
    "UUU": "Phenylalanine",
    "UUC": "Phenylalanine",
    "UUA": "Leucine",
    "UUG": "Leucine",
    "UCU": "Serine",
    "UCC": "Serine",
    "UCA": "Serine",
    "UCG": "Serine",
    "UAU": "Tyrosine",
    "UAC": "Tyrosine",
    "UGU": "Cysteine",
    "UGC": "Cysteine",
    "UGG": "Tryptophan",
    "UAA": "STOP",
    "UAG": "STOP",
    "UGA": "STOP"
}

def proteins(strand):
    protein=[]
    Triplet = [strand[i:i+3] for i in range(0, len(strand), 3)]
    for aa in Triplet:
        print(aa)
        if aa in ["UAA", "UAG", "UGA"]:            
            return protein
        elif aa in Codon:
            protein.append(Codon[aa])
    return(protein)

ARN="AUGUUUUCUUAAAUG"

proteins(ARN)
