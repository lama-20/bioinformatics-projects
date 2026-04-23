#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Import regular expressions library to search for overlapping ATG start codons
import re

# Import SeqIO from Biopython to read FASTA files containing DNA sequences
from Bio import SeqIO

# Import Seq class from Biopython to translate DNA sequence into protein sequence
from Bio.Seq import Seq


# Define stop codons used to terminate ORFs
# ORF must start with ATG and end with one of these codons
STOP_CODONS = {"TAA", "TAG", "TGA"}


# Function to calculate GC content percentage
# GC% = (Number of G + Number of C) / Total sequence length × 100
def gc_content(seq):

    # Convert sequence to uppercase to avoid lowercase problems
    seq = seq.upper()

    # If sequence is empty, return 0 to avoid division by zero
    if len(seq) == 0:
        return 0.0

    # Count total number of G and C nucleotides
    gc_count = seq.count("G") + seq.count("C")

    # Return GC percentage
    return (gc_count / len(seq)) * 100


# Function to count number of ATG start codons in the full sequence
# Uses overlapping search so ATGATG = 2 not 1
def count_atg(seq):

    # Convert sequence to uppercase
    seq = seq.upper()

    # Use regular expression to find overlapping ATG matches
    return len(re.findall(r"(?=ATG)", seq))


# Function to detect Open Reading Frames (ORFs)
# Rules:
# 1. Start with ATG
# 2. End with TAA, TAG, or TGA
# 3. Must be in the same reading frame
# 4. Analyze only forward strand (3 reading frames)
def find_orfs(seq):

    # Convert sequence to uppercase
    seq = seq.upper()

    # Empty list to store all detected ORFs
    orfs = []

    # Loop through the 3 forward reading frames: 0, 1, 2
    for frame in range(3):

        # Move codon by codon (step = 3)
        for i in range(frame, len(seq) - 2, 3):

            # Extract current codon
            codon = seq[i:i+3]

            # Check if codon is a start codon
            if codon == "ATG":

                # Search for the first valid stop codon after ATG
                for j in range(i + 3, len(seq) - 2, 3):

                    # Extract possible stop codon
                    stop_codon = seq[j:j+3]

                    # Check if stop codon is valid
                    if stop_codon in STOP_CODONS:

                        # Extract full ORF DNA from ATG to stop codon
                        orf_dna = seq[i:j+3]

                        # Translate DNA into amino acid sequence (protein)
                        # to_stop=True stops translation before stop codon
                        protein = str(Seq(orf_dna).translate(to_stop=True))

                        # Store ORF information inside dictionary
                        orfs.append({
                            "start": i + 1,      # Convert to 1-based index
                            "end": j + 3,        # End position inclusive
                            "dna": orf_dna,      # DNA sequence of ORF
                            "protein": protein   # Protein sequence
                        })

                        # Stop at first valid stop codon only
                        break

    # Sort ORFs by start position then end position
    orfs.sort(key=lambda x: (x["start"], x["end"]))

    # Return all ORFs found
    return orfs


# Main function to read FASTA file and print all required analysis
def analyze_fasta(file_path):

    # Variable to check if FASTA file contains any sequences
    found_any = False

    # Read all sequences from FASTA file
    for record in SeqIO.parse(file_path, "fasta"):

        found_any = True

        # Convert sequence into uppercase string
        seq = str(record.seq).upper()

        # Calculate sequence length
        length = len(seq)

        # Calculate GC content
        gc = gc_content(seq)

        # Count number of ATG codons
        atg = count_atg(seq)

        # Detect all ORFs
        orfs = find_orfs(seq)

        # Print general sequence information
        print(f"Sequence: {record.id}")
        print(f"Length: {length}")
        print(f"GC%: {gc:.2f}")
        print(f"ATG count: {atg}")
        print(f"ORFs found: {len(orfs)}")

        # Print each ORF separately
        for idx, orf in enumerate(orfs, start=1):

            print(f"\nORF {idx}:")
            print(f"Start: {orf['start']}")
            print(f"End: {orf['end']}")
            print(f"DNA: {orf['dna']}")
            print(f"Protein: {orf['protein']}")

        # Print separator line between sequences
        print("\n" + "-" * 50)

    # If FASTA file has no sequences
    if not found_any:
        print("No sequences found in the FASTA file.")


# Write FASTA file name here
# Example: Contig1.txt
file_path = "Contig1.txt"


# Run the full analysis on the FASTA file
analyze_fasta(file_path)


# In[ ]:




