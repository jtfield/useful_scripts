#! /usr/bin/env python

import argparse


def parse_args():
	parser = argparse.ArgumentParser()
	parser.add_argument('--sam_file')
	parser.add_argument('--gt_num')
	parser.add_argument('--lt_num')
	return parser.parse_args()

def main():
    args = parse_args()
    with_open(args.sam_file) as file:
	read_position_start = args.gt_num
	read_position_end = args.lt_num


#with open('best_map.sam') as file:

#readdat = file.read()

		next(file)
		next(file)
		next(file)
		red = file.readlines()
		for i in red:
			line_split = i.split('\t')
			pos = line_split[3:4]
			for item in pos:
				num = int(item)

				# if num > 1830415 and num < 1830454:
				# 	print(i)
				if num > read_position_start and num < read_position_end:
					print(i)


if __name__ == '__main__':
    main()
