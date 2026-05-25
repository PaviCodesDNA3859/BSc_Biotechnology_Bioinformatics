# Foundational Scripts: Computational Logic & Gene Analysis

This repository serves as a functional archive of core bioinformatics scripts developed to bridge fundamental programming architecture with molecular biology parameters. Every script is written from scratch to analyze genomic data structures, evaluate thermodynamic properties, and automate sequence triage workflows.

---

## Module 1: DNA GC-Content & Structural Thermodynamic Calculator

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

---

## Module 2: Codon Translation Triage Pipeline

### 1. Scientific Context
During cellular translation, a biological ribosome reads an mRNA transcript sequentially in three-nucleotide blocks known as **codons** to construct peptide chains. The accurate initialization, elongation, and termination of this sequence dictate protein structure and cellular function.

This automated triage pipeline simulates ribosomal processing behavior across an active reading frame by categorizing inputs into distinct execution phases:
* **Initiation (START):** Triggered exclusively by the `ATG` codon, marking the origin point of translation.
* **Elongation:** Standard structural codons calling for tRNA-mediated amino acid delivery to append the growing peptide chain.
* **Termination (STOP):** Recognized via three universal stop signals (`TAA`, `TAG`, `TGA`), where molecular release factors dismantle the translation complex.

### 2. Algorithmic Workflow & Optimization
The architecture uses a high-efficiency single-pass iteration sequence:
1.  **Iterative Enumeration:** Implements Python's native `enumerate()` generator to track absolute index positioning coordinates in memory without running redundant linear searches.
2.  **Conditional Gating Matrix:** Deploys prioritized conditional blocks (`if`/`elif`/`else`) to evaluate strings.
3.  **Containment Evaluation:** Condenses stop codon evaluation logic using a lookup collection (`in ["TAA", "TGA", "TAG"]`), minimizing logical check overhead.

### 3. Execution & Analytical Output
Input Stream Array: `["ATG", "GTC", "TAA", "CCA", "TAG", "GTT", "TGA", "ACT"]`

The system evaluates the data register and generates a clean tracking log directly within the console terminal environment, mapping each operational phase to its specific positional coordinates.

---

## Module 3: The Central Dogma Automation Engine

### 1. Scientific Context
In molecular genetics, cellular transcription represents the foundational mechanism of the Central Dogma, where genetic blueprints stored inside double-stranded DNA are transcribed into single-stranded messenger RNA (mRNA) transcripts by RNA polymerase. 

To automate this process, a computational pipeline must respect two critical biochemical rules:
* **Complementary Pairing (Replication/Coding):** DNA strands run anti-parallel. The template strand must be mapped to its exact structural complement where Adenine (A) pairs with Thymine (T), and Cytosine (G) pairs with Guanine (C).
* **Ribose Transition (Transcription):** During RNA synthesis, Thymine is chemically unavailable and is entirely substituted by the pyrimidine base Uracil (U).

### 2. Algorithmic Workflow & Structural Optimization
A naive sequential execution string replacement (e.g., swapping A with T, then T with A) results in a logical collision where subsequent operations overwrite prior data arrays. 

To bypass this architectural limitation, this module implements a parallel mapping matrix:
1. **Simultaneous Translation Matrix:** Deploys `str.maketrans()` to evaluate the entire string layout in a single execution pass, mapping template bases to coding complements simultaneously without sequential data corruption.
2. **Transcript Conversion:** Executes an optimized single-character substitution pipeline (`.replace()`) to transition the established coding strand into an active mRNA sequence stream.

### 3. Execution & Analytical Output
* **Input DNA Template:** `TACGGCCTAATC`
* **Generated Coding Strand:** `ATGCCGGATTAG`
* **Final mRNA Transcript:** `AUGCCGGAUUAG`
