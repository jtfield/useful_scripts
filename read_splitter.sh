#! /usr/bin/env bash

cd $1

tail=$2

#seq -f "%02g-a.txt" 6 10
list=$(ls *.fastq | awk -F '_' '{print $2}')

for i in $list; do
  printf "$i"
done
