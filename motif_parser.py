# Coded by Jonas D. Elsborg
# jonas.elsborg@cpr.ku.dk
# 


import os
import re
import pandas as pd

# Input: Prompt user for the pattern to search in the fasta files
# pattern = "KS"
pattern = input("Please enter what the script should extract:\n")
pattern = pattern.upper()

# Function to parse fasta files and extract sequences
def fasta_parser(fasta):
    fasta_dir = {}
    for line in fasta:
        if re.search(r"^>", line):  # Detect header lines
            key = ""; value = []
            key = re.search(r"\|(.*?)\|", line).group(1)  # Extract Uniprot ID from header
        else:
            line = line.rstrip("\n")
            value.append(line)
            combined = "".join(value)
            fasta_dir[key] = combined
    return fasta_dir

# Function to find the positions of the specified pattern in the sequences
def lookup_aa(fasta_directory, amino):
    row_list = []
    for uniprot, sequence in fasta_directory.items():
        match_obj = re.finditer(amino, sequence)
        for site in match_obj:
            a_row_dict = {"Uniprot ID": uniprot, "Position in sequence": site.start() + 1}
            row_list.append(a_row_dict)
    df = pd.DataFrame.from_dict(row_list)
    df = df[["Uniprot ID", "Position in sequence"]]
    return df

# Function to process all fasta files in the 'fasta' folder
def process_fasta_folder(fasta_folder, pattern):
    result_data = pd.DataFrame()  # Initialize an empty dataframe to hold all results
    for filename in os.listdir(fasta_folder):
        if filename.endswith(".fasta"):
            file_path = os.path.join(fasta_folder, filename)
            with open(file_path, "r") as file_object:
                lines = file_object.readlines()
            fasta_parsed = fasta_parser(lines)  # Parse the fasta file to a dictionary
            output_dataframe = lookup_aa(fasta_parsed, pattern)  # Get the positions of the pattern
            result_data = pd.concat([result_data, output_dataframe], ignore_index=True)  # Combine results
    return result_data

# Ensure 'result' directory exists
if not os.path.exists("result"):
    os.makedirs("result")

# Process the fasta files in the 'fasta' folder and save results
result_dataframe = process_fasta_folder("fasta", pattern)

# Output the results to a file in the 'result' folder
output_file_name = f"result/position_results_{pattern}.txt"
result_dataframe.to_csv(output_file_name, sep='\t', index=False)
print(f"Results saved to {output_file_name}")
