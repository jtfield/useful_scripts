#! /usr/bin/env python3
import argparse
import os
from re import split

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--align')
    parser.add_argument('--output_align', default="NONE")
    return parser.parse_args()


def main():
    args = parse_args()

    lengths = {}

    input_file = open(args.align, 'r')
    read_input = input_file.read()

    split_file = read_input.split('>')

    
    output = open(args.output_align, 'w')

    for num, taxon in enumerate(split_file):
        split_name_and_seq = taxon.split('\n', 1)
        if len(split_name_and_seq) > 1:
            name = split_name_and_seq[0]
            seq = split_name_and_seq[1]

            joined_seq = ''.join(seq)
            joined_seq = joined_seq.replace('\n', '')

            seq_len = len(joined_seq)

            lengths[name] = seq_len
            print(name)
            print(seq_len)

            
            output.write('>' + name)
            output.write('\n')
            output.write(joined_seq)
            output.write('\n')

    


            


    
    
    
    input_file.close()




if __name__ == '__main__':
    main()