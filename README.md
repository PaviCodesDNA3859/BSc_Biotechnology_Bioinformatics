# Foundational Scripts: Computational Logic & Gene Analysis

This repository serves as a functional archive of core bioinformatics scripts developed to bridge fundamental programming architecture with molecular biology parameters. Every script is written from scratch to analyze genomic data structures, evaluate thermodynamic properties, and automate sequence triage workflows.

---

## 1: DNA GC-Content & Structural Thermodynamic Calculator

### 1. Scientific Context
In molecular biology, **GC-content** represents the exact percentage of nitrogenous bases in a DNA or RNA fragment that are either Guanine (G) or Cytosine (C). 

Unlike Adenine (A) and Thymine (T), which share only two hydrogen bonds, Guanine and Cytosine bind via **three hydrogen bonds**. Consequently, regions of DNA with an elevated GC-content exhibit significantly higher chemical and thermal stability. 

Calculating this metric is a critical prerequisite in computational biology for:
*   **PCR Primer Design:** Predicting the exact melting temperature required to unzip the double helix during amplification cycles.
*   **Genomic Mapping:** Identifying gene-dense regions (which typically exhibit higher GC-content) versus non-coding genomic "deserts."
*   **Taxonomic Classification:** Differentiating bacterial strains based on conserved genomic base ratios.

### 2. Algorithmic Workflow
The script processes a raw sequence string through an independent structural pipeline:
1.  **Sequence Ingestion:** Evaluates a target genomic string array.
2.  **Array Mapping:** Leverages optimized string manipulation methods (`.count()`) to scan the sequence and isolate the specific frequencies of `G` and `C` nucleotides.
3.  **Dimensional Analysis:** Uses native integer length functions (`len()`) to dynamically calculate the total base-pair count.
4.  **Mathematical Processing:** Computes the structural ratio using the standard thermodynamic percentage formula:

{GC Content (%)} = {Count(G)} + {Count(C)} / {Total Base Pairs} * 100

### 3. Execution & Analytical Output
Given the primary test sequence:
`"AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGT"`

The system successfully maps and outputs the following biochemical metrics directly to the console:
*   **Total Base Count:** 57 bp
*   **Guanine (G) Frequency:** 13
*   **Cytosine (C) Frequency:** 9
*   **Calculated GC-Content:** 38.596491228070175% (~38.59%)

*Thermodynamic Deduction:* A result of 38.59% classifies this sequence as AT-rich. In a practical laboratory setting, this template would require a significantly lower denaturation temperature threshold inside a thermal cycler due to the lower cumulative density of triple-hydrogen bonds.
