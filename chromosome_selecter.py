#! /usr/bin/python
# reads in a fasta file with multiple >'s designating chromosomes or sequencesself.
# takes the name of the chromosome you need and outputs that chromosome to a new files
# example useage:
# /path/to/chromosome_selecter.py --alignment_file /path/to/fasta --chr_name {CHROMOSOME NAME} --output_name {FILE OUTPUT NAME}

import argparse

def parse_args():
    parser = argparse.ArgumentParser(description = 'Take name of chromosome and output a file containing only that chromosome')
    parser.add_argument('--alignment_file')
    parser.add_argument('--chr_name')
    parser.add_argument('--output_name')
    return parser.parse_args()

def main():
    # read in files
    args = parse_args()

    file = open(args.alignment_file,'r')
    data = file.read()
    split_data = data.split('>')

    output = open(str(args.output_name),'w')

    for chunk in split_data:
        if str(args.chr_name) in chunk:
            output.write('>')
            output.write(chunk)

    output.close()
    file.close()




if __name__ == '__main__':
    main()
