#! /usr/bin/python
# Program to concatenate all sequences in an alignment that correspond to separate contigs in a genome
import argparse
import csv
import pandas as pd
from collections import defaultdict

def parse_args():
    parser = argparse.ArgumentParser(description = 'Concatenates separate contigs in a single file into a single sequence')
    parser.add_argument('--align_file')
    parser.add_argument('--out_file')
    parser.add_argument('--position_csv_file')
    return parser.parse_args()

def main():

    args = parse_args()

    data = (open(args.align_file, 'r').read())

    concat_seqs = []
    name_list = []
    file_name_and_seq_len_dict = {}
    taxon_name_and_seqs = defaultdict(list)
    final_dict = {}
    tuple_name_and_seq_len_list = []
    loci_count = 0
    csv_header = ['locus_position_number', 'locus_file_name', 'locus_length']
    tuple_name_and_seq_len_list.append(csv_header)

    split_file = data.split(">")
    for name_and_seq in split_file:
        if len(name_and_seq) > 1:
            loci_count+=1
            name_seq_split = name_and_seq.split("\n", 1)
            name = name_seq_split[0]
            seq = name_seq_split[1]
            seq = seq.replace("\n","")
            seq_len = len(seq)
            #print(seq_len)
            taxon_name_and_seqs[name].append(seq)
            file_name_and_seq_len_dict[name] = seq_len
            locus_len = seq_len
            name_and_len = [loci_count, name, seq_len]
            tuple_name_and_seq_len_list.append(name_and_len)
            
            #add seqs to list for concatenation
            concat_seqs.append(seq)
    #print(concat_seqs)
    
    #concat sequences
    final_concat_seq = ''.join(concat_seqs)
    #print(final_concat_seq)
    
    print(tuple_name_and_seq_len_list)
    
    #write out the csv of locus positions in the concatenated sequence and the concatenated sequence itself
    
    myFile = open(args.position_csv_file, 'w')
    with myFile:
        writer = csv.writer(myFile)
        writer.writerows(tuple_name_and_seq_len_list)

    output = open(args.out_file, 'w')
    output.write(">concat_sequence")
    output.write("\n")
    output.write(final_concat_seq)
    output.close()

    print("Writing complete")

if __name__ == '__main__':
    main()

