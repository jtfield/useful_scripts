#!/usr/bin/env python

import os
import argparse
import subprocess
import csv
import numpy
import pandas as pd

def parse_args():
    parser = argparse.ArgumentParser(description = 'Take in a .csv file from pathogendb, pull the run SRA numbers and fastq dump them')
    parser.add_argument('--metadata_file')
    parser.add_argument('--max_num')
    return parser.parse_args()



def main():
    args = parse_args()

    data = args.metadata_file
    max_num = int(args.max_num)
    num_count = 0
    #with open('employee_birthday.txt') as csv_file:
    #    csv_reader = csv.reader(csv_file, delimiter=',')
    #    line_count = 0

    temp=pd.read_csv(data, usecols=['Run'])
    #print(temp)

    for index, row in temp.iterrows():
        if num_count < max_num and type(row['Run']) != float:
            num_count+=1
            print("value")
            print(row['Run'])
            print(type(row['Run']))
            subprocess.call(['fastq-dump', '--split-files', row['Run']])










if __name__ == '__main__':
    main()
