#! /usr/bin/python

import os
import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='descp')
    parser.add_argument('--taxa_dir')
    #parser.add_argument('--new_dir')
    parser.add_argument('--max_num')
    return parser.parse_args()

args = parse_args()
files = os.listdir(args.taxa_dir)

for i in files:
    splitter = i.split('_')
    num = int(splitter[1])
    if num <= int(args.max_num):
        print(num)
