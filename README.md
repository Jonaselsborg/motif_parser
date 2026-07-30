# Amino Acid Sequence Position Finder in FASTA Files

This script searches one or more FASTA files for a user-specified amino acid sequence (pattern) and reports the **UniProt IDs** and **positions** where the pattern occurs.

## Requirements

- Python 3.8 or later  
- Packages:
  - `pandas`
  - `re` (standard library)
  - `os` (standard library)

## Input
1. Place all FASTA files to be searched in a folder named fasta/ in the same directory as the script.
2. When you execute the script, it will prompt you for the amino acid sequence (pattern) you want to search for.
* Example: entering KS will search for the motif "KS" in all protein sequences.
* Note: the script accepts regular expressions. Entering K[A-Z]E with search for the motif KxE (SUMO modification motif).

## Output
Results are written to the `result/` folder (created automatically if it does not exist).
The output file is named according to the search pattern, e.g.:
```bash
result/position_results_KS.txt
```

* The file is a tab-separated table with the following columns:
* Uniprot ID – extracted from the FASTA header
* Position in sequence – start position (1-based) of the pattern match

### Example Output
| Uniprot ID | Position in sequence |
|:----------:|:--------------------:|
| P09874     | 499                  |
| P09874     | 507                  |
| P09874     | 519                  |
| P33778     | 7                    |

## Usage
Run the script from the terminal:
```bash
python motif_parser.py
```
Then provide the sequence pattern when prompted. 
