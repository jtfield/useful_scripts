#! /usr/bin/python

import os
import argparse
import shutil


def parse_args():
    parser = argparse.ArgumentParser(description='descp')
    parser.add_argument('--taxa_dir')
    parser.add_argument('--new_dir')
    parser.add_argument('--max_num')
    return parser.parse_args()

args = parse_args()
files = os.listdir(args.taxa_dir)
os.chdir(args.taxa_dir)
num = int(args.max_num)

for i in files:
    print(i)
    splitter = i.split('_')
    taxon_num = splitter[1]
    if taxon_num <= num:
        #shutil.move('./' + i, args.new_dir+i)
        print(i)
