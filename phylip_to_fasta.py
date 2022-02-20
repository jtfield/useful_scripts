#! /usr/bin/python3

import os
import argparse
from Bio import SeqIO

def parse_args():
    parser = argparse.ArgumentParser(prog='phylip to fasta', \
        description='convert phylip file to fasta format.')
    parser.add_argument('--phylip_file', default='', help='input phylip option.')
    parser.add_argument('--out_file', default='', help='ourput file name.')

    return parser.parse_args()

def main():
    args = parse_args()

    # WOULD HAVE BEEN NICE IF THIS WORKED
    # biopython requires sequences to be the same length

    # records = SeqIO.parse(args.phylip_file, "phylip")
    #
    # print(records.format("fasta"))

    # count = SeqIO.write(records, args.out_file, "fasta")
    #
    # print("Converted %i records" % count)

    read_input = open(args.phylip_file, 'r').read()

    split_phylip = read_input.split('\n')

    output = open(args.out_file, 'w')

    for num, chunk in enumerate(split_phylip):
        if len(chunk) > 0:
            split_chunk = chunk.split(' ')
            # print(split_chunk[0])
            name = split_chunk[0]
            seq = split_chunk[1].replace('?','N')
            # print(name)
            output.write('>' + name)
            output.write('\n')
            output.write(seq)
            output.write('\n')

if __name__ == '__main__':
    main()
