#! /usr/bin/python

import os
import argparse
import shutil
import subprocess


def parse_args():
    parser = argparse.ArgumentParser(description='program to move or remove numbers beneath a certain number')
    parser.add_argument('-d', action='store_true', description='delete certain files')
    parser.add_argument('-m', action='store_true', description='move certain files')
    parser.add_argument('--taxa_dir')
    parser.add_argument('--new_dir')
    parser.add_argument('--max_num')
    return parser.parse_args()

def main():
    args = parse_args()

    if args.m == True:

        files = os.listdir(args.taxa_dir)
        os.chdir(args.taxa_dir)
        num = int(args.max_num)

        for i in files:
            splitter = i.split('_')
            taxon_num = splitter[1]
            tx = int(taxon_num)
            if tx <= num:
                #shutil.move('./' + i, args.new_dir+i)
                print(i)
                subprocess.call(['mv', args.taxa_dir+i, args.new_dir + '/'], stdout=PIPE, stderr=PIPE)
                #stdout, stderr = process.communicate()


    elif args.d == True:

        files = os.listdir(args.taxa_dir)
        os.chdir(args.taxa_dir)
        num = int(args.max_num)

        for i in files:
            splitter = i.split('_')
            taxon_num = splitter[1]
            tx = int(taxon_num)
            if tx <= num:
                print(i)
                subprocess.Popen(['rm', args.taxa_dir+i], stdout=PIPE, stderr=PIPE)
                #stdout, stderr = process.communicate()
