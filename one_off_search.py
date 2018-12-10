#! /usr/bin/env python

#file = open('full_test_best_map.sam','r')
#file = open('test_best_map.sam','r')

#with open('full_test_best_map.sam') as file:
with open('best_map.sam') as file:

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
	
			if num > 1830415 and num < 1830454:
				print(i)
