#!/usr/bin/env python

import os
import re
import sys
import subprocess
import argparse
from collections import defaultdict

def parse_args():
    parser = argparse.ArgumentParser(description = 'Run bowtie2 on multiple fastas and matching read sets')
    parser.add_argument('--ref_dir')
    parser.add_argument('--read_dir')
    parser.add_argument('--read_split_num')
    parser.add_argument('--ref_split_num')
    return parser.parse_args()

def main():
    args = parse_args()

    list_refs = os.listdir(args.ref_dir)
    print(list_refs)

    os.chdir(args.ref_dir)

    fasta_list = ['.fas', '.fa', '.fasta']

    file_count = 0
    count = 1
    for file in list_refs:
        file_count+=1

    for tail in fasta_list:
        for file in list_refs:
            if re.search(tail, file) and count <= file_count:
                count+=1
                subprocess.call(['bowtie2-build', file, file])
                #print(file)

    splt_list = []
    list_reads = os.listdir(args.read_dir)
    for item in list_reads:
        splt_item = item.split('_')
        splt_item[args.read_split_num] = int(splt_item[args.read_split_num])
        splt_list.append(splt_item)
    organize = sorted(splt_list, key=lambda file: file[args.read_split_num])
    #print(organize)

    dict_count = 0
    read_dict = defaultdict(list)
    for item in organize:
        item[args.read_split_num] = str(item[args.read_split_num])
        #print(item)
        joined = '_'.join(item)
        #print(joined)
        read_dict[int(item[args.read_split_num])].append(joined)
        dict_count+=1
    #print(read_dict)

    ref_dict = {}
    for item in list_refs:
        split_ref = item.split('_')
        ref_dict[int(split_ref[args.ref_split_num])] = item
    #print(ref_dict)

    for read,read_value in read_dict.items():
        for ref,ref_value in ref_dict.items():
            if read == ref:
                print(read_value[0])
                print(read_value[1])
                print(ref_value)

    #subprocess.call(['ls', args.read_dir'/newClade_2_01.R1_.fastq'])
    #subprocess.call(['pwd'])
                subprocess.call(['bowtie2', '-p', '6', '--very-fast', '-x', args.ref_dir + ref_value , '-1', args.read_dir + read_value[1] , '-2', args.read_dir + read_value[0] , '--al-conc' , args.read_dir + read_value[1]])

    #subprocess.call(['for i in $(ls )'])


    # for file in list_refs:
    #     for tail in fasta_list:
    #         if tail in file:
    #             print(file)
    #             subprocess.call(['bowtie2-build', file, file])






if __name__ == '__main__':
    main()
























# #!/usr/bin/env python
#
# import os
# import re
# import sys
# import subprocess
# import argparse
# from collections import defaultdict
#
# def parse_args():
#     parser = argparse.ArgumentParser(description = 'Run bowtie2 on multiple fastas and matching read sets')
#     parser.add_argument('--ref_dir')
#     parser.add_argument('--read_dir')
#     parser.add_argument('--read_split_num')
#     parser.add_argument('--ref_split_num')
#     return parser.parse_args()
#
# def main():
#     args = parse_args()
#
#     list_refs = os.listdir(args.ref_dir)
#     print(list_refs)
#
#     os.chdir(args.ref_dir)
#
#     fasta_list = ['.fas', '.fa', '.fasta']
#
#     file_count = 0
#     count = 1
#     for file in list_refs:
#         file_count+=1
#
#     for tail in fasta_list:
#         for file in list_refs:
#             if re.search(tail, file) and count <= file_count:
#                 count+=1
#                 subprocess.call(['bowtie2-build', file, file])
#                 #print(file)
#
#     splt_list = []
#     list_reads = os.listdir(args.read_dir)
#     for item in list_reads:
#         splt_item = item.split('_')
#         splt_item[1] = int(splt_item[1])
#         splt_list.append(splt_item)
#     organize = sorted(splt_list, key=lambda file: file[1])
#     #print(organize)
#
#     dict_count = 0
#     read_dict = defaultdict(list)
#     for item in organize:
#         item[1] = str(item[1])
#         #print(item)
#         joined = '_'.join(item)
#         #print(joined)
#         read_dict[int(item[1])].append(joined)
#         dict_count+=1
#     #print(read_dict)
#
#     ref_dict = {}
#     for item in list_refs:
#         split_ref = item.split('_')
#         ref_dict[int(split_ref[1])] = item
#     #print(ref_dict)
#
#     for read,read_value in read_dict.items():
#         for ref,ref_value in ref_dict.items():
#             if read == ref:
#                 print(read_value[0])
#                 print(read_value[1])
#                 print(ref_value)
#
#     #subprocess.call(['ls', args.read_dir'/newClade_2_01.R1_.fastq'])
#     #subprocess.call(['pwd'])
#                 subprocess.call(['bowtie2', '-p', '6', '--very-fast', '-x', args.ref_dir + ref_value , '-1', args.read_dir + read_value[1] , '-2', args.read_dir + read_value[0] , '--al-conc' , args.read_dir + read_value[1]])
#
#     #subprocess.call(['for i in $(ls )'])
#
#
#     # for file in list_refs:
#     #     for tail in fasta_list:
#     #         if tail in file:
#     #             print(file)
#     #             subprocess.call(['bowtie2-build', file, file])
#
#
#
#
#
#
# if __name__ == '__main__':
#     main()
