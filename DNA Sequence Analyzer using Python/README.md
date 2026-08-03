# DNA Sequence Analyzer using Python & Biopython

This project is a simple bioinformatics tool written in Python for analyzing DNA sequences from FASTA files.

The program performs several biological sequence analyses including:

- Sequence length calculation
- GC content percentage
- ATG start codon counting
- Open Reading Frame (ORF) detection
- DNA to protein translation

The project uses Biopython for FASTA parsing and sequence translation.

---

## Features

### 1. GC Content Calculation
Calculates the percentage of G and C nucleotides in the DNA sequence.

### 2. ATG Start Codon Detection
Counts all ATG codons including overlapping matches.

Example:
ATGATG = 2 start codons

### 3. ORF Detection
Detects Open Reading Frames based on these rules:

- Start codon: ATG
- Stop codons: TAA, TAG, TGA
- Same reading frame only
- Forward strand analysis (3 reading frames)

### 4. Protein Translation
Translates each detected ORF into its corresponding protein sequence.

---

## Technologies Used

- Python
- Biopython
- Regular Expressions (re)

---

## Input Format

The program reads DNA sequences from a FASTA file.

Example:

```fasta
>Sequence1
ATGAAATGAAAAATAG

