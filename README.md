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

---

## Module 4: Genomic File Parsing Infrastructure

### 1. Scientific & Structural Context
In raw computational genomic analysis, sequence strings are structurally too vast to be embedded directly within programmatic source variables. High-throughput sequencing pipelines rely heavily on the standardized **FASTA text file format** to organize, compress, and transfer genomic data structures.

A standard FASTA infrastructure follows a binary architectural format:
* **The Header Line (`>`):** Initial single-line metadata register defining the structural source, accession code, and taxonomy profile of the sequence.
* **The Sequence Block:** Multi-line text layout containing the raw biological character sequences, structurally restricted to fixed column widths (typically 60-80 parameters) to optimize file parsing buffers.

### 2. Architectural Blueprint
The incoming processing framework transitions the repository from manual sequence declaration to disk I/O operational parsing. The underlying engine will target the initialized `sample_insulin.fasta` file, isolate and bypass descriptive header matrices, strip whitespace buffers, and merge split sequence arrays into a unified continuous data string for structural processing.

---

## Module 5: Automated Genomic File Parsing Engine

### 1. Scientific & Structural Context
Raw data files ingested from external sequence databases contain format-specific structural noise (metadata blocks and line-wrapping delimiters) that corrupts downstream analytical metrics if processed raw. 

This module serves as a data-cleaning pipeline, executing file-system extraction and sequence normalization to isolate functional genomic data from physical text assets.

### 2. Architectural Implementation
The processing script establishes a clean data pipeline to target, read, and normalize the raw template file:
1. **Context-Managed Ingestion:** Deploys a secure `with open()` file-system context manager, maintaining an active stream buffer to `sample_insulin.fasta` while guaranteeing automated memory reclamation.
2. **Metadata Elimination Gate:** Evaluates incoming text streams row-by-row using the structural character check `.startswith('>')`. When detected, an automated execution skip command (`continue`) drops the record to bypass the header segment.
3. **Array Accumulation & Sanitization:** Initializes an explicit string accumulator array outside the loop context. As the file stream processes valid nucleotide sequences, the pipeline executes a target character substitution matrix (`.replace('\n', '')`) to drop line-wrapping markers and unify the bases into a single continuous sequence parameter.

### 3. Verification & Compute Metrics
* **Target File Source:** `sample_insulin.fasta`
* **Computed Array Dimensions:** `420 base pairs`
* **Normalized In-Memory Sequence:** `AGCCCTCCAGGACAGGCTGCATCAGAAGAGGCCATCAAGCAGATCACTGTCCTTCTGCCATGGCCCTGTGGATGCGCCTCCTGCCCCTGCTGGCGCTGCTGGCCCTCTGGGGACCTGACCCAGCCGCAGCCTTTGTGAACCAACACCTGTGCGGCTCACACCTGGTGGAAGCTCTCTACCTAGTGTGCGGGGAACGAGGCTTCTTCTACACACCCAAGACCCGCCGGGAGGCAGAGGACCTGCAGGTGGGGCAGGTGGAGCTGGGCGGGGGCCCTGGTGCAGGCAGCCTGCAGCCCTTGGCCCTGGAGGGGTCCCTGCAGAAGCGTGGCATTGTGGAACAATGCTGTACCAGCATCTGCTCCCTCTACCAGCTGGAGAACTACTGCAACTAGACGCAGCCCGCAGGCAGCCCCCCACCCG`.

---

## Module 6: Global Biological Databases & Data Provenance

### 1. Scientific Context
In computational biology, data provenance and global standardization are critical for reproducible research. Genomic sequences generated via high-throughput sequencing platforms are archived across a decentralized, cross-synchronized network of international data repositories.

The core global architecture relies on the **International Nucleotide Sequence Database Collaboration (INSDC)**, which comprises three primary institutions:
* **NCBI (National Center for Biotechnology Information - USA):** Manages GenBank, a comprehensive public database of nucleotide sequences and supporting biomedical literature.
* **ENA (European Nucleotide Archive - UK/Europe):** Provides a comprehensive record of the world's nucleotide sequencing information, covering raw data, alignments, and functional annotations.
* **DDBJ (DNA Data Bank of Japan - Asia):** Serves as the primary data collection and dissemination hub for genomic assets generated across Asian research sectors.

### 2. Operational Application
Downstream computational pipelines (such as automated file parsers and sequence aligners) rely on unique identifiers—known as **Accession Numbers** (e.g., `NM_000207.3`)—assigned by these databases to guarantee absolute data integrity and version control when fetching raw FASTA assets for automated processing.

---

## Module 7: Genomic Translation and Post-Translational Processing Pipeline for Human Insulin (INS)

### 1. Project Overview
This project delivers a specialized bioinformatics pipeline designed to parse, transcribe, align, and translate the raw nucleotide sequence of the human insulin gene (*INS*) into its mature, hormone-active form. Designed as part of the Module 7 curriculum, the script automates the processing of NCBI Reference Sequence: `NM_000207.3` (Homo sapiens insulin, transcript variant 1, mRNA), mimicking both the transcriptional mechanics of the ribosome and the post-translational enzymatic processing occurring inside mammalian pancreatic beta cells.

The primary engineering hurdle resolved in this implementation is the mitigation of open reading frame (ORF) shifts caused by upstream non-coding sequences, ensuring 100% fidelity in protein synthesis without relying on static, fragile index assumptions.
---
### 2. Biological Architecture & Data Coordinates

Standard genomic data streams contain architectural layers that do not translate directly into structural proteins. This pipeline tracks the biological lifecycle of the *INS* transcript through four distinct molecular phases:

#### 1. The 5' Untranslated Region (5' UTR Runway)
The initial 59 nucleotides of the mRNA sequence (`AGCCCT...`) act as a ribosomal docking track. They do not possess amino acid coding instructions. The true Open Reading Frame begins strictly at index 59 with the initialization codon `AUG`.

#### 2. Preproinsulin (The Initial Translation Product)
Spanning from the `AUG` start codon to the terminating stop codon, this continuous 110-amino-acid chain represents the raw translation sequence. It contains the structural directives required for cellular routing but cannot yet execute metabolic signaling.

#### 3. Proinsulin (The Folded Precursor)
Pancreatic enzymes cleave the first 24 amino acids from the N-terminus. This omitted section is the **Signal Peptide**, a hydrophobic sequence whose sole purpose is navigating the growing protein through the Endoplasmic Reticulum membrane. Its removal yields Proinsulin (85 amino acids), which subsequently stabilizes via internal disulfide cross-linkages.

#### 4. Mature Human Insulin (The Dual-Chain Hormone)
To activate the hormone, the intracellular protease *Prohormone Convertase* excises the internal **C-Peptide loop** alongside its flanking dibasic cleavage markers (`RR` and `KR`). This cleavage divides the molecule into two distinct, covalently bonded polypeptide strands:
*   **Active B-Chain:** The initial 30 amino acids (`FVNQHLCGSHLVEALYLVCGERGFFYTPKT`)
*   **Active A-Chain:** The final 21 amino acids (`GIVEQCCTSICSLYQLENYCN`)

#### Coordinate Matrix Map
The pipeline navigates the transcript string using the following mathematical index slices:

| Molecular Segment | Length | Sequence Coordinates | Slice Logic (Python Syntax) |
| :--- | :--- | :--- | :--- |
| Full mRNA Transcript | 465 nt | Indices 0 to 464 | `mRNA_sequence` |
| Coding Sequence (CDS) | 333 nt | Indices 59 to 392 | `mRNA_sequence[start:]` |
| Preproinsulin Peptide | 110 AA | Indices 0 to 109 | `preproinsulin` |
| Proinsulin Segment | 85 AA | Indices 24 to 109 | `preproinsulin[24:]` |
| Active B-Chain | 30 AA | Indices 0 to 29 | `proinsulin[0:30]` |
| Omitted C-Peptide | 35 AA | Indices 30 to 64 | Deleted during processing |
| Active A-Chain | 21 AA | Indices 65 to 85 | `proinsulin[65:]` |
---
### 3. Pipeline Logic & Algorithmic Steps

The execution block inside `Insulin_Translation_Engine.py` handles data transformation through a five-stage architecture:

1.  **File Input and Normalization:** The FASTA file parser detects and skips the FASTA header string (`>NM_000207.3...`), extracts the raw multiline sequence lines, strips out structural newline characters (`\n`), and merges the broken fragments into one unbroken string.
2.  **Biochemical Transcription:** Utilizing a translation matrix map, the script converts DNA Thymine (`T`) bases into RNA Uracil (`U`) bases to prepare the data array for ribosomal simulation.
3.  **Dynamic Reading Frame Alignment:** Rather than deploying a hardcoded offset index, the pipeline searches the compiled transcript string using an automated `.find('AUG')` locator. This ensures that regardless of the 5' UTR runway length, the translation window matches the biological frame initialization.
4.  **Codon Translation Loop:** The script parses the sequence in sequential, non-overlapping triplets (3-nucleotide steps). Each triplet queries a global 64-key dictionary object to append the matching amino acid single-letter identifier, terminating cleanly when an explicit `[STOP]` condition is met.
5.  **Multi-Stage Digital Proteolysis:** The final module applies precise index slices to isolate the active B-chain and A-chain fragments, displaying them alongside a structural marker simulating the physical disulfide bridges connecting the chains.
---
### 4. Expected Output Structure
[SYSTEM] Parsing File For Translation : sample_insulin.fasta
mRNA Sequence : AGCCCUCCAGGACAG...
Coding mRNA Sequence : AUGGCCCUGUGGAUG...
Preproinsulin Protein Sequence : MALWMRLLPLLALLALWGPDPAAAFVNQHLCGSHLVEALYLVCGERGFFYTPKTRREAEDLQVGQVELGGGPGAGSLQPLALEGSLQKRGIVEQCCTSICSLYQLENYCN[STOP]
Proinsulin Protein Sequence : FVNQHLCGSHLVEALYLVCGERGFFYTPKTRREAEDLQVGQVELGGGPGAGSLQPLALEGSLQKRGIVEQCCTSICSLYQLENYCN[STOP]
Mature Insulin Protein Sequence : 
Active B-Chain ( 30 AA ) : FVNQHLCGSHLVEALYLVCGERGFFYTPKT
/                    /
Disulphide Bonds In Between Cysteines
/                    /
Active A-Chain ( 21 AA ) : GIVEQCCTSICSLYQLENYCN
---
### 5. Coder's Note
~ Initially, having not solidified my basics in the overall structure of human insulin and the sequence of events in it's translation, I was stuck with trying to translate the raw mRNA sequence generated from the FASTA file through my parsing, resulting in a ten day slump from speedrunning my coding journey. After coming to terms that perhaps it's not my code or the syntax but the lack of molecular knowledge and it's implementation where it all went wrong and the lacking dictionary I implemented to my code. After reviewing the conceptual aspects of insulin and the structural transformations it has to undergo in order to finally result in mature insulin, as in from preproinsulin to proinsulin (After removal of Signal peptide) and finally to mature insulin (After removal of C peptide which gives insulin it's structure), I finally realised I could then easily foresee the required logical approach. Finally, after updating my dictionary with the help of sources and fixing my syntax accordingly, I finally broke my ten day slump, successfully. I added lines to indicate the disulphide bonds between the sulphur atoms in the amino acids (Cysteine) of the A-Chain and B-Chain to visualise the structure as well as add a personal touch to my code XD.
