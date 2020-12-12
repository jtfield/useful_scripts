#! /usr/bin/env python3
import argparse
import os
import re

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--align')
    parser.add_argument('--output_align')
    return parser.parse_args()

def separate_names_and_seqs(split_file):
    seqs = []
    for num, taxon in enumerate(split_file):
        if len(taxon) > 1:
            split_name_and_seq = taxon.split('\n', 1)
            #print(split_name_and_seq)
            seq = split_name_and_seq[1].replace('\n', '')
            #print(seq)

            seqs.append(seq)
    print(len(seqs))
    return seqs

def all_equal(lst):
    return lst[:-1] == lst[1:]

def iterative_all_equal(list_of_nucs):
    first_nuc = list_of_nucs[0]
    # print(list_of_nucs)
    for nuc in list_of_nucs:
        # print(nuc)
        if nuc != first_nuc:
            # print(nuc)
            return True

        elif nuc == first_nuc:
            continue

def check_lens(list_of_seqs):
    return len(list_of_seqs[:-1]) == len(list_of_seqs[1:])


def separate_variants(list_of_seqs):
    variants = []
    viable_nucs = {'A', 'C', 'G', 'T'}
    for num, nuc in enumerate(list_of_seqs[0]):
        if nuc.upper() in viable_nucs:
            nucs_at_this_position = []
            for seq in list_of_seqs:
                # seq = seq.upper()
                nucs_at_this_position.append(seq[num].upper())
            # check_equality = all_equal(nucs_at_this_position)
            # if check_equality != True:
            check_equality = iterative_all_equal(nucs_at_this_position)
            if check_equality == True:
                variants.append(num)
                print(num)
                # print(nucs_at_this_position)
                # print(len(nucs_at_this_position))
    return variants

def construct_variants_seqs(seqs, variant_positions):
    variant_seqs = []
    print(len(seqs))
    for num, seq in enumerate(seqs):
        current_seq_variants = []
        print(num)
        for position in variant_positions:
            # print(num)
            current_seq_variants.append(seq[position])
        variant_seqs.append(''.join(current_seq_variants))
    
    if check_lens(variant_seqs) == True:

        return variant_seqs

def make_output_align(variant_seqs, input_file, output_name):
    output = open(output_name, 'w')
    
    with open(input_file, 'r') as input:
        lines = input.readlines()
        name_count = 0
        for line in lines:
            if line.startswith('>'):
                # print(line)
                # print(name_count)
                output.write(line)
                output.write(variant_seqs[name_count])
                output.write('\n')
                name_count+=1
    output.close()

    # print(variant_seqs)
    # print(len(variant_seqs))

def main():
    args = parse_args()

    input = open(args.align, 'r')
    read_input = input.read()

    split_input = read_input.split('>')
    print(len(split_input))
    
    # print(split_input)
    
    separate_seqs = separate_names_and_seqs(split_input)
    print(len(separate_seqs))

    input.close()

    variants = separate_variants(separate_seqs)
    #print(variants)

    build_seqs = construct_variants_seqs(separate_seqs, variants)
    #print(build_seqs)

    make_output_align(build_seqs, args.align, args.output_align)





if __name__ == '__main__':
    main()