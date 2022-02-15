#!/usr/bin/env python3

import os
import argparse
import subprocess
import csv
import numpy
import pandas as pd

def parse_args():
    parser = argparse.ArgumentParser(description = 'Take in a .csv file from pathogendb, pull the run SRA numbers and fastq dump them')
    parser.add_argument('--metadata_file')
    parser.add_argument('--max_num', default = 1000)
    parser.add_argument('--sp', default=None)
    parser.add_argument('--delim', default=',', help='Set delimiter for the csv or tsv file (DEFAULT: \',\' )'  )
    return parser.parse_args()

def get_files_with_sp(data, species, max_num, delim):
    temp=pd.read_csv(data, usecols=['Run', 'Scientific name'], sep=delim, engine='python')
    #print(temp)
    num_count = 0

    for index, row in temp.iterrows():
        if num_count < max_num and type(row['Run']) != float and row['Run'] != None:
            # if row['Scientific name'] == species and type(row['Scientific name']) == str:
            if species in row['Scientific name'] and type(row['Scientific name']) == str:
                num_count+=1
                print("value")
                print(row['Run'])
                print(type(row['Run']))
                subprocess.call(['fasterq-dump', '--split-files', row['Run']])


def get_files_no_sp(data, max_num, delim):
    num_count = 0

    temp=pd.read_csv(data, usecols=['Run'], sep=delim, engine='python')

    for index, row in temp.iterrows():
        if num_count < max_num and type(row['Run']) != float:
            num_count+=1
            print("value")
            print(row['Run'])
            print(type(row['Run']))
            subprocess.call(['fasterq-dump', '--split-files', row['Run']])

def main():
    args = parse_args()

    data = args.metadata_file
    max_num = int(args.max_num)
    delim = args.delim

    if args.sp == None:
        get_files_no_sp(data, max_num, delim)

    else:
        get_files_with_sp(data, args.sp, max_num, delim)








if __name__ == '__main__':
    main()
